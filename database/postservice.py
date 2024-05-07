from database import get_db
from database.models import UserPost, Comment, Hashtag
from datetime import datetime

# Получение всех или одного конкретного поста
def get_all_or_exact_post_db(post_id):
    db = next(get_db())
    if post_id:
        exact_post = db.query(UserPost).filter_by(id=post_id).first()
        return exact_post
    elif post_id == 0:
        all_posts = db.query(UserPost).all()
        return [i for i in all_posts]

# Редактирование поста
def change_post_text_db(post_id, new_text):
    db = next(get_db())
    post_to_edit = db.query(UserPost).filter_by(id=post_id).first()
    if post_to_edit:
        post_to_edit.main_text = new_text
        db.commit()
        return True
    return False

# Удаление поста
def delete_post_db(post_id):
    db = next(get_db())
    post_to_delete = db.query(UserPost).filter_by(id=post_id).first()
    if post_to_delete:
        db.delete(post_to_delete)
        db.commit()
        return True
    return False

# Публикация поста
def public_post_db(user_id, main_text, hashtag=None):
    db = next(get_db())
    new_post = UserPost(user_id=user_id, main_text=main_text, post_date=datetime.now(), hashtag_name=hashtag)
    db.add(new_post)
    db.commit()
    return True

# Добавление комментария
def public_comment_db(user_id, post_id, text):
    db = next(get_db())
    new_comment = Comment(user_id=user_id, post_id=post_id, text=text, comment_date=datetime.now())
    db.add(new_comment)
    db.commit()
    return True

# Получение комментариев
def get_exact_post_comment_db(post_id):
    db = next(get_db())
    exact_comments = db.query(Comment).filter_by(post_id=post_id).all()
    return exact_comments

# Изменение текста комментария
def change_comment_text_db(comment_id, new_text):
    db = next(get_db())
    comment_to_edit = db.query(Comment).filter_by(id=comment_id).first()
    if comment_to_edit:
        comment_to_edit.text = new_text
        db.commit()
        return True
    return False

# Удаление комментария
def delete_exact_comment_db(comment_id):
    db = next(get_db())
    comment_to_delete = db.query(Comment).filter_by(id=comment_id).first()
    if comment_to_delete:
        db.delete(comment_to_delete)
        db.commit()
        return True
    return False

# Создание хэштэга
def add_hashtag(name):
    db = next(get_db())
    new_hashtag = Hashtag(hashtag_name=name, hashtag_date=datetime.now())
    db.add(new_hashtag)
    db.commit()
    return True

# Получение определенного хэштега
def get_exact_hashtag_db(hashtag_name):
    db = next(get_db())
    exact_hashtag = db.query(UserPost).filter_by(hashtag_name=hashtag_name).all()
    return exact_hashtag

# Получение рекомендаций по хэштегам
def get_some_hashtag_db(size, hashtag_name):
    db = next(get_db())
    posts = db.query(UserPost).filter_by(hashtag_name=hashtag_name).all()
    return posts[:size]
