from typing import Optional
from pydantic import BaseModel

class NoteSchema(BaseModel):
    title: Optional[str]
    content: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "title": "Logrocket",
                "content":"Logrocket is the most flexible"
            }
        }