from pydantic import BaseModel

class SignInParameter(BaseModel):
    email: str
    password: str
