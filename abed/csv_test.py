import csv

with open('players.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row[9]+' '+row[10])
        print("\n\n\ni am a newline\n\n\n")
