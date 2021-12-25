import math
import sqlite3
import time


class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def getMenu(self):
        sql = '''SELECT * FROM mainmenu'''
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res: return res
        except:
            print('Помилка читання з бази даних')
        return []

    def addPost(self, title, text):
        try:
            tm = math.floor(time.time())
            self.__cur.execute('INSERT INTO posts VALUES(NULL, ?, ?, ?)',(title, text, tm))
            self.__db.commit()
        except sqlite3.Error as e:
            print('Помилка додавання статті в базу даних' + str(e))
            return False

        return True

    def getPost(self, postId):
        try:
            self.__cur.execute(f'SELECT title, text FROM posts WHERE id = {postId} LIMIT 1')
            res = self.__cur.fetchone()
            if res:
                return res
        except sqlite3.Error as e:
            print('Помилка отримання статті з бази даних' + str(e))

        return (False, False)