import requests
import pandas as pd

all_poke_data = []

def main():
    for index in range(1, 152): 
        pokemon_data = fetch_poke_details(index)
        if pokemon_data:
            all_poke_data.append({
                "name": pokemon_data["name"],
                "type": pokemon_data["types"][0]["type"]["name"]
            })
    
    #save data to a CSV file using pandas
    df = pd.DataFrame(all_poke_data)
    df.to_csv("poke_data.csv", index=False)

def fetch_poke_details(poke_id):
    URL = f"https://pokeapi.co/api/v2/pokemon/{poke_id}"
    response = requests.get(URL)

    if response.status_code != 200:
        print("Error >>> Failed to fetch pokemon details! Pokemon ID: {poke_id}")
        return None
    
    return response.json()

if __name__ == "__main__":
    main()
