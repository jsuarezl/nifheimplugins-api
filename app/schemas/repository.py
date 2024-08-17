from pydantic import BaseModel


class RepositoryBase(BaseModel):
    name: str
    url: str
    version: str


class RepositoryCreate(RepositoryBase):
    pass


class Repository(RepositoryBase):
    id: int

    class Config:
        orm_mode = True
