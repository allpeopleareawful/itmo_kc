from database import postgres_connection
from helpers import get_user, get_post, get_feed, get_recommended_feed

conn = postgres_connection()

print("Загружаем пользователя с id=200")
user = get_user(conn, user_id=200)
print("Результат:", user, end="\n\n")

print("Загружаем пост с id=3")
post = get_post(conn, post_id=3)
print("Результат:", post, end="\n\n")

print("Загружаем 3 последних действия пользователя с id=200")
feed = get_feed(conn, user_id=200, limit=3)
print(f"Результат: {feed}")
print()

print("Загружаем топ-3 рекомендованных поста")
recommended = get_recommended_feed(conn, id=0, limit=3)
print(f"Результат: {recommended}")