# GST Notice Reply Draft Assistant

This repository provides a simple Streamlit app to draft a structured reply to GST notices. The app lets you upload:

- A GST notice (PDF or text)
- Supporting workings (optional, PDF or text)
- A sample reply format to mimic
- Your optional opinion or specific points to include

It then generates a structured reply using a consistent format, references to relevant GST law, and highlights the facts, issues, and responses.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## Notes

This is a template-based drafting tool. It does not provide legal advice.
