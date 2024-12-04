from pydantic import BaseModel, ConfigDict


class LoginDto(BaseModel):
    model_config = ConfigDict(extra="forbid")

    email: str
    password: str
