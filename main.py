from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

class LicenseRequest(BaseModel):
    mt5AccountId: str
    product: str

# Configura tus cuentas y sus fechas de vencimiento aquí
CUENTAS_EXPIRACION = {
    "1234567": "2026-12-31",
    "34221750": "2027-05-03",
    "19904047": "2027-05-03",
    "19964266": "2027-02-03",
}

@app.post("/api/validate")
async def validar(request: LicenseRequest):
    cuenta = request.mt5AccountId
    
    if cuenta in CUENTAS_EXPIRACION:
        fecha_exp = datetime.strptime(CUENTAS_EXPIRACION[cuenta], "%Y-%m-%d")
        
        # Comparamos la fecha actual con la de expiración
        if datetime.now().date() <= fecha_exp.date():
            return {"status": "ACTIVE", "message": f"Válido hasta {CUENTAS_EXPIRACION[cuenta]}"}
        else:
            return {"status": "EXPIRED", "message": "Tu licencia ha caducado"}
            
    return {"status": "DENIED", "message": "Cuenta no autorizada"}
