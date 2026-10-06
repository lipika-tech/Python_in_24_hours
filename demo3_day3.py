import csv

with open("students.csv", newline="",
          encoding = "utf -8") as f:
    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
        print(row)

orders = [{"product":"pen","qty":10},
          {"product":"book","qty":4}
 with open("orders.csv","w", newline="") as f:
           w=csv.DictWriter(f, fieldnames =["product", "qty"])
           w.writeheader()
           w.writerows(orders)]
    
          
