from typing import List
from fastapi import FastAPI, HTTPException, Depends
from database import postgres_connection
from schema import UserGet, PostGet, FeedGet
from helpers import get_user, get_post, get_feed, get_recommended_feed

# Инициализация FastAPI-приложения — точка входа для всех маршрутов
app = FastAPI()


# Функция для создания и закрытия подключения к базе данных.
# Используется в Depends — FastAPI сам управляет подключением и закрытием.
def get_conn():
    """
    Создаёт и возвращает подключение к PostgreSQL через psycopg2.

    Подключение автоматически закрывается после выполнения запроса.
    Используется как зависимость FastAPI.
    """
    conn = postgres_connection()
    try:
        yield conn  # отдаём соединение в обработчик запроса
    finally:
        conn.close()  # обязательно закрываем соединение после завершения


@app.get("/user/{id}", response_model=UserGet)
def handle_get_user(id: int, conn=Depends(get_conn)) -> UserGet:
    """
    Получить информацию о пользователе по ID.

    Параметры:
        id (int): Уникальный идентификатор пользователя.

    Возвращает:
        UserGet: Данные пользователя в формате, пригодном для API.

    Исключения:
        HTTPException 404 — если пользователь с заданным ID не найден.
    """
    # TODO: Получить объект пользователя из БД с помощью функции get_user(conn, id)
    user = get_user(conn, user_id=id)
    # TODO: Если пользователь не найден — выбросить HTTPException(404)
    if user is None:
            raise HTTPException(404)
    # TODO: Вернуть объект класса User
    return user


@app.get("/post/{id}", response_model=PostGet)
def handle_get_post(id: int, conn=Depends(get_conn)) -> PostGet:
    """
    Получить информацию о посте по его ID.

    Параметры:
        id (int): Уникальный идентификатор поста.

    Возвращает:
        PostGet: Информация о посте (текст и тема).

    Исключения:
        HTTPException 404 — если пост с заданным ID не найден.
    """
    # TODO: Получить пост из БД с помощью get_post(conn, id)
    post = get_post(conn, post_id=id)
    # TODO: Если пост не найден — выбросить HTTPException(404)
    if post is None:
                raise HTTPException(404)
    # TODO: Вернуть объект класса Post
    return post


@app.get("/user/{id}/feed", response_model=List[FeedGet])
def handle_get_user_feed(
    id: int, limit: int = 10, conn=Depends(get_conn)
) -> List[FeedGet]:
    """
    Получить список действий пользователя (лайки, просмотры) по его ID.

    Параметры:
        id (int): Идентификатор пользователя.
        limit (int): Максимальное количество действий в ответе (по умолчанию 10).

    Возвращает:
        List[FeedGet]: Список действий, отсортированных от новых к старым.
    """
    # TODO: Получить список действий из БД с помощью get_feed(conn, user_id=id, limit=limit)
    feed_by_user = get_feed(conn, user_id=id, limit=limit)
    # TODO: Вернуть полученный список объектов класса Feed
    return feed_by_user


@app.get("/post/{id}/feed", response_model=List[FeedGet])
def handle_get_post_feed(
    id: int, limit: int = 10, conn=Depends(get_conn)
) -> List[FeedGet]:
    """
    Получить список действий пользователей с заданным постом.

    Параметры:
        id (int): Идентификатор поста.
        limit (int): Максимальное количество действий (по умолчанию 10).

    Возвращает:
        List[FeedGet]: Список действий пользователей с этим постом,
        отсортированный от новых к старым.
    """
    # TODO: Получить действия с постом через get_feed(conn, post_id=id, limit=limit)
    feed_by_post = get_feed(conn, post_id=id, limit=limit)
    # TODO: Вернуть полученный список объектов класса Feed
    return feed_by_post


@app.get("/post/recommendations/", response_model=List[PostGet])
def recommended_posts(
    id: int, limit: int = 10, conn=Depends(get_conn)
) -> List[PostGet]:
    """
    Получить рекомендованные посты (baseline-версия).

    Возвращает топ-N популярных постов по количеству лайков.
    Это базовая версия рекомендательной системы, одинаковая для всех пользователей.

    Параметры:
        id (int): ID пользователя (пока не используется, зарезервирован для будущей персонализации).
        limit (int): Количество постов в выдаче (по умолчанию 10).

    Возвращает:
        List[PostGet]: Список популярных постов, отсортированных по убыванию лайков.
    """
    # TODO: Получить список популярных постов с помощью get_recommended_feed(conn, id, limit)
    top_k = get_recommended_feed(conn, id, limit)
    # TODO: Вернуть полученный список объектов класса Post
    return top_k
