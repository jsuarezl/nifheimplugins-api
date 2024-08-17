from typing import Type
from sqlalchemy.orm import Session
from app.database import models
from app.database.models import Repository


def get_repository(db: Session, repository_id: int) -> models.Repository:
    return db.query(models.Repository).filter(models.Repository.id == repository_id).first()


def get_repositories(db: Session) -> list[Type[Repository]]:
    return db.query(models.Repository).all()


def get_repository_by_name(db: Session, name: str) -> models.Repository:
    return db.query(models.Repository).filter(models.Repository.name == name).first()


def create_repository(db: Session, repository: models.Repository) -> models.Repository:
    db.add(repository)
    db.commit()
    db.refresh(repository)
    return repository


def delete_repository(db: Session, repository: models.Repository):
    db.delete(repository)
    db.commit()


def update_repository(db: Session, repository: models.Repository):
    db.refresh(repository)
    return repository
