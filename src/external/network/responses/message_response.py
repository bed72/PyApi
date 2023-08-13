from typing import Optional
from pydantic import BaseModel

class MessageResponse(BaseModel):
    msg: Optional[str] = None
    error: Optional[str] = None
    error_description: Optional[str] = None
