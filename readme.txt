Fonction principale :
Renommer des fichiers selon un modèle de nom donné et une incrémentation numérique.

Utilisation :
Si vous utilisez le script en tant que fichier.
- Placer le fichier dans le répertoire de travail
- Renommer le fichier en .code.py  # Si le fichier n'est pas caché, il sera renommé également
- Effectuer la commande ./.code.py

Template renommage:
file_xy_00000.ext
file = var(prefix)
xy = deux caractères aléatoires (voir § "Utilisation du random")
00000 = incrémentation (numéro du fichier)
ext = extension du fichier

Fonctionnalités :
En tant qu'utilisateur, il est possible de modifier le contenu de la variable prefix (ligne 13).

Fonctionnement :
Basé sur Linux voici la procédure de fonctionnement du script.
- Effectuer un "ls | sort -n" dans le répertoire courant
- Envoyer le résultat de cette commande dans le fichier .file_list
- Récupérer le contenu du fichier .file_list
- Créer une variable qui contient le pochoir avec l'entier incrémenté
- Effectuer un "mv <old_file> <pochoir>"
- Indiquer la réussite / échec de l'opération menée

Utilisation du random :
On place dans notre pochoir 2 caractères random qui servent à éviter la perte de données.
Effectivement, la suite de commandes suivante aura pour conséquence la perte du fichier 2 et l'écrasement du fichier 1 par le contenu du fichier 2.
echo "test1" > file1 ; echo "test2" > file2 ; mv test2 test1
Pour éviter cette situation, on génère 2 caractères "aléatoires" afin d'éviter la perte de données au cas où l'on exécute le script deux fois de suite sans changer le préfix.
