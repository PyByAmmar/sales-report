import csv
totals = {}

def read_sales():
    totals = {}

    with open("sales.csv", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
    
        for row in reader:
            category = row["category"]
            amount = float(row["amount"])
            totals[category] = totals.get(category, 0)+ amount


    for category, total in totals.items():
        print(category + ":", total)        
    return totals

def write_rep():
    totals = {}
    with open("report.csv", "w", newline="", encoding="utf-8") as out:
        writer = csv.writer(out)
        writer.writerow(["category", "total"])

        for category, total in totals.items():
            writer.writerow([category, total])
    return totals
try:
    totals = read_sales()
    totals = write_rep()  
except FileNotFoundError:
    print("sales.csv not found.")
except ValueError:
    print("A row has an invalid amount.")    
