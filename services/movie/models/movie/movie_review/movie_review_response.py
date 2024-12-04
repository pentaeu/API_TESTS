from datetime import datetime

from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel


class User(BaseModel):
    fullname: str


class MovieReviewResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True, alias_generator=to_camel)

    user_id: str
    rating: float
    text: str
    created_at: datetime
    user: User
