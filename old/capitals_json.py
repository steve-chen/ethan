import json
import sys

with open("country-list.json", "r") as jsonFile:
    all_countries = json.load(jsonFile)
    jsonFile.close()

if len(sys.argv) == 1:
    for country in all_countries:
        country_name, capital_name = country['country'], country['capital']
        print(f"The capital of {country_name} is {capital_name}.")
elif len(sys.argv) == 2:
    ask_country = sys.argv[1]
    print(f"Looking up the capital for {ask_country.capitalize()}")

    for country in all_countries:
        country_name, capital_name = country['country'], country['capital']
        if country_name.lower() == ask_country.lower():
            print(f"Found it! The capital of {ask_country.capitalize()} is {capital_name}.")
            sys.exit(0)
    print(f"We couldn't find your country!")
elif len(sys.argv) > 2:
    print("That capitals isn't on our list.")
    

