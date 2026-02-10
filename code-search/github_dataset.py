import requests
import json
import os
from tqdm import tqdm

# NO TOKEN REQUIRED
HEADERS = {
    "Accept": "application/vnd.github.v3+json"
}

REPOS = [

    # Core Python frameworks (must-have)
    "pallets/flask",
    "django/django",
    "fastapi/fastapi",

    # Data science / AI (very important)
    "numpy/numpy",
    "pandas-dev/pandas",
    "scikit-learn/scikit-learn",
    "tensorflow/tensorflow",
    "pytorch/pytorch",
    "huggingface/transformers",

    # Web / JS popular frameworks
    "facebook/react",
    "expressjs/express",

    # Python utilities (clean readable code)
    "psf/requests",

    # Algorithms / coding interview (excellent for demos)
    "TheAlgorithms/Python"

]

dataset = []
idx = 1


def get_repo_files(repo):
    url = f"https://api.github.com/repos/{repo}/contents"
    response = requests.get(url, headers=HEADERS)

    if response.status_code != 200:
        print("Error:", response.text)
        return []

    return response.json()


for repo in REPOS:
    print("Fetching repo:", repo)

    files = get_repo_files(repo)

    for f in tqdm(files):

        if not f["name"].endswith((".py", ".js", ".java")):
            continue

        raw_url = f.get("download_url")

        if not raw_url:
            continue

        try:
            code = requests.get(raw_url).text
        except:
            continue

        dataset.append({
            "id": str(idx),
            "description": f["name"],
            "code": "\n".join(code.split("\n")[:20])
        })

        idx += 1


os.makedirs("data", exist_ok=True)

with open("data/snippets.json", "w") as f:
    json.dump(dataset, f, indent=2)

print("✅ Dataset created:", len(dataset), "snippets")
