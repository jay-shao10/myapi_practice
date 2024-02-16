from fastapi import FastAPI ,Path
from typing import Optional
from pydantic import BaseModel
import psycopg2

app=FastAPI()
# 0. get all user data
@app.get("/get_all_user")
def get_student():
    try:
    # 連接到本地資料庫，指定帳號、密碼、主機和埠號
        connection = psycopg2.connect(user="postgres",
                                    password="root",
                                    host="localhost",
                                    port="5433",
                                    database="postgres")

        # 創建一個游標物件
        cursor = connection.cursor()

        # 執行 SQL 查詢
        cursor.execute('SELECT * FROM public."USER"')
        record = cursor.fetchall()
        print("You are connected to - ", record, "\n")
        return record

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)

    finally:
        # 關閉游標和連接
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

@app.get("/get-user-by-id/{id}")
def get_student(id):
    try:
    # 連接到本地資料庫，指定帳號、密碼、主機和埠號
        connection = psycopg2.connect(user="postgres",
                                    password="root",
                                    host="localhost",
                                    port="5433",
                                    database="postgres")

        # 創建一個游標物件
        cursor = connection.cursor()

        # 執行 SQL 查詢
        
        cursor.execute('SELECT * FROM public."USER" WHERE user_id = %s' % id)

        record = cursor.fetchall()
        print("You are connected to - ", record, "\n")
        return record

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)

    finally:
        # 關閉游標和連接
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


@app.post("/create-student/{name},{password}")
def get_student(name,password):
    try:
        connection = psycopg2.connect(user="postgres",
                                    password="root",
                                    host="localhost",
                                    port="5433",
                                    database="postgres")
        cursor = connection.cursor()
        
        cursor.execute('INSERT INTO public."USER" (user_name, password) VALUES (%s, %s)', (name, password))
        

        record = cursor.fetchall()
        print("You are connected to - ", record, "\n")
        return record

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)

    finally:
        # 關閉游標和連接
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")








            
# # 1. get user by (id)->data
# @app.get("/get-student-by-id/{student_id}")
# def get_student(student_id:int=Path(description="The ID of the student you want to view",)):
#     return students[student_id]

# # 2. add user
# @app.post("/create-student")
# def create_student(student:MathStudent):
#     students[len(students)+1]=student
#     return len(students)
# # 3. update user
# @app.put("/update_student")
# def update_student(student_id:int,testScore:int):
#     students[student_id].testscore=testScore
#     return students[student_id]

# # delete user by id