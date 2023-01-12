usage_help = """
Usage:
This will list out all the countries or states that the program knows about.
> capitals.py list

This will lookup the capital of one of the countries or states.
> capitals.py lookup [country or state]

This will add a new capital for a country or state
> capitals.py add [country] [capital]

This will delete a capital or state.  Please confirm with the user that they want to really delete. 
> capitals.py delete [country or state]

This will display how to use the application by showing the commands of "list", "lookup", "add", and "delete"
> capitals.py help
"""

import sys
import json


with open("convert.txt") as jsonFile:
    capitals = json.load(jsonFile)
    jsonFile.close()

command = sys.argv[1]
arguments = sys.argv[2:]


def save_file():
    with open('convert.txt', 'w') as convert_file: 
        convert_file.write(json.dumps(capitals))

if command == 'list':
    print(capitals)
    sys.exit(0)
elif command == 'help':
    print(usage_help)
    sys.exit(0)
elif command == 'lookup':
    try:
        print(f"The capital of {arguments[0].capitalize()} is {capitals[arguments[0]].capitalize()}")
    except KeyError:
        print(f"The capital of {arguments[0].capitalize()} is not in the dictionary.")
    sys.exit(0)
elif command == 'add':
    input_country = arguments[0]
    input_capital = arguments[1]
    input_country = input_country.lower()
    input_capital = input_capital.lower()
    capitals[input_country] = input_capital

    print("This is the new dictionary")
    print(capitals)
    save_file()

elif command == 'delete':
    del capitals[arguments[0]]
    save_file()
    