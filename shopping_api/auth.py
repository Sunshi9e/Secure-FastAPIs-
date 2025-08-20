from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

# Fake users database
fake_users_db = {
    "admin_token": {"username": "admin", "role": "admin"},
    "customer_token": {"username": "john", "role": "customer"},
}


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_users_db.get(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing token",
        )
    return user

def require_admin(user: dict = Depends(get_current_user)):
    if user["role"] != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin access required",
        )
    return user
