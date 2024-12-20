#!/usr/bin/env python3
from models import Client
import cgi
import cgitb
import logging

# Activer le débogage CGI
cgitb.enable()

# Récupérer les données du formulaire
form = cgi.FieldStorage()
nom = form.getvalue('nom')
email = form.getvalue('email')
siret = form.getvalue('siret')

# Début de la réponse HTML
print("Content-type: text/html\n")
print("<html>")
print("<head>")
print("<title>Inscription</title>")
print("</head>")
print("<body>")

# Vérifier si les champs sont vides
if not nom or not email or not siret:
    print("<h2>Erreur : Tous les champs sont obligatoires !</h2>")
    print("<p>Veuillez revenir en arrière et remplir le formulaire.</p>")
else:
    # Générer la réponse HTML personnalisée
    print("<h2>Merci pour votre inscription !</h2>")
    print(f"<p>Nom : {nom}</p>")
    print(f"<p>Email : {email}</p>")
    print(f"<p>Siret : {siret}")
    


print("</body>")
print("</html>")
