import json

data = {
    "target": "10.0.2.15",
    "scan_results": [
        {"port": 22, "status": "CLOSED"},
        {"port": 80, "status": "CLOSED"},
        {"port": 443, "status": "CLOSED"},
        {"port": 8000, "status": "OPEN"},
        {"port": 9000, "status": "CLOSED"}
    ]
}

with open("scan_report.json", "w") as file:
    json.dump(data, file, indent=4)

print("JSON report created: scan_report.json")
