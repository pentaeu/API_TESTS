from services.movie.helpers.genre_helper import GenreHelper
from services.movie.helpers.movie_helper import MovieHelper
from services.movie.models.genre.create_genre_dto import CreateGenreDto
from services.movie.models.genre.genre_response import GenreResponse
from services.movie.models.movie.create_movie_dto import CreateMovieDto
from services.movie.models.movie.find_all_movies_response import FindAllMoviesResponse
from services.movie.models.movie.find_one_movie_response import FindOneMovieResponse
from services.movie.models.movie.movie_response import MovieResponse


class MovieService:
    def __init__(self, api_utils) -> None:
        self.api_utils = api_utils

        self.genre_helper = GenreHelper(self.api_utils)
        self.movie_helper = MovieHelper(self.api_utils)

    def post_genre(self, create_genre: CreateGenreDto) -> GenreResponse:
        response = self.genre_helper.post_genre(json=create_genre.model_dump(by_alias=True,
                                                                             exclude_defaults=True))

        return GenreResponse(**response.json())

    def post_movie(self, create_movie: CreateMovieDto) -> MovieResponse:
        response = self.movie_helper.post_movie(json=create_movie.model_dump(by_alias=True,
                                                                             exclude_defaults=False))

        return MovieResponse(**response.json())

    def get_movies(self) -> FindAllMoviesResponse:
        response = self.movie_helper.get_movies()

        return FindAllMoviesResponse(**response.json())

    def get_movie(self, movie_id):
        response = self.movie_helper.get_movie(movie_id)

        return FindOneMovieResponse(**response.json())
