import json
import os

files = [
    "data/snippets.json",
    "data/basic_python_snippets.json",
    "data/interview_snippets.json"
]

combined = []

for file in files:
    if os.path.exists(file):
        print("Loading:", file)
        with open(file) as f:
            combined.extend(json.load(f))

print("Total snippets:", len(combined))

endee_data = []

for item in combined:
    text = f"{item.get('description','')} {item.get('code','')}"
    endee_data.append({
        "id": str(item.get("id")),
        "text": text
    })

os.makedirs("data", exist_ok=True)

with open("data/code_data.json", "w") as f:
    json.dump(endee_data, f, indent=2)

print("\nDataset ready for Endee ingestion")
