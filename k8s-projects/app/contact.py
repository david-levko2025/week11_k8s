from pydantic import BaseModel,Field
from typing import Annotated


class Contact(BaseModel):
    first_name:Annotated[str,Field(max_length=50)]
    last_name:Annotated[str,Field(max_length=50)]
    phone_number:Annotated[str,Field(max_length=20)]


    def get_dict(self) -> dict:
        return{
            "first_name":self.first_name,
            "last_name":self.last_name,
            "phone_number":self.phone_number
        }