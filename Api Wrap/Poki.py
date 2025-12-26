import requests
import json

url = "https://pokeapi.co/api/v2/pokemon/"


def getPoki(poki):
    response = requests.get(f"{url}{poki}")

    if response.ok:
        data = response.json()
        return data
    else:
        print("error")


poki = input("Pick Pokimon: ")


data = getPoki(poki)

print(f"[{poki}]\n")
print(f"Height: {data['height']}")
print(f"Weight: {data['weight']}")
for ab in data["abilities"]:
    print(f"Ability: {ab['ability']['name']}")

for stat in data["stats"]:
    f = stat["base_stat"]
    s = stat["stat"]["name"]
    print(f"{f}: {s}")
