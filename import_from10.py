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
    for row in modele_data:
        code_prefix = row['code'][:3]  # Extract first 3 digits
        account_type_map[code_prefix] = row['account_type']

    # Parse the XML file
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Prepare data for CSV
    data = []
    for record in root.findall(".//record"):  # Adjust path if needed
        record_data = {}
        for field in record.findall("field"):
            name = field.get("name")
            if name == "code":
                code = field.text
                record_data[name] = code
                record_data["account_type"] = account_type_map.get(code[:3], '')  # Map account_type
            else:
                record_data[name] = field.text
            record_data["id"] = record.get("id")  # Get the 'id' from the record tag
        data.append(record_data)

    # Get the desired header order from the modele file
    csv_headers = headers

    # Write to CSV
    with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_headers)
        writer.writeheader()
        for row in data:
            # Map XML field names to CSV headers and fill missing values
            csv_row = {}
            for header in csv_headers:
                if header == 'account_type' and 'account_type' in row:
                    csv_row[header] = row['account_type']
                elif header in ('id', 'name', 'code', 'name@fr') and header in row:
                    csv_row[header] = row[header]
                else:
                    csv_row[header] = ''  # Default to empty string if not found
            writer.writerow(csv_row)


# Usage
xml_file = "account_chart_template_data.xml"  # Replace with your XML file path
csv_file = "output.csv"  # Replace with your desired CSV output file path
modele_file = "account.account-fr.txt"  # Replace with your modele file path

xml_to_csv(xml_file, csv_file, modele_file)