import requests

url = "https://pokeapi.co/api/v2/pokemon/"


def getPoki(poki):
    response = requests.get(f"{url}{poki}")

    if response.ok:
        data = response.json()
        print(data)
    else:
        print("error")


poki = input("Pick Pokimon: ")


getPoki(poki)
