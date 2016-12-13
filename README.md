# Madagascar - Modules divers

## INFO PRINCIPALE
Ces modules sont compatibles avec odoo v9 et v10 (plus tard). Plus d'anciennes versions.
Le repository "l10n_mg" a été viré et effacé de github car n'a pas évolué et plein d'erreurs.

## Objectifs principaux:
* Fournir les localisations en Malagasy et dans la législation Malagasy les guides du PCG 2005
* Fournir autant que possible des modules spécifiques à MG
* Réunir autour de ce projet des bonnes volontés (dév, experts...) pour l'améliorer et le rendre meilleur.
* Apprendre aux nationaux de partager et investir dans l'opensource

## odoo et le l10n_mg :
Toujours utiliser odoo quelle que soit la nature de votre entreprise: cycle achats, cycle production, cycle de vente, comptabilisation des dépenses, recettes, opérations diverses...

# Usage

* Télécharger le module
* Rajouter dans les "addonspaths"
* Lors de la création d'une base de données, choisir le Pays : Madagascar
* Activer le module Comptabilité et Finances qui va intégrer l10n_mg (QUI NE CONTIENT PAS DE PLAN COMPTABLE !!!)
* Configurer le Nb de digits (longueur de comptes) dans la fiche de la société
* Dans la configuration de la comptabilité, installer un schéma en choisissant le module qui convient à votre société
  * l10n_mg_standard : si grande société qui déclare ses TVA
  * l10n_mg_pme : si société non assujettie à la déclaration de TVA mais tenant une comptabilité complète
  * l10n_mg_tpe : si vous avez une petite société que vous pouvez gérer avec le Système minimal de trésorerie
* Vous pouvez installer autres modules s'il y en a plus tard !

# Known issues / Roadmap

* [ ] Livrer les codes complets en v9
* [ ] Livrer les codes complets en v10
* [ ] Revoir la licence
* SOUHAIT: validation par des spécialistes en comptabilité et finances et droits fiscaux Malagasy
* SOUHAIT: revue des textes, titres, libellés, mots par des experts
* SOUHAIT: reportings spécifiques

# Credits

* Equipe Informatique du Groupe Vidzar
* Nos anciens stagiaires de l'ENI

## Contributors

* Harison Frédéric RAMANDANIARIVO <fredericramanda@gmail.com>

## Maintainer

* Harison Frédéric RAMANDANIARIVO <fredericramanda@gmail.com>
* Vous etes tous invités à soumettre des suggestions et des améliorations.
* Mais vous pouvez forker aussi.
