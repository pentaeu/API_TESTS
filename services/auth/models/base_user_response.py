from typing import List
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field
from pydantic.alias_generators import to_camel

from services.auth.models.enums import RolesEnum


class BaseUserResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True,
                              alias_generator=to_camel)

    id: UUID
    email: str
    full_name: str
    roles: List[RolesEnum] = Field(default=[RolesEnum.USER])
