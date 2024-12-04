from datetime import datetime

from pydantic import BaseModel, Field, ConfigDict, HttpUrl
from pydantic.alias_generators import to_camel

from services.movie.models.enums import LocationEnum


class Genre(BaseModel):
    name: str


class MovieResponse(BaseModel):
    model_config = ConfigDict(extra="forbid",
                              populate_by_name=True,
                              alias_generator=to_camel)

    id: int
    name: str
    price: int
    description: str
    image_url: HttpUrl
    location: LocationEnum
    published: bool
    genre_id: int
    genre: Genre
    created_at: datetime
    rating: float = Field(ge=0, le=5)
