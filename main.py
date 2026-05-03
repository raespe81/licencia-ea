from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Modelo para recibir los datos que envía MetaTrader
class LicenseRequest(BaseModel):
    mt5AccountId: str
    product: str

# Lista de cuentas permitidas
CUENTAS_VIP = ["1234567", "34221750", "19904047"]

@app.post("/api/validate")
async def validar(request: LicenseRequest):
    if request.mt5AccountId in CUENTAS_VIP:
        # Devolvemos "ACTIVE" para que el código MQL5 lo reconozca
        return {"status": "ACTIVE", "message": "Acceso concedido"}
    
    return {"status": "DENIED", "message": "Cuenta no autorizada"}
