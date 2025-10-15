"""
Convert a Json file to csv file to be used in a quote app (Quote UnQuote)
"""
import json, os

with open("quotes.json", 'r') as file:
    data = json.load(file)

data = data['quotes']

with open('output.csv', mode='w', newline='') as file:
    for q in data:
        quote = q["author"] + "||" + q["quote"] + "\n"
        total = quote.replace('"','')
        file.writelines(total)
