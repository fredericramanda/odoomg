# Madagascar - Comptabilité

Comptatible avec odoo v9 et 10 bientôt.

Ce module ne contient pas de plan de comptes : il sera activé en premier pendant l'installation de l'application Finances et comptabilité d'odoo.

Après, l'administrateur doit choisir un plan de compte en activant des modules plus spécifiques:
- l10n_mg_tpe : pour les très petites entreprises
- l10n_mg_pme : pour les moyennes entreprises qui ne sont pas assujetties à la TVA
- l10n_mg_standard : pour les entreprises qui ont l'obligation de déclarer la TVA.

Cette décomposition en module principal "vide" et module de plan de compte à part est inspirée des modules l10n_cn_XXX (Chine)

Voir README complet de ce groupe de modules
