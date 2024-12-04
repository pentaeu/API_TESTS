from typing import List

from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel

from services.movie.models.movie.movie_response import MovieResponse


class FindAllMoviesResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True,
                              alias_generator=to_camel)

    movies: List[MovieResponse]
    count: int
    page: int
    page_size: int
    page_count: int
