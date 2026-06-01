import json
import csv
import io

def format_json(data):
    return json.dumps(data, indent=2)

def format_csv(data):
    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=data.keys())
    writer.writeheader()
    writer.writerow(data)
    return output.getvalue()