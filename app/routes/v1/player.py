"""
Player route
"""

from fastapi import APIRouter, HTTPException, status

router = APIRouter(
    prefix="/player",
    tags=["Player"]
)


@router.get("")
def game_start():
    return "Construction"
