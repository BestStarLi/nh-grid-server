from fastapi import APIRouter
from . import patch, topo

router = APIRouter(prefix='/patch', tags=['patch-related apis'])

router.include_router(patch.router)
router.include_router(topo.router)