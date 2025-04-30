import xml.etree.ElementTree as ET
import csv

def xml_to_csv(xml_file, csv_file, modele_file):
    """
    Converts an XML file to a CSV file, mapping account types based on the first three digits of the code.

    Args:
        xml_file (str): Path to the XML file.
        csv_file (str): Path to the output CSV file.
        modele_file (str): Path to the modele (account.account-fr.txt) file 
                          to get the CSV header and account types.
    """

    # Parse the modele file to get headers and account type mapping
    modele_data = []
    with open(modele_file, 'r', encoding='utf-8') as f:
        csv_reader = csv.reader(f)
        headers = next(csv_reader)  # Get the header row
        for row in csv_reader:
            modele_data.append(dict(zip(headers, row)))

    # Create a dictionary to map the first 3 digits of the code to account_type
    account_type_map = {}
    english_name = {}
    for row in modele_data:
        code_prefix = row['code'][:3]  # Extract first 3 digits
        account_type_map[code_prefix] = row['account_type']
        english_name[row['code']] = row['name']  # Store the English name

    # Parse the XML file
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Prepare data for CSV
    data = []
    for record in root.findall(".//record"):  # Adjust path if needed
        record_data = {}
        name_value = None
        code_six = None
        for field in record.findall("field"):
            name = field.get("name")
            if name == "name":
                name_value = field.text
            elif name == "code":
                code = field.text
                code_six = (code + "000000")[:6]  # Ensure code is 6 digits
                record_data[name] = code_six
                record_data["account_type"] = account_type_map.get(code[:3], '')  # Map account_type
            elif name == "tag_ids" and 'eval' in field.attrib:
                eval_str = field.attrib['eval']
                record_data[name] = 'account.' + eval_str[14:-5]
            else:
                if 'eval' in field.attrib:
                    record_data[name] = field.attrib['eval']
                else:
                    record_data[name] = field.text
        record_data["name"] = english_name.get(code_six, name_value)  # Map to English name
        record_data["name@fr"] = name_value
        record_data["id"] = record.get("id")
        if "reconcile" not in record_data:
            record_data["reconcile"] = 'False'
        data.append(record_data)

    # Get the desired header order from the modele file
    csv_headers = headers

    # Write to CSV
    with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_headers, quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
        writer.writeheader()
        for row in data:
            # Map XML field names to CSV headers and fill missing values
            csv_row = {}
            for header in csv_headers:
                if header == 'account_type' and 'account_type' in row:
                    csv_row[header] = row['account_type']
                elif header in ('id', 'name', 'code', 'reconcile', 'name@fr', 'tag_ids') and header in row:
                    csv_row[header] = row[header]
                else:
                    csv_row[header] = ''  # Default to empty string if not found
            writer.writerow(csv_row)


# Usage
xml_file = "/home/framandaniarivo/factory/ravintsara/current/custom/odoomg/l10n_mg/old_data/account_template_data.xml"
csv_file = "/home/framandaniarivo/factory/ravintsara/current/custom/odoomg/l10n_mg/data/account.account-mg.csv"
modele_file = "/home/framandaniarivo/factory/ravintsara/current/odoo/home/odoo/odoo/addons/l10n_fr/data/template/account.account-fr.csv"

xml_to_csv(xml_file, csv_file, modele_file)