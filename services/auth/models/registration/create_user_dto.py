from pydantic import BaseModel, Field, ConfigDict
from pydantic.alias_generators import to_camel


class CreateUserDto(BaseModel):
    model_config = ConfigDict(populate_by_name=True,
                              alias_generator=to_camel)

    banned: bool = Field(default=False)
    email: str
    full_name: str
    password: str
    verified: bool = Field(default=True)
