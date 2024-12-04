from pydantic import BaseModel, ConfigDict, Field, HttpUrl
from pydantic.alias_generators import to_camel

from services.movie.models.enums import LocationEnum


class CreateMovieDto(BaseModel):
    model_config = ConfigDict(populate_by_name=True, alias_generator=to_camel)

    name: str = Field(default="Название фильма")
    image_url: str = Field(default="https://example.com/image.png")
    price: int = Field(default=100)
    description: str = Field(default="Описание фильма")
    location: LocationEnum = Field(default=LocationEnum.SPB)
    published: bool = Field(default=True)
    genre_id: int = Field(default=1)
