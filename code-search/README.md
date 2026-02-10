# AI Code Semantic Search (Endee)

An AI-powered tool that allows users to perform **semantic search** over code snippets. Unlike traditional keyword-based search, this tool understands the meaning and intent behind your queries using Natural Language Processing (NLP).

## Features

- **Semantic Understanding**: Uses `Sentence Transformers` (all-MiniLM-L6-v2) to find code based on context, not just keywords.
- **Automated Data Ingestion**: Fetches real-world code snippets from popular GitHub repositories (Flask, Django, FastAPI, React, etc.).
- **Interactive Web Interface**: Built with `Streamlit` for a seamless search experience.
- **Flexible Search**: Includes both a web-based app and a command-line interface (CLI) for quick searches.

##  Tech Stack

- **Language**: Python 3.x
- **NLP Model**: [Sentence Transformers](https://www.sbert.net/) (`all-MiniLM-L6-v2`)
- **Frontend**: [Streamlit](https://streamlit.io/)
- **Data Handling**: NumPy, Requests, tqdm

##  Installation

1. **Clone the repository**:
   ```bash
   git clone <your-repo-url>
   cd code-search
   ```

2. **Set up a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Data Preparation

Before running the search, you need to fetch and prepare the dataset:

1. **Fetch from GitHub**:
   ```bash
   python github_dataset.py
   ```
   *This will download snippets from several top-tier open-source repositories and save them to `data/snippets.json`.*

2. **Consolidate and Ingest**:
   ```bash
   python ingest.py
   ```
   *This combines various snippet sources into a single optimized search index at `data/code_data.json`.*

##  Usage

### Web Application (Recommended)
Run the interactive search tool in your browser:
```bash
streamlit run app.py
```

### CLI Search
Perform quick searches directly from your terminal:
```bash
python search.py
```

## Project Structure

- `data/`: Final processed datasets and raw snippets.
- `github_dataset.py`: Logic for scraping code from GitHub API.
- `ingest.py`: Combines and prepares data for the search engine.
- `search.py`: CLI implementation for semantic search.
- `app.py`: The main Streamlit web application.
- `requirements.txt`: Project dependencies.
