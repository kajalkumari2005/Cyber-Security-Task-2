import csv

data = [
    ["IP Address", "Port", "Status"],
    ["10.0.2.15", 22, "CLOSED"],
    ["10.0.2.15", 80, "CLOSED"],
    ["10.0.2.15", 443, "CLOSED"],
    ["10.0.2.15", 8000, "OPEN"],
    ["10.0.2.15", 9000, "CLOSED"]
]

with open("scan_report.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("CSV report created: scan_report.csv")
