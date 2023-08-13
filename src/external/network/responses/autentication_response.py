from typing import Optional
from pydantic import BaseModel

class AuthenticationMetadataResponse(BaseModel):
    name: Optional[str] = None

class AuthenticationUserResponse(BaseModel):
    email: str
    user_metadata: AuthenticationMetadataResponse

class AuthenticationResponse(BaseModel):
    expires_in: int
    access_token: str
    refresh_token: str
    user: AuthenticationUserResponse
