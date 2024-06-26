import os
import sys

sys.path.insert(1, "config")
sys.path.insert(1, "utils")

from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import List
from models import Producao, Processamento, Comercializacao, Importacao, Exportacao
from security import authenticate_user, create_access_token, get_current_user
from datetime import timedelta
from config import api_config
from utils import ler_csv


# Configuração do aplicativo FastAPI
app = FastAPI()

# Segurança e Autenticação
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

fake_users_db = {
    "user": {
        "username": "user",
        "full_name": "User",
        "email": "user@example.com",
        "hashed_password": "$2b$12$RX6xbfaxBBzWlEGkHjv1xeSbtFfhidNd.zPqp4VGCA4FPFcl1Fvji",  # senha: password
        "disabled": False,
    }
}


# Rotas protegidas com autenticação JWT
@app.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user["username"]})
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/producao/", response_model=List[Producao])
async def get_producao(token: str = Depends(oauth2_scheme)):
    username = get_current_user(token)
    if username is None:
        raise HTTPException(status_code=401, detail="Invalid token")
    return ler_csv(api_config.PRODUCAO_FILE)


@app.get("/processamento/", response_model=List[Processamento])
async def get_processamento(token: str = Depends(oauth2_scheme)):
    username = get_current_user(token)
    if username is None:
        raise HTTPException(status_code=401, detail="Invalid token")
    return ler_csv(api_config.PROCESSAMENTO_FILE)


@app.get("/comercializacao/", response_model=List[Comercializacao])
async def get_comercializacao(token: str = Depends(oauth2_scheme)):
    username = get_current_user(token)
    if username is None:
        raise HTTPException(status_code=401, detail="Invalid token")
    return ler_csv(api_config.COMERCIALIZACAO_FILE)


@app.get("/importacao/", response_model=List[Importacao])
async def get_importacao(token: str = Depends(oauth2_scheme)):
    username = get_current_user(token)
    if username is None:
        raise HTTPException(status_code=401, detail="Invalid token")
    return ler_csv(api_config.IMPORTACAO_FILE)


@app.get("/exportacao/", response_model=List[Exportacao])
async def get_exportacao(token: str = Depends(oauth2_scheme)):
    username = get_current_user(token)
    if username is None:
        raise HTTPException(status_code=401, detail="Invalid token")
    return ler_csv(api_config.EXPORTACAO_FILE)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
