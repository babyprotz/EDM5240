#coding: utf-8

#Au départ, je dois importer mon demander à mon scripte python de lire les fichiers csv. Je lui fais donc la requete
#Par la suite, je dosi importer le plugin BeautifulSoup. Je crée donc un environement virtuel que j'active. 

import csv
from bs4 import BeautifulSoup
import requests
import time
import datetime

#Je donne un nom à mon fichier

fichier = "valeurmorue90-2014.csv"

#Objectif du travail: identifier le montant total recueilli par pêche en Atlantique lors de 1990 à 2014
#Pour cela, je dois avoir deux URL. Le premier m'amènera à l'index ou se retrouve tout le travail, l'autre étant la fin de l'url.
url1= "http://www.dfo-mpo.gc.ca/stats/commercial/land-debarq/sea-maritimes/s"
url2= "av-fra.htm"

#À des fins professionnelles, je dois m'identifier

entetes = {
    "User-Agent": "Alex Proteau s'intéresse aux poissons",
 
    "From":"alexproteau6@gmail.com"
}

#Afin de trouver la variable par année, je dois détailler chaque partie de l'HTML qui différencie.
#Changement=année


periode = {
	"90" : "1990",
	"91" : "1991",
	"92" : "1992",
	"93" : "1993",
	"94" : "1994",
	"95" : "1995",
	"96" : "1996",
	"97" : "1997",
	"98" : "1998",
	"99" : "1999",
	"00" : "2000",
	"01" : "2001",
	"02" : "2002",
	"03" : "2003",
	"04" : "2004",
	"05" : "2005",
	"06" : "2006",
	"07" : "2007",
	"08" : "2008",
	"09" : "2009",
	"10" : "2010",
	"11" : "2011",
	"12" : "2012",
	"13" : "2013",
	"14" : "2014",
 
 }
 
 
#Pour clore le tout, je crée une équation qui me permettra de trouver ce que je cherche.
#En inspectant ma page, je regarde quel est la partie HTML qui me donne l'information concernant le montant total
#Je rajoute .text pour avoir l'information en .text.

for years,periode in periode.items():

    url = "{}{}{}".format(url1,periode,url2)
    print("L'URL pour {} est {}".format(years,url))
    
    x = requests.get(url,headers=entetes,verify=False)
    
    page = BeautifulSoup(x.text,"html.parser")
    
    #print(page)
    
  
#Je crée une formule qui me donnera la valeur total selon deux variables, soit l'année{1} et le montant{0}
    total = page.find(class_="bg-info text-right").text
    valeur=total
    
    print(" La valeur de la peche commerciale par la Nouvelle-Écosse en Maritimes en {1} est de {0} $ ".format(total,periode))
    
#j'enregistre mon travail!

    travail = open(fichier,"a")
    alexproteau = csv.writer(travail)
    alexproteau.writerow(fichier)
    i=+1
