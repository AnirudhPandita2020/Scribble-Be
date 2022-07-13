"""
Game route
"""

from fastapi import APIRouter, HTTPException, status, Depends
from app.schemas import *
from app.models import *

router = APIRouter(
    prefix="/game",
    tags=["Game"]
)


@router.get("")
def game_start():
    return "Construction"
