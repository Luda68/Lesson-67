from pydantic import BaseModel
from fastapi import FastAPI, Path, status, Body, HTTPException, Request
from fastapi.responses import HTMLResponse
from typing import Annotated, List
from fastapi.templating import Jinja2Templates


class CreateUser(BaseModel):
    username: str
    firstname: str
    lastname: str
    age: int


class UpdateUser(BaseModel):
    firstname: str
    lastname: str
    age: int


class CreateTask(BaseModel):
    title: str
    content: str
    priority: int


class UpdateTask(BaseModel):
    title: str
    content: str
    priority: int