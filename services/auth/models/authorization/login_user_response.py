from datetime import datetime
from uuid import UUID

from pydantic import ConfigDict, Field, BaseModel

from services.auth.models.base_user_response import BaseUserResponse


class UserLoginResponse(BaseModel):
    model_config = ConfigDict(extra="forbid",
                              populate_by_name=True)

    user: BaseUserResponse
    access_token: str = Field(alias="accessToken")
    refresh_token: UUID = Field(alias="refreshToken")
    expires_in: datetime = Field(alias="expiresIn")
