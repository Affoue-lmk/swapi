import requests
import json

def find_ship():
    x = requests.get('https://swapi.dev/api/films/')
    for each_data in  x.json()["results"]:
        if each_data["title"]=="Return of the Jedi":
            print("---------Return of the Jedi-----------")
            for all in each_data["starships"]:
                y = requests.get(all)
                print(y.json()["name"])

def find_hyperdrive():
    print("----------Hyperdrive>=1.0----------")
    x = requests.get("https://swapi.dev/api/starships")
    for each in x.json()['results']:
        if float(each["hyperdrive_rating"])>=1.0:
            print(each["name"])

def find_crews_no():
    print("----------3=<crews>=100----------")
    x = requests.get("https://swapi.dev/api/starships")
    for each in x.json()['results']:
        new = each["crew"].split('-')
        if "," not in new[0]:
            if (len(new)==1):
                if int(new[0])>=3:
                    print(each["name"])
            else:
                if (int(new[0])>=3 and int(new[1])<=100):
                    print(each["name"])

find_ship()
find_hyperdrive()
find_crews_no()
