from database import postgres_connection

from typing import List, Optional
from psycopg2.extensions import connection
from psycopg2.extras import DictCursor

from models import User, Post, Feed

conn = postgres_connection()

def get_user(conn: connection, user_id: int) -> Optional[User]:
    """
    Загружает одного пользователя из базы данных по его Id.

    Возвращает объект User, если пользователь найден.
    Если пользователь с таким id отсутствует — возвращает None.
    """
    # TODO: Написать SQL-запрос для получения пользователя по user_id
    query = 'SELECT * FROM public."user" WHERE id = %s'

    with conn.cursor(cursor_factory=DictCursor) as cur:
        cur.execute(query, (user_id,))
        row = cur.fetchone()

        if row is None:
            return None
        # TODO: Преобразовать результат в объект User, если строка найдена

        return User(**row)


def get_post(conn: connection, post_id: int) -> Optional[Post]:
    """
    Загружает один пост из базы данных по его Id.

    Возвращает объект Post, если пост найден.
    Если пост с таким id отсутствует — возвращает None.
    """
    # TODO: Написать SQL-запрос для получения поста по post_id
    query = 'SELECT * FROM public.post WHERE id = %s'

    with conn.cursor(cursor_factory=DictCursor) as cur:
        cur.execute(query, (post_id,))
        row = cur.fetchone()

        if row is None:
            return None
        
        # TODO: Преобразовать результат в объект Post, если строка найдена
        return Post(**row)


def get_feed(
    conn: connection, user_id: int = None, post_id: int = None, limit: int = 10
) -> List[Feed]:
    """
    Получает список действий пользователей с постами, включая данные о пользователях и постах.

    - Необходимо указать хотя бы один фильтр: user_id или post_id.
    - Возвращает не более `limit` записей.
    - Действия сортируются по времени: от самых свежих к более старым.
    - Используется для получения последних активностей пользователя или взаимодействий с постом.
    """
    if user_id is None and post_id is None:
        raise ValueError("Необходимо указать хотя бы user_id или post_id")

    # TODO: Написать SQL-запрос:
    # - выбрать данные из feed_action
    # - JOIN с user и post
    # - фильтрация по user_id / post_id (если заданы)
    # - сортировка по времени (DESC)
    # - ограничение по LIMIT

    query = '''
        SELECT f.*, u.*, p.text, p.topic
        FROM public.feed_action AS f
        JOIN public."user" AS u ON f.user_id = u.id
        JOIN public.post AS p ON f.post_id = p.id
    '''

    if user_id is not None:
        query += " WHERE f.user_id = %s ORDER BY f.time DESC LIMIT %s"
        params = (user_id, limit)
    elif post_id is not None:
        query += " WHERE f.post_id = %s ORDER BY f.time DESC LIMIT %s"
        params = (post_id, limit)

    result = []
    with conn.cursor(cursor_factory=DictCursor) as cur:
        # TODO: Выполнить запрос, получить строки
        cur.execute(query, params)
        rows = cur.fetchall()
        # TODO: Для каждой строки:

        # TODO: Создать объект User из строки
        for row in rows:
            user = User(
                id=row["user_id"],
                gender=row["gender"],
                age=row["age"],
                country=row["country"],
                city=row["city"],
                exp_group=row["exp_group"],
                os=row["os"],
                source=row["source"]
            )

        # TODO: Создать объект Post из строки
            post = Post(
                id=row["post_id"],
                text=row["text"],
                topic=row["topic"]
            )

        # TODO: Создать объект Feed и добавить в список result
            feed = Feed(
                user_id=row["user_id"],
                post_id=row["post_id"],
                user=user,
                post=post,
                action=row["action"],
                time=row["time"]
            )
            result.append(feed)

    return result

def get_recommended_feed(conn: connection, id: int, limit: int) -> List[Post]:
    """
    Возвращает список top-N постов с наибольшим числом лайков.

    Это базовая реализация рекомендательной системы (baseline),
    которая не учитывает индивидуальные предпочтения, а показывает
    одинаковые популярные посты всем пользователям.

    Параметры:
        conn (connection): подключение к базе данных.
        id (int): ID пользователя (в этой версии не используется,
                  но оставлен для совместимости с будущей логикой).
        limit (int): количество постов в выдаче.

    Возвращает:
        List[Post]: список объектов Post, отсортированных по убыванию популярности.
    """
    # TODO: Написать SQL-запрос для выбора top-N постов с наибольшим числом лайков
    query = '''
        SELECT 
            p.id, 
            p.text,
            p.topic
        FROM public.feed_action AS f
        JOIN public.post AS p ON f.post_id = p.id
        WHERE action = 'like'
        GROUP BY p.id
        ORDER BY COUNT(*) DESC
        LIMIT %s
    '''

    with conn.cursor(cursor_factory=DictCursor) as cur:
        cur.execute(query, (limit,))
        rows = cur.fetchall()
        result = []
        for row in rows:
            post = Post(**row)
            result.append(post)

        return result
