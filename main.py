from fastapi import FastAPI

app = FastAPI()

# Lista de cuentas de MT5 permitidas
CUENTAS_VIP = ["1234567", "34221750", "19904047"]

@app.get("/validar")
def validar(cuenta: str):
    if cuenta in CUENTAS_VIP:
        return {"status": "autorizado"}
    return {"status": "denegado"}
