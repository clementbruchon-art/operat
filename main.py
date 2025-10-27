from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # à restreindre plus tard
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE = "https://operat.ademe.fr/api"

@app.post("/login")
def login(data: dict):
    r = requests.post(f"{BASE}/login_check", json=data)
    r.raise_for_status()
    return r.json()

@app.get("/clients")
def clients(token: str):
    headers = {"Authorization": f"Bearer {token}"}
    r = requests.get(f"{BASE}/user_accounts?user.id=5172&pagination=false", headers=headers)
    r.raise_for_status()
    return r.json()

@app.get("/client_token/{client_id}")
def client_token(client_id: int, token: str):
    headers = {"Authorization": f"Bearer {token}"}
    r = requests.get(f"{BASE}/user_accounts/{client_id}/token", headers=headers)
    r.raise_for_status()
    return r.json()

@app.get("/consumptions/{client_token}")
def consumptions(client_token: str):
    headers = {"Authorization": f"Bearer {client_token}"}
    r = requests.get(f"{BASE}/consumptions", headers=headers)
    r.raise_for_status()
    return r.json()

@app.get("/corrected/{client_token}")
def corrected(client_token: str):
    headers = {"Authorization": f"Bearer {client_token}"}
    r = requests.get(f"{BASE}/consumptions/get_certificate_list", headers=headers)
    r.raise_for_status()
    return r.json()
