import math
import sqlite3
import time
import re


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

    def convertToBinary(self, image):
        self.blobData = image.read()
        return self.blobData

    def addPost(self, passport_number, title, text, institution_name, department_name, definition, typological,
                object_owner, author, clarified_author, object_title, clarified_object_title, time_of_creation,
                clarified_time_of_creation, material, clarified_material, technique, clarified_technique, object_size,
                clarified_size, weight, clarified_weight, reason, object_input_date, execute_restorer,
                object_output_date,
                responsible_restorer, origin_description, appearance_description, damages_description,
                signs_description,
                size_description, purposes_researches, methods_researches, executor_date_researches, results_researches,
                restoration_program, treatments_descriptions, treatments_chemicals, treatments_executor_date,
                treatments_results, image_of_object, image_description):
        try:
            reason = re.sub(r'\n', '<br>', reason)
            origin_description = re.sub(r'\n', '<br>', origin_description)
            appearance_description = re.sub(r'\n', '<br>', appearance_description)
            damages_description = re.sub(r'\n', '<br>', damages_description)
            signs_description = re.sub(r'\n', '<br>', signs_description)
            size_description = re.sub(r'\n', '<br>', size_description)
            purposes_researches = re.sub(r'\n', '<br>', purposes_researches)
            methods_researches = re.sub(r'\n', '<br>', methods_researches)
            executor_date_researches = re.sub(r'\n', '<br>', executor_date_researches)
            results_researches = re.sub(r'\n', '<br>', results_researches)
            restoration_program = re.sub(r'\n', '<br>', restoration_program)
            treatments_descriptions = re.sub(r'\n', '<br>', treatments_descriptions)
            treatments_chemicals = re.sub(r'\n', '<br>', treatments_chemicals)
            treatments_executor_date = re.sub(r'\n', '<br>', treatments_executor_date)
            treatments_results = re.sub(r'\n', '<br>', treatments_results)

            binary_image = self.convertToBinary(image_of_object)

            tm = math.floor(time.time())
            self.__cur.execute(
                'INSERT INTO posts VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                (passport_number,
                 title, text, institution_name, department_name, definition, typological, object_owner, author,
                 clarified_author, object_title,
                 clarified_object_title, time_of_creation, clarified_time_of_creation, material, clarified_material,
                 technique, clarified_technique, object_size,
                 clarified_size, weight, clarified_weight, reason, object_input_date, execute_restorer,
                 object_output_date, responsible_restorer, origin_description,
                 appearance_description, damages_description, signs_description, size_description, purposes_researches,
                 methods_researches, executor_date_researches, results_researches, restoration_program,
                 treatments_descriptions, treatments_chemicals, treatments_executor_date, treatments_results,
                 binary_image, image_description, tm))
            self.__db.commit()
        except sqlite3.Error as e:
            print('Помилка додавання публікації в базу даних' + str(e))
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
                               f'size_description, purposes_researches, methods_researches, executor_date_researches,'
                               f' results_researches, restoration_program, treatments_descriptions,'
                               f' treatments_chemicals, treatments_executor_date,'
                               f' treatments_results FROM posts WHERE id = {postId} LIMIT 1')
            res = self.__cur.fetchone()
            if res:
                return res
        except sqlite3.Error as e:
            print('Помилка отримання публікації з бази даних' + str(e))

        return (False, False)

    def getPostsAnonce(self):
        try:
            self.__cur.execute(f'SELECT id, title, text FROM posts ORDER BY time DESC')
            res = self.__cur.fetchall()
            if res:
                return res
        except sqlite3.Error as e:
            print('Помилка отримання публікації з бази даних' + str(e))

        return []
