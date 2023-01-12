import json
import sys


with open("country-list.json", "r") as jsonFile:
    capitals = json.load(jsonFile)
    jsonFile.close()

if len(sys.argv) == 1:
    for line in capitals:
        country, capital = line.keys(), line.values()
        print(f"The capital of {country} is {capital}.")
elif len(sys.argv) == 2:
    ask_country = sys.argv[1]
    print(f"Looking up the capital for {ask_country}")


    for line in capitals:
        country, capital = line.keys(), line.values()
        if country.lower() == ask_country.lower():
            print(f"The capital of {ask_country} is {capital}.")
            sys.exit(0)
    
    print(f"We couldn't find your country!")
elif len(sys.argv) > 2:
    print("That capitals isn't on our list.")
    

