import random

from faker import Faker

from logger.logger_main import Logger
from services.movie.models.genre.create_genre_dto import CreateGenreDto
from services.movie.models.movie.create_movie_dto import CreateMovieDto, LocationEnum
from services.movie.movies_api_service import MovieService

faker = Faker()


class TestMovieCreate:
    def test_movie_create(self, api_utils_super_admin_movie_api):
        movie_service = MovieService(api_utils=api_utils_super_admin_movie_api)
        Logger.info("### Steps 1. Create genre")
        genre = CreateGenreDto(name=faker.name())
        created_genre = movie_service.post_genre(genre)
        movie = CreateMovieDto(name=faker.name(),
                               price=random.randint(100, 1000),
                               description=faker.pystr(),
                               location=LocationEnum.SPB,
                               genre_id=created_genre.id,
                               published=True,
                               image_url=faker.url())
        Logger.info("### Steps 2. Create movie")
        created_movie = movie_service.post_movie(movie)

        assert created_movie.genre.name == genre.name, (f"Wrong genre name. Actual: '{created_movie.genre.name}', "
                                                        f"but expected: '{genre.name}'")
