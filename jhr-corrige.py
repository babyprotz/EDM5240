# coding: utf-8

# SUPER BONNE IDÉE QUE DE PRENDRE LA QUALITÉ DE L'AIR

import csv
import requests
from bs4 import BeautifulSoup
import time
import datetime

now = datetime.datetime.now()

jour = now.day
mois = time.strftime("%b")
annee = now.year
heure = time.strftime("%Hh%M")

fichier= "air200-jhr.csv"

url1= "http://meteo.gc.ca"
url2= "/airquality/pages/"
url3= "_f.html"

entetes = {
    "User-Agent": "Alex Proteau veut s'informer des conditions de l'air",
    "From":"alexproteau6@gmail.com"
}
url = url1 + url2
# print(url)
q = requests.get(url,headers=entetes)
page1 = BeautifulSoup(q.text,"html.parser")

# Tout ce que j'ai fait, c'est de permettre à ton script
# d'aller chercher les indices de qualité de l'air de toutes les villes
# au Canada

# Il y a donc 2 boucles.
# La première va chercher toutes les provinces et territoires à partir de la page d'accueil

provinces = page1.find("ul", class_="nav")
for province in provinces.find_all("li"):
    urlProv = province.a.get("href")
    prov = province.span.text
    print(urlProv,prov)
    
    lien1 = url1+urlProv
    # print(lien1)
    
    p = requests.get(lien1,headers=entetes)
    pageProv = BeautifulSoup(p.text,"html.parser")
    
    tableau = pageProv.find("tbody")

    # Et la 2e boucle va chercher chacune des villes par province
    # C'est à l'intérieur cette 2e boucle qu'on écrit notre fichier CSV
    
    for ligne in tableau.find_all("tr"):
        
        indice = []
        
        ville = ligne.a.text
        qualite = ligne.find("td",headers="current-observation").text
        qualite = qualite[0]
        # print(ville,qualite)
        
        indice.append(ville)
        indice.append(prov)
        indice.append(qualite)
        indice.append(jour)
        indice.append(mois)
        indice.append(annee)
        indice.append(heure)
        print(indice)
        
        travail = open(fichier,"a")
        alexproteau = csv.writer(travail)
        alexproteau.writerow(indice) # Ici, tu avais écrit (fichier); c'est (indice) que tu souhaitais écrire