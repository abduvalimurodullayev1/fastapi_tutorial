from fastapi import Depends, HTTPException, status
from fastapi.security import oauth2, OAuth2PasswordBearer

import token1

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def get_current_user(data: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return token1.verify_token(data, credentials_exception)
