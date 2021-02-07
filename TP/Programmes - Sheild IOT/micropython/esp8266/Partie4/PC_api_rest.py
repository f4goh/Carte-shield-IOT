"""
Programme sur PC
https://blynkapi.docs.apiary.io/
"""

import requests, json

proxies = {
  'http': 'http://172.30.137.29:3128',
}

# Authentification token
BLYNK_AUTH = '8ttq4bU0Pt-EB8uvTXVqOHlAhYOKe4cg'

# URL de base
BLYNK_URL = "http://blynk-cloud.com/"


def write(pin,value):
    # url de la requete
    url = BLYNK_URL + BLYNK_AUTH + "/update/" + pin+ "?value=" + str(value)
    print("l'url est",url)
    response = requests.get(url)
    #response = requests.get(url,proxies=proxies)
    print(response)

def property(pin,prop,value):
    # url de la requete
    url = BLYNK_URL + BLYNK_AUTH + "/update/" + pin+ "?"+prop+"=" + value
    print("l'url est",url)
    response = requests.get(url)
    #response = requests.get(url,proxies=proxies)
    print(response)

def read(pin):
    # url de la requete
    url = BLYNK_URL + BLYNK_AUTH + "/get/" + pin
    print("l'url est",url)
    response = requests.get(url)
    #response = requests.get(url,proxies=proxies)
    #response qui va être convertit en liste
    print(response)
    lst = response.json()
    print(lst[0])

#lecture de la gauge
read("V1")

#mets à jour la gauge V1 à 325
write("V1",325)

#change la couleur de la gauge
property("V1","color","%2385c100")





