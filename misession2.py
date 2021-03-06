# coding: utf-8

#Au départ, je dois importer mon demander à mon scripte python de lire les fichiers csv. Je lui fais donc la requete
#Par la suite, je dosi importer le plugin BeautifulSoup. Je crée donc un environement virtuel que j'active. 
#Pour le bienfait de mon travail, j'aurai besoin de la date et et de l'heure, alors j'importe l'heure et la journée

#Le but de mon travail est de retrouver les conditions dans chaque province.

import csv
import requests
from bs4 import BeautifulSoup
import time
import datetime

#Je me crée un nom de fichier ou l'on pourra apercevoir mes résulats compilés

fichier= "air200.csv"

#Pour cela, je dois avoir deux URL. Le premier m'amènera à l'index ou se retrouve tout le travail, l'autre étant la fin de l'url.

url1= "http://meteo.gc.ca/airquality/pages/"
url2= "_f.html"

#À des fins professionnelles, je dois m'identifier

entetes = {
    "User-Agent": "Alex Proteau veut s'informer des conditions de l'air",
    "From":"alexproteau6@gmail.com"
}

# contenu = requests.get(url1,headers=entetes)

# page = BeautifulSoup(contenu.text,"html.parser")

# print(page)

#Chaque ville correspond à une certaine portion de l'adresse URL. Pour la trouver, je regarde ce qui différencie des autres et cela me donne le code de chacune des villes

codes= {
    
    
	"Fredericton" : "nbaq-002",
	"Saskatoon" : "skaq-002",
	"Montréal" : "onaq-008",
	"Calgary" : "abaq-002",
	"Victoria" : "bcaq-010",
	"St.John's" : "nlaq-001",
	"Toronto" : "onaq-001",
	"Winnipeg" : "mbaq-001",
	"Yellowknife" : "ntaq-001",
	"Halifax" : "nsaq-001",
	"Iqaluit" : "ntaq-002",
	"Ile-du-Prince-Édouard" : "peaq-003",
	"Whitehorse" : "ytaq-001"
	

}

#Étant donné que je veux savoir la condition de l'air à l'heure actuelle, j'imprime le jour, mois, année et l'heure à travers différentes équations.

now = datetime.datetime.now()

jour = now.day
mois = time.strftime("%b")
annee = now.year
heure = time.strftime("%Hh%M")

print("\n")
print("#"*50)
print("Nous sommes le {0} {1} {2}".format(jour,mois,annee))
print("Il est {0}\n".format(heure))

#Par la suite, je crée une loop qui me permettra de trouver le niveau de la qualité de l'air de la ville en question

for ville,code in codes.items():
    
#Je crée un url qui me permettra de trouver quel le but ma recherche

    
    url = "{}{}{}".format(url1,code,url2)
    print("L'URL pour {} est {}".format(ville,url))

#Je me connecte à l'URL que je viens de créer
    x = requests.get(url,headers=entetes,verify=False)

#Je demande à BeautifulSoup de me trouver le lien HTML recherché    
    page = BeautifulSoup(x.text,"html.parser")
    
    # print(page)

#Pour clore le tout, je crée une équation qui me permettra de trouver le niveau de l'air de la ville désirée
#En inspectant ma page, je regarde quel est la partie HTML qui me donne l'information concernant le niveau de l'air.
#Je rajoute .text pour avoir l'information en .text et j'ajoute .strip pour enlever les espaces.

    airquality = page.find("p", class_="withBorder").text.strip()
    quality=airquality[0]
    
#Je crée une formule qui me donnera le niveau de qualité de l'air selon deux variables, soit la ville{1} et le niveau{0}
    
    print(" Le niveau de qualité de l'air de la ville {1} est de {0} ".format(quality,ville))

#J'enregistre mes réponses sous un fichier en format.csv

    travail = open(fichier,"a")
    alexproteau = csv.writer(travail)
    alexproteau.writerow(fichier)
    i=+1
    
    #print(travail)
    
    