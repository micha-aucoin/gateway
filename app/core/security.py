from fastapi.security import OAuth2PasswordBearer

from app import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f".{settings.api_v1_prefix}/auth/token")
