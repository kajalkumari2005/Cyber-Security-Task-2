html = """
<html>
<head>
    <title>Network Reconnaissance Report</title>
</head>
<body>
    <h1>Network Reconnaissance Report</h1>

    <h2>Target</h2>
    <p>10.0.2.15</p>

    <h2>Port Scan Results</h2>

    <table border="1">
        <tr>
            <th>Port</th>
            <th>Status</th>
        </tr>
        <tr><td>22</td><td>CLOSED</td></tr>
        <tr><td>80</td><td>CLOSED</td></tr>
        <tr><td>443</td><td>CLOSED</td></tr>
        <tr><td>8000</td><td>OPEN</td></tr>
        <tr><td>9000</td><td>CLOSED</td></tr>
    </table>
</body>
</html>
"""

with open("scan_report.html", "w") as file:
    file.write(html)

print("HTML report created: scan_report.html")
