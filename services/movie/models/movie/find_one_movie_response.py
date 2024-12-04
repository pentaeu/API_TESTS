from typing import List

from pydantic import ConfigDict
from pydantic.alias_generators import to_camel

from services.movie.models.movie.movie_response import MovieResponse
from services.movie.models.movie.movie_review.movie_review_response import MovieReviewResponse


class FindOneMovieResponse(MovieResponse):
    model_config = ConfigDict(extra="forbid",
                              populate_by_name=True,
                              alias_generator=to_camel)

    reviews: List[MovieReviewResponse]
