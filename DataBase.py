import math
import sqlite3
import time
import re


class DataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def getMainMenu(self):
        sql = '''SELECT * FROM main_menu'''
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res:
                return res
        except:
            FileNotFoundError('Помилка читання з бази даних')
        return []

    def store_passport(self, passport_number, inventory_number, acceptance_number, institution_name, department_name,
                       definition, typological, object_owner, author, clarified_author, object_name,
                       clarified_object_name, time_of_creation, clarified_time_of_creation, material,
                       clarified_material, technique, clarified_technique, object_size, clarified_size, weight,
                       clarified_weight, reason, object_input_date, execute_restorer, object_output_date,
                       responsible_restorer, origin_description, appearance_description, damages_description,
                       signs_description, size_description, purposes_researches, methods_researches,
                       executor_date_researches, results_researches, restoration_program, treatments_descriptions,
                       treatments_chemicals, treatments_executor_date, treatments_results):
        try:
            # Carriage return
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

            tm = math.floor(time.time())
            self.__cur.execute(
                'INSERT INTO passports VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                (passport_number, inventory_number, acceptance_number, institution_name, department_name, definition,
                 typological, object_owner, author, clarified_author, object_name, clarified_object_name,
                 time_of_creation, clarified_time_of_creation, material, clarified_material, technique,
                 clarified_technique, object_size, clarified_size, weight, clarified_weight, reason, object_input_date,
                 execute_restorer, object_output_date, responsible_restorer, origin_description,
                 appearance_description, damages_description, signs_description, size_description, purposes_researches,
                 methods_researches, executor_date_researches, results_researches, restoration_program,
                 treatments_descriptions, treatments_chemicals, treatments_executor_date, treatments_results, tm))
            self.__db.commit()
        except sqlite3.Error as e:
            FileNotFoundError('Помилка додавання публікації в базу даних' + str(e))
            return False

        return True

    def get_passport(self, id_post):
        try:
            self.__cur.execute(
                f'SELECT passport_number, inventory_number, acceptance_number, institution_name, department_name, definition, '
                f'typological, object_owner, author, clarified_author, object_name, clarified_object_name,'
                f'time_of_creation, clarified_time_of_creation, material, clarified_material,'
                f'technique, clarified_technique, object_size, clarified_size, weight, clarified_weight,'
                f'reason, object_input_date, execute_restorer, object_output_date, responsible_restorer,'
                f'origin_description, appearance_description, damages_description, signs_description,'
                f'size_description, purposes_researches, methods_researches, executor_date_researches,'
                f' results_researches, restoration_program, treatments_descriptions,'
                f' treatments_chemicals, treatments_executor_date,'
                f' treatments_results FROM passports WHERE id = {id_post} LIMIT 1')
            passport_field_output = self.__cur.fetchone()
            if passport_field_output:
                return passport_field_output
        except sqlite3.Error as e:
            print('Помилка отримання публікації з бази даних' + str(e))

        return (False, False)

    def get_passports_preview(self):
        try:
            self.__cur.execute(f'SELECT id, inventory_number, object_name FROM passports ORDER BY time DESC')
            passports_preview = self.__cur.fetchall()
            if passports_preview:
                return passports_preview
        except sqlite3.Error as e:
            FileNotFoundError('Помилка отримання публікації з бази даних' + str(e))

        return []

    def get_current_passport(self, id_post):
        try:
            self.__cur.execute(f'SELECT id FROM passports WHERE id == {id_post}')
            passport_id = self.__cur.fetchone()
            if passport_id:
                return passport_id
        except sqlite3.Error as e:
            FileNotFoundError('Помилка отримання публікації з бази даних при редагуванні' + str(e))

        return []

    def delete_passport(self, id_post):
        try:
            self.__cur.execute(f'DELETE FROM passports WHERE id == {id_post}')
            self.__db.commit()
        except sqlite3.Error as error:
            print('Помилка отримання публікації з бази даних при редагуванні' + str(error))
            return True

        return False

    def get_passport_to_update(self, id_post):
        try:
            self.__cur.execute(
                f'SELECT passport_number, inventory_number, acceptance_number, institution_name, department_name,'
                f'definition, typological, object_owner, author, clarified_author, object_name, clarified_object_name,'
                f'time_of_creation, clarified_time_of_creation, material, clarified_material, technique,'
                f'clarified_technique, object_size, clarified_size, weight, clarified_weight, reason, object_input_date,'
                f'execute_restorer, object_output_date, responsible_restorer, origin_description, appearance_description,'
                f'damages_description, signs_description, size_description, purposes_researches, methods_researches,'
                f'executor_date_researches, results_researches, restoration_program, treatments_descriptions,'
                f' treatments_chemicals, treatments_executor_date,'
                f' treatments_results FROM passports WHERE id = {id_post} LIMIT 1')
            passport_number, inventory_number, acceptance_number, institution_name, department_name, definition, typological, object_owner, author, clarified_author, object_name, clarified_object_name, time_of_creation, clarified_time_of_creation, material, clarified_material, technique, clarified_technique, object_size, clarified_size, weight, clarified_weight, reason, object_input_date, execute_restorer, object_output_date, responsible_restorer, origin_description, appearance_description, damages_description, signs_description, size_description, purposes_researches, methods_researches, executor_date_researches, results_researches, restoration_program, treatments_descriptions, treatments_chemicals, treatments_executor_date, treatments_results = self.__cur.fetchone()

            # Get rid of tags
            reason = re.sub(r'<br>', '', reason)
            origin_description = re.sub(r'<br>', '', origin_description)
            appearance_description = re.sub(r'<br>', '', appearance_description)
            damages_description = re.sub(r'<br>', '', damages_description)
            signs_description = re.sub(r'<br>', '', signs_description)
            size_description = re.sub(r'<br>', '', size_description)
            purposes_researches = re.sub(r'<br>', '', purposes_researches)
            methods_researches = re.sub(r'<br>', '', methods_researches)
            executor_date_researches = re.sub(r'<br>', '', executor_date_researches)
            results_researches = re.sub(r'<br>', '', results_researches)
            restoration_program = re.sub(r'<br>', '', restoration_program)
            treatments_descriptions = re.sub(r'<br>', '', treatments_descriptions)
            treatments_chemicals = re.sub(r'<br>', '', treatments_chemicals)
            treatments_executor_date = re.sub(r'<br>', '', treatments_executor_date)
            treatments_results = re.sub(r'<br>', '', treatments_results)
            return passport_number, inventory_number, acceptance_number, institution_name, department_name, definition, typological, object_owner, author, clarified_author, object_name, clarified_object_name, time_of_creation, clarified_time_of_creation, material, clarified_material, technique, clarified_technique, object_size, clarified_size, weight, clarified_weight, reason, object_input_date, execute_restorer, object_output_date, responsible_restorer, origin_description, appearance_description, damages_description, signs_description, size_description, purposes_researches, methods_researches, executor_date_researches, results_researches, restoration_program, treatments_descriptions, treatments_chemicals, treatments_executor_date, treatments_results
        except sqlite3.Error as e:
            print('Помилка отримання публікації з бази даних при редагуванні' + str(e))
