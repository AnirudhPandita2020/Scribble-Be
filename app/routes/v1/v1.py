"""
Version 1 of Scribble
"""

from fastapi import APIRouter
from app.routes.v1 import game, player

router = APIRouter(
    prefix="/api/v1",
)
router.include_router(game.router)
router.include_router(player.router)
