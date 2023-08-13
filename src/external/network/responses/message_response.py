from typing import Optional
from pydantic import BaseModel

class MessageResponse(BaseModel):
    msg: Optional[str] = None
    error: Optional[str] = None
    error_description: Optional[str] = None

    @staticmethod
    def from_json(json: any, is_authentication: bool = False):
        return MessageResponse(
                error = json['error'],
                error_description=json['error_description']
            ) if is_authentication else MessageResponse(
                msg = json['msg']
            )
