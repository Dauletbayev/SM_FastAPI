from fastapi import APIRouter, Request, Body, UploadFile
from pydantic import BaseModel
from urllib import request
from typing import List, Dict
from database.postservice import *
import re

posts_router = APIRouter(prefix='/posts', tags=['Управление постами'])

@posts_router.post('/api/add_post')
async def add_post(user_id: int, main_text: str, hashtag: str = None):
    new_post = public_post_db(user_id, main_text, hashtag)
    if new_post:
        return {'status': 1, 'message': 'Пост успешно создан'}
    return {'status': 0, 'message': 'Не удалось создать пост'}

@posts_router.get('/api/posts')
async def get_all_or_exact_post(post_id=0):
    post = get_all_or_exact_post_db(post_id)
    if post:
        return {'status': 1, 'message': post}
    return {'status': 0, 'message': 'Пост не найден'}

@posts_router.put('/api/change_post')
async def change_post_text(post_id: int, text: str):
    if post_id and text:
        change_post_text_db(post_id, text)
        return {'status': 1, 'message': 'Пост успешно изменен'}
    return {'status': 0, 'message': 'Ошибка'}

@posts_router.delete('/api/delete_post')
async def delete_post(post_id: int):
    try:
        delete_post_db(post_id)
        return {'status': 1, 'message': 'Пост успешно удален'}
    except:
        return {'status': 0, 'message': 'Ошибка'}







