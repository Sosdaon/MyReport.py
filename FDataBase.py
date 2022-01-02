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

    def addPost(self, passport_number, title, text, institution_name, department_name, definition, typological,
                object_owner, author, clarified_author, object_title, clarified_object_title, time_of_creation,
                clarified_time_of_creation, material, clarified_material, technique, clarified_technique, object_size,
                clarified_size, weight, clarified_weight, reason, object_input_date, execute_restorer,
                object_output_date,
                responsible_restorer, origin_description, appearance_description, damages_description,
                signs_description,
                size_description):
        try:
            tm = math.floor(time.time())
            self.__cur.execute(
                'INSERT INTO posts VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                (passport_number,
                 title, text, institution_name, department_name, definition, typological, object_owner, author,
                 clarified_author, object_title,
                 clarified_object_title, time_of_creation, clarified_time_of_creation, material, clarified_material,
                 technique, clarified_technique, object_size,
                 clarified_size, weight, clarified_weight, reason, object_input_date, execute_restorer,
                 object_output_date, responsible_restorer, origin_description,
                 appearance_description, damages_description, signs_description, size_description, tm))
            self.__db.commit()
        except sqlite3.Error as e:
            print('Помилка додавання статті в базу даних' + str(e))
            return False

        return True

    def getPost(self, postId):
        try:
            self.__cur.execute(f'SELECT passport_number, title, text, institution_name, department_name, definition, '
                               f'typological, object_owner, author, clarified_author, object_title, clarified_object_title,'
                               f'time_of_creation, clarified_time_of_creation, material, clarified_material,'
                               f'technique, clarified_technique, object_size, clarified_size, weight, clarified_weight,'
                               f'reason, object_input_date, execute_restorer, object_output_date, responsible_restorer,'
                               f'origin_description, appearance_description, damages_description, signs_description,'
                               f'size_description FROM posts WHERE id = {postId} LIMIT 1')
            res = self.__cur.fetchone()
            if res:
                return res
        except sqlite3.Error as e:
            print('Помилка отримання статті з бази даних' + str(e))

        return (False, False)

    def getPostsAnonce(self):
        try:
            self.__cur.execute(f'SELECT id, title, text FROM posts ORDER BY time DESC')
            res = self.__cur.fetchall()
            if res:
                return res
        except sqlite3.Error as e:
            print('Помилка отримання статті з бази даних' + str(e))

        return []
