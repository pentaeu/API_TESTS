from pydantic import BaseModel, ConfigDict


class CreateGenreDto(BaseModel):
    model_config = ConfigDict(extra="forbid",
                              populate_by_name=True)

    name: str
