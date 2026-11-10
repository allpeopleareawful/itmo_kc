from  fastapi import FastAPI, HTTPException, Depends
import datetime
from pydantic import BaseModel
from loguru import logger
import psycopg2
from psycopg2.extras import RealDictCursor

app = FastAPI()

# @app.get('/')
# def hello_world():
#     return 'hello, world'

@app.get('/')
def sum_of_two(a: int, b:int) -> int:
    return a + b

@app.get('/sum_date')
def sum_date(current_date: datetime.date, offset: int) -> datetime.date:
    return current_date + datetime.timedelta(days=offset)

class User(BaseModel):
    name: str
    surname: str
    age: int
    registration_date: datetime.date
    class Config:
         orm_mode = True

@app.post('/user/validate')
def validate_user(user: User):
    logger.info(f"Валидация пользователя: {user}")
    return f'Will add user: {user.name} {user.surname} with age {user.age}'

# @app.get('/user/{id}')
# def get_user(id: int):
#      conn = psycopg2.connect(
#         "***REMOVED***",
#         cursor_factory=RealDictCursor
#     )

#      cursor = conn.cursor()

#      cursor.execute(f"""
#           SELECT gender, age, city
#           FROM "user"
#           WHERE id = {id}
#      """)
    
#      result = cursor.fetchone()
#      cursor.close()
#      conn.close()

#      if not result:
#          raise HTTPException(status_code=404, detail="user not found")
     
#      logger.info(result)
#      return result

def get_db():
     conn = psycopg2.connect(
             "***REMOVED***",
             cursor_factory=RealDictCursor
         )
     

     return conn

# @app.get('/user/{id}')
# def get_user(id: int, db = Depends(get_db)):
#      with db.cursor() as cursor:
#           cursor.execute(f'''
#           SELECT gender, age, city
#           FROM "user"
#           WHERE id = {id}
#           ''')

#           result = cursor.fetchone()

#           if not result:
#                raise HTTPException(status_code=404, detail="user not found")

#           return result

class PostResponse(BaseModel):
    id: int
    text: str
    topic: str
    class Config:
         orm_mode = True


@app.get('/post/{id}')
def get_post(id: int, db=Depends(get_db)) -> PostResponse:
    with db.cursor() as cursor:
        cursor.execute(
          f'''
          SELECT id, text, topic
          FROM post
          WHERE id = {id}
          '''
        )
        result = cursor.fetchone()
        
        if not result:
            raise HTTPException(status_code=404, detail="post not found")
        
    return PostResponse(**result)