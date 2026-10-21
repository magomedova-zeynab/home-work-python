import csv

with open('text4.csv', 'r', encoding="utf-8") as infile, \
    open('output.csv', 'w', newline='', encoding='utf-8') as outfile:
    reader = csv.reader(infile)
    a = next(reader)
    writer = csv.writer(outfile)
    writer.writerow(a)
    for line in reader:
        name, category, price = line
        if int(price) > 100: writer.writerow(line)
