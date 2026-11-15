from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class User:
    """
    Класс для представления пользователя.

    Атрибуты:
        id (int): Уникальный идентификатор пользователя.
        gender (int): Пол пользователя. (0 — мужчина, 1 — женщина).
        age (int): Возраст пользователя.
        country (str): Страна проживания пользователя.
        city (str): Город проживания пользователя.
        exp_group (int): Экспериментальная группа
        os (str): Операционная система устройства
        source (str): Источник трафика
    """
    # TODO: Перечислите все поля с их типами, например:
    # id: int
    # gender: int
    id: int
    gender: int
    age: int
    country: str
    city: str
    exp_group: int
    os: str
    source: str


@dataclass
class Post:
    """
    Класс для представления поста (контента).

    Атрибуты:
        id (int): Уникальный идентификатор поста.
        text (str): Текст поста.
        topic (Optional[str], по умолчанию None): Тематика поста.
            Может быть None, если тема не задана.
    """
    #TODO: укажите все поля Post
    # topic по умолчанию равен None (используйте тип Optional)
    id: int
    text: str
    topic: Optional[str] = None


@dataclass
class Feed:
    """
    Класс для представления действия пользователя с постом.

    Атрибуты:
        user_id (int): Идентификатор пользователя, совершившего действие.
        post_id (int): Идентификатор поста, с которым было совершено действие.
        user (User): Объект пользователя, совершившего действие.
        post (Post): Объект поста, с которым было совершено действие.
        action (str): Тип действия ('like', 'view').
        time (datetime): Время совершения действия.
    """
    # TODO: перечислите поля Feed
    # Кроме ссылок user_id, post_id, мы также будет хранить объекты user и post
    user_id: int
    post_id: int
    user: User
    post: Post
    action: str
    time: datetime