from datetime import datetime
from pydantic import BaseModel


class UserGet(BaseModel):
    """
    Модель данных пользователя для API-ответов.

    Атрибуты:
    - id: уникальный идентификатор пользователя.
    - gender: пол пользователя, представлен числом
    - age: возраст пользователя.
    - country: страна проживания.
    - city: город проживания.
    - exp_group: группа эксперимента, к которой относится пользователь.
    - os: операционная система устройства пользователя
    - source: источник регистрации или привлечения пользователя.
    """

    # TODO: Определить все поля с нужными типами данных
    id: int
    gender: int
    age: int
    country: str
    city: str
    exp_group: int
    os: str
    source: str


class PostGet(BaseModel):
    """
    Модель данных поста для API-ответов.

    Атрибуты:
    - id: уникальный идентификатор поста.
    - text: текстовое содержимое поста.
    - topic: тема или категория поста.
    """

    # TODO: Определить все поля с нужными типами данных
    id: int
    text: str
    topic: str


class FeedGet(BaseModel):
    """
    Модель данных действия пользователя с постом для API-ответов.

    Атрибуты:
    - user_id: идентификатор пользователя, который совершил действие.
    - post_id: идентификатор поста, над которым совершено действие.
    - user: вложенный объект UserGet с данными пользователя.
    - post: вложенный объект PostGet с данными поста.
    - action: тип действия
    - time: дата и время совершения действия в формате datetime.
    """

    # TODO: Определить все поля с нужными типами данных
    user_id: int
    post_id: int

    user: UserGet  # TODO: Связать с классом UserGet
    post: PostGet  # TODO: Связать с классом PostGet

    action: str
    time: datetime
