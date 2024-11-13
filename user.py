from fastapi import APIRouter
from fastapi import FastAPI, Path, status, Body, HTTPException, Request
from fastapi.responses import HTMLResponse
from typing import Annotated, List
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates

router = APIRouter(prefix='/user', tags=['user'])

@router.get('/')
async def all_users():
    pass


@router.get('/user_id')
async def user_by_id():
    pass


@router.post('/create')
async def create_user():
    pass


@router.put('/update')
async def update_user():
    pass


@router.delete('/delete')
async def delete_user():
    pass