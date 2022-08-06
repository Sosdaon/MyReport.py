import math
import time
import re

from flask import flash
import sqlite3


class DataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def get_main_menu(self):
        sql = '''SELECT * FROM main_menu'''
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res:
                return res
        except:
            print('Нажаль виникла помилка читання елементів меню з бази даних')
            flash('Нажаль виникла помилка і елементи меню не відображаються', category='error')
        return []

    def store_passport(self, passport_number, inventory_number, acceptance_number, institution_name, department_name,
                       definition, typological, object_owner, author, clarified_author, object_name,
                       clarified_object_name, time_of_creation, clarified_time_of_creation, material,
                       clarified_material, technique, clarified_technique, object_size, clarified_size, weight,
                       clarified_weight, reason, object_input_date, execute_restorer, object_output_date,
                       responsible_restorer, origin_description, appearance_description, damages_description,
                       signs_description, size_description, purposes_researches, methods_researches,
                       executor_date_researches, results_researches, restoration_program, treatments_descriptions,
                       treatments_chemicals, treatments_executor_date, treatments_results, current_restorer_id):
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
                'INSERT INTO passports VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                (passport_number, inventory_number, acceptance_number, institution_name, department_name, definition,
                 typological, object_owner, author, clarified_author, object_name, clarified_object_name,
                 time_of_creation, clarified_time_of_creation, material, clarified_material, technique,
                 clarified_technique, object_size, clarified_size, weight, clarified_weight, reason, object_input_date,
                 execute_restorer, object_output_date, responsible_restorer, origin_description,
                 appearance_description, damages_description, signs_description, size_description, purposes_researches,
                 methods_researches, executor_date_researches, results_researches, restoration_program,
                 treatments_descriptions, treatments_chemicals, treatments_executor_date, treatments_results,
                 current_restorer_id, tm))
            self.__db.commit()
        except sqlite3.Error as e:
            print('Нажаль виникла помилка додавання паспорта в базу даних' + str(e))
            flash('Нажаль виникла помилка збереження паспорта', category='error')
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
            print('Нажаль виникла помилка отримання паспорта з бази даних' + str(e))
            flash('Нажаль виникла помилка отримання паспорта з бази даних', category='error')

        return (False, False)

    def get_passports_preview(self, author_of_passport_id):
        try:
            self.__cur.execute(f'SELECT id, inventory_number, object_name FROM passports WHERE author_of_passport_id == {author_of_passport_id} ORDER BY time DESC')
            passports_preview = self.__cur.fetchall()
            if passports_preview:
                return passports_preview
        except sqlite3.Error as e:
            print('Нажаль виникла помилка отримання паспортів з бази даних для портфоліо' + str(e))
            flash('Нажаль виникла помилка відображення портфоліо', category='error')

        return []

    def get_current_passport(self, id_post):
        try:
            self.__cur.execute(f'SELECT id, inventory_number, object_name FROM passports WHERE id == {id_post}')
            passport_id = self.__cur.fetchone()
            if passport_id:
                return passport_id
        except sqlite3.Error as e:
            print('Нажаль виникла помилка отримання поточного паспорта з бази даних при редагуванні' + str(e))
            flash('Нажаль виникла помилка отримання поточного паспорта з бази даних при редагуванні', category='error')

        return []

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
            print('Нажаль виникла помилка отримання публікації з бази даних при редагуванні' + str(e))
            flash('Нажаль виникла помилка отримання публікації з бази даних при редагуванні', category='error')

    def delete_passport(self, id_post):
        try:
            self.__cur.execute(f'DELETE FROM passports WHERE id == {id_post}')
            self.__db.commit()
        except sqlite3.Error as error:
            print('Нажаль виникла помилка видалення паспорта з бази даних' + str(error))
            flash('Нажаль виникла помилка видалення паспорта', category='error')
            return True

        return False

    def add_restorer(self, restorer_name, restorer_email, hashed_restorer_password):
        try:
            self.__cur.execute(f"SELECT COUNT() as 'count' FROM restorers WHERE restorer_name LIKE '{restorer_name}'")
            existed_restorer_name = self.__cur.fetchone()
            if existed_restorer_name['count'] > 0:
                flash("Користувач з таким ім'ям вже має кабінет", category='error')
                return False
            self.__cur.execute(f"SELECT COUNT() as 'count' FROM restorers WHERE restorer_email LIKE '{restorer_email}'")
            existed_restorer_email = self.__cur.fetchone()
            if existed_restorer_email['count'] > 0:
                flash("Користувач з такою електронною адресою вже має кабінет", category='error')
                return False
            else:
                tm = math.floor(time.time())
                self.__cur.execute('INSERT INTO restorers VALUES(NULL, ?, ?, ?, ?)', (restorer_name, restorer_email, hashed_restorer_password, tm))
                self.__db.commit()
        except sqlite3.Error as e:
            print('Нажаль виникла помилка додавання користувача в базу даних' + str(e))
            flash('Нажаль виникла помилка додавання користувача в базу даних', category='error')
            return False

        return True

    def get_restorer(self, restorer_id):
        try:
            self.__cur.execute(f"SELECT * FROM restorers WHERE id = {restorer_id} LIMIT 1")
            result = self.__cur.fetchone()
            if not result:
                print('Нажаль користувача за таким ай ді не знайдено')
                flash('Нажаль користувача не знайдено', category='error')
                return False

            return result
        except sqlite3.Error as e:
            print('Нажаль виникла помилка отримання даних про реставратора з бази даних за таким ай ді' + str(e))
            flash('Нажаль виникла помилка отримання даних про реставратора з бази даних', category='error')

        return False

    def get_restorer_by_email(self, restorer_email):
        try:
            self.__cur.execute(f"SELECT * FROM restorers WHERE restorer_email = '{restorer_email}' LIMIT 1")
            result = self.__cur.fetchone()
            if not result:
                print('Нажаль користувача за такою електронною адресою не знайдено')
                flash('Нажаль користувача за такою електронною адресою не знайдено', category='error')
                return False

            return result
        except sqlite3.Error as e:
            print('Нажаль виникла помилка отримання електронної адреси з бази даних' + str(e))
            flash('Нажаль виникла помилка отримання електронної адреси реставратора з бази даних', category='error')

        return False

    def store_experience(self, experienced_material, experienced_description, experienced_damages_description, experienced_research_title, experienced_research_description, experienced_restoration_program, experienced_treatments_descriptions, experienced_treatments_chemicals,
                         author_of_experience_id):
        try:
            tm = math.floor(time.time())
            self.__cur.execute('INSERT INTO experience VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (experienced_material, experienced_description, experienced_damages_description, experienced_research_title, experienced_research_description, experienced_restoration_program, experienced_treatments_descriptions, experienced_treatments_chemicals, author_of_experience_id, tm))
            self.__db.commit()
        except sqlite3.Error as e:
            print('Нажаль виникла помилка додавання досвіду в базу даних' + str(e))
            flash('Нажаль виникла помилка додавання досвіду', category='error')
            return False

        return True

    def get_experiences_preview(self, author_of_experience_id):
        try:
            self.__cur.execute(f'SELECT id, experienced_material FROM experience WHERE author_of_experience_id == {author_of_experience_id} ORDER BY time DESC')
            experiences_preview = self.__cur.fetchall()
            if experiences_preview:
                return experiences_preview
            if not experiences_preview:
                return print('Нажаль у вас ще немає досвіду')
        except sqlite3.Error as e:
            print('Нажаль виникла помилка отримання вашого реставраційного досвіду з бази даних' + str(e))
            flash('Нажаль виникла помилка отримання вашого реставраційного досвіду з бази даних', category='error')

    def get_experience(self, author_of_experience_id):
        try:
            self.__cur.execute(
                f'SELECT id, experienced_material, experienced_description, experienced_damages_description, experienced_research_title, experienced_research_description, experienced_restoration_program, experienced_treatments_descriptions, experienced_treatments_chemicals FROM experience WHERE author_of_experience_id = {author_of_experience_id} LIMIT 1')
            experience_fields_output = self.__cur.fetchone()
            if experience_fields_output:
                return experience_fields_output
            if not experience_fields_output:
                empty_experience_fields_output = '', '', '', '', '', '', '', '', ''
                return empty_experience_fields_output
        except sqlite3.Error as e:
            print('Нажаль виникла помилка отримання досвіду з бази даних' + str(e))
            flash('Нажаль виникла помилка отримання досвіду з бази даних', category='error')

    def get_experience_to_show(self, id_post):
        try:
            self.__cur.execute(
                f'SELECT experienced_material, experienced_description, experienced_damages_description, experienced_research_title, experienced_research_description, experienced_restoration_program, experienced_treatments_descriptions, experienced_treatments_chemicals FROM experience WHERE id = {id_post} LIMIT 1')
            experience_fields_output = self.__cur.fetchone()
            if experience_fields_output:
                return experience_fields_output
            if not experience_fields_output:
                empty_experience_fields_output = '', '', '', '', '', '', '', ''
                return empty_experience_fields_output
        except sqlite3.Error as e:
            print('Нажаль виникла помилка отримання досвіду з бази даних' + str(e))
            flash('Нажаль виникла помилка отримання досвіду з бази даних', category='error')
