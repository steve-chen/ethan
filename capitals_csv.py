import csv
import sys

csv_file = open("country-list.csv", "r")
reader = csv.reader(csv_file)

#print(f"sys.argv = {sys.argv}")
#print(f"len(sys.argv) = {len(sys.argv)}")

if len(sys.argv) == 1:
    for line in reader:
        country, capital = line[0], line[1]
        print(f"The capital of {country} is {capital}.")
elif len(sys.argv) == 2:
    ask_country = sys.argv[1]
    print(f"Looking up the capital for {ask_country}")


    for line in reader:
        country, capital = line[0], line[1]
        if country.lower() == ask_country.lower():
            print(f"The capital of {ask_country} is {capital}.")
            sys.exit(0)
    
    print(f"We couldn't find your country!")
elif len(sys.argv) > 2:
    print("That capitals isn't on our list.")
    

