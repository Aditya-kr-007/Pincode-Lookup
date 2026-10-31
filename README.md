# Pincode Lookup API

A small FastAPI service that looks up Indian pincodes and returns city, state, and district information.

## Run locally

```bash
python -m venv .venv
# Windows PowerShell: .venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Open `http://127.0.0.1:8000/docs` for the interactive API documentation.

## Endpoints

- `GET /` — service message
- `GET /pincode/{code}` — look up one six-digit pincode
- `POST /pincode/bulk` — look up up to 20 pincodes

The included dataset is a small sample in `data.py`.
