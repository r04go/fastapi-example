from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    id: Optional[str]
    nombre: str
    email: str
    passwd: str