from fastapi import APIRouter, Request, HTTPException, status, Depends
from sqlalchemy.orm import Session
from app.database import get_db

from app import schemas, github_client
import logging

router = APIRouter(prefix='/repo', tags=['repositories'],
                   responses={404: {'description': 'not found'}})

repos = ['coins']


# TODO: use response models
@router.get("/{name}")
async def get_data_for_repo(name: str, request: Request, db: Session = Depends(get_db)):
    name = name.lower().strip()
    logger = logging.getLogger(__name__)
    if name not in repos:
        logger.info(request.client)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'unknown repository: {name}')
    version = await get_latest_version('jsuarezl', name)
    if version is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f'version could not be found for: {name}')
    return {'plugin': name, 'version': version}


async def get_latest_version(name: str, repository: str):
    versions = await github_client.fetch_repository_tags(name, repository)
    # compare different tag names
    latest_version = None
    for version in filter(lambda release: not 'BETA' in release, versions):
        version = version.lstrip('v')
        if latest_version is None:
            latest_version = version
            continue
        major, minor, patch = version.split('.')
        latest_major, latest_minor, latest_patch = latest_version.split('.')
        if int(major) > int(latest_major) and int(minor) > int(latest_minor) and int(patch) > int(latest_patch):
            latest_version = version
    return latest_version
