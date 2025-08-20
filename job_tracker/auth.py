from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

# Fake users database (tokens mapped to users)
fake_users_db = {
    "admin_token": {"username": "admin", "role": "admin"},
    "user1_token": {"username": "alice", "role": "user"},
    "user2_token": {"username": "bob", "role": "user"},
}

# OAuth2 scheme - expects token in Authorization header
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Dependency: get current user
def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_users_db.get(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing token",
        )
    return user
