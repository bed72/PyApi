from typing import Optional
from pydantic import BaseModel

class AuthenticationMetadataResponse(BaseModel):
    name: Optional[str] = None

    @staticmethod
    def from_json(json: any):
        return AuthenticationMetadataResponse(
            name=json['name']
        )

class AuthenticationUserResponse(BaseModel):
    email: str
    user_metadata: AuthenticationMetadataResponse

    @staticmethod
    def from_json(json: any):
        return AuthenticationUserResponse(
            email=json['email'],
            user_metadata=AuthenticationMetadataResponse.from_json(json['user_metadata'])
        )

class AuthenticationResponse(BaseModel):
    expires_in: int
    access_token: str
    refresh_token: str
    user: AuthenticationUserResponse

    @staticmethod
    def from_json(json: any):
        return AuthenticationResponse(
            expires_in=json['expires_in'],
            access_token=json['access_token'],
            refresh_token=json['refresh_token'],
            user=AuthenticationUserResponse.from_json(json['user'])
        )
