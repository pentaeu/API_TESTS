from pydantic import BaseModel, ConfigDict


class GenreResponse(BaseModel):
    model_config = ConfigDict(extra="forbid",
                              populate_by_name=True)

    id: int
    name: str
