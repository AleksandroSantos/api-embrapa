import sys
sys.path.insert(1, "config")

import jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta
from config import api_config

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# Funções de autenticação
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return user_dict


def authenticate_user(fake_db, username: str, password: str):
    user = get_user(fake_db, username)
    if not user:
        return False
    if not verify_password(password, user["hashed_password"]):
        return False
    return user


def create_access_token(data: dict):
    expires_delta = timedelta(minutes=api_config.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, api_config.SECRET_KEY, algorithm=api_config.ALGORITHM
    )
    return encoded_jwt


# Função para decodificar e verificar o token JWT
def get_current_user(token: str):
    try:
        payload = jwt.decode(
            token, api_config.SECRET_KEY, algorithms=[api_config.ALGORITHM]
        )
        username: str = payload.get("sub")
        if username is None:
            return None
    except jwt.ExpiredSignatureError:
        return None
    except jwt.JWTError:
        return None
    return username
