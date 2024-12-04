from datetime import datetime
from pydantic import ConfigDict

from services.auth.models.base_user_response import BaseUserResponse


class UserResponse(BaseUserResponse):
    model_config = ConfigDict(populate_by_name=True)

    verified: bool = True
    createdAt: datetime = "2024-03-02T05:37:47.298Z"
    banned: bool = False
