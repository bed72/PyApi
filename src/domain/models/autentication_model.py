from pydantic import BaseModel

class AuthenticationModel(BaseModel):
    name: str
    email: str
    expires_in: int
    access_token: str
    refresh_token: str
