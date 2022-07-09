from pydantic import BaseModel


class CertainNews(BaseModel):
    ref: str
    datetime: str
    title: str
    type: str



