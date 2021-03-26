import csv


lists=[["Top Gun", "Risky Business", "Minority Report"], ["Titanic", "The Revenant", "Inception"], ["Training Day", "Man on Fire", "Flight"]]

with open('../cs50/movies.csv', 'w') as f:

    writer=csv.writer(f, delimiter=',')

    for list in lists:

        writer.writerows(list)