import math
import time
import re

import markupsafe
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
            tm = math.floor(time.time())
            self.__cur.execute(
                f'INSERT INTO passports VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,'
                f' ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
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
                f'SELECT passport_number, inventory_number, acceptance_number, institution_name, department_name,'
                f'definition, typological, object_owner, author, clarified_author, object_name, clarified_object_name,'
                f'time_of_creation, clarified_time_of_creation, material, clarified_material, technique,'
                f'clarified_technique, object_size, clarified_size, weight, clarified_weight, reason,'
                f'object_input_date, execute_restorer, object_output_date, responsible_restorer, origin_description,'
                f'appearance_description, damages_description, signs_description, size_description,'
                f'purposes_researches, methods_researches, executor_date_researches, results_researches,'
                f'restoration_program, treatments_descriptions, treatments_chemicals, treatments_executor_date,'
                f' treatments_results FROM passports WHERE id = {id_post} LIMIT 1')
            passport = self.__cur.fetchone()
            return passport
        except sqlite3.Error as e:
            print('Нажаль виникла помилка отримання паспорта з бази даних' + str(e))
            flash('Нажаль виникла помилка отримання паспорта з бази даних', category='error')

        return (False, False)

    def get_passports_preview(self, author_of_passport_id):
        try:
            self.__cur.execute(
                f'SELECT id, inventory_number, object_name FROM passports WHERE author_of_passport_id = {author_of_passport_id} ORDER BY time DESC')
            passports_preview = self.__cur.fetchall()
            if passports_preview:
                return passports_preview
        except sqlite3.Error as e:
            print('Нажаль виникла помилка отримання паспортів з бази даних для портфоліо' + str(e))
            flash('Нажаль виникла помилка відображення портфоліо', category='error')

        return []

    def get_current_passport_id(self, id_post):
        try:
            self.__cur.execute(f'SELECT id FROM passports WHERE id = {id_post} LIMIT 1')
            passport_id = self.__cur.fetchone()
            if passport_id:
                return passport_id
        except sqlite3.Error as e:
            print('Нажаль виникла помилка отримання поточного паспорта з бази даних при редагуванні' + str(e))
            flash('Нажаль виникла помилка отримання поточного паспорта з бази даних при редагуванні', category='error')

        return []

    def get_current_passport_deletion_warning_data(self, id_post):
        try:
            self.__cur.execute(f'SELECT id, object_name, inventory_number FROM passports WHERE id = {id_post} LIMIT 1')
            passport_id = self.__cur.fetchone()
            if passport_id:
                return passport_id
        except sqlite3.Error as e:
            print('Нажаль виникла помилка отримання поточного паспорта з бази даних при редагуванні' + str(e))
            flash('Нажаль виникла помилка отримання поточного паспорта з бази даних при редагуванні', category='error')

        return []

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
                self.__cur.execute('INSERT INTO restorers VALUES(NULL, ?, ?, ?, ?)',
                                   (restorer_name, restorer_email, hashed_restorer_password, tm))
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

    def count_practices_preview(self, author_of_practice_id):
        try:
            self.__cur.execute(f'SELECT id FROM practice WHERE author_of_experience_id = {author_of_practice_id} LIMIT 1')
            practices_preview = self.__cur.fetchall()
            if practices_preview:
                return practices_preview
            if not practices_preview:
                empty_table = 'empty'
                return empty_table
        except sqlite3.Error as e:
            print('Нажаль виникла помилка отримання вашого реставраційного досвіду з бази даних' + str(e))
            flash('Нажаль виникла помилка отримання вашого реставраційного досвіду з бази даних', category='error')

    def count_practices_preview_2(self, author_of_practice_id):
        try:
            self.__cur.execute(f'SELECT id FROM practice_2 WHERE author_of_experience_id = {author_of_practice_id} LIMIT 1')
            practices_preview = self.__cur.fetchall()
            if practices_preview:
                return practices_preview
            if not practices_preview:
                empty_table = 'empty'
                return empty_table
        except sqlite3.Error as e:
            print('Нажаль виникла помилка отримання вашого реставраційного досвіду з бази даних' + str(e))
            flash('Нажаль виникла помилка отримання вашого реставраційного досвіду з бази даних', category='error')

    def count_practices_preview_3(self, author_of_experience_id):
        try:
            self.__cur.execute(
                f'SELECT id FROM practice_3 WHERE author_of_experience_id = {author_of_experience_id} LIMIT 1')
            practices_preview = self.__cur.fetchall()
            if practices_preview:
                return practices_preview
            if not practices_preview:
                empty_table = 'empty'
                return empty_table
        except sqlite3.Error as e:
            print('Нажаль виникла помилка отримання вашого реставраційного досвіду з бази даних' + str(e))
            flash('Нажаль виникла помилка отримання вашого реставраційного досвіду з бази даних', category='error')

    def get_practices_preview(self, author_of_experience_id):
        try:
            self.__cur.execute(f'SELECT id, experienced_material FROM practice WHERE author_of_experience_id = {author_of_experience_id} ORDER BY time DESC')
            practices_preview = self.__cur.fetchall()
            if practices_preview:
                return practices_preview
            if not practices_preview:
                return print('Нажаль у вас ще немає досвіду з першої практики')
        except sqlite3.Error as e:
            print('Нажаль виникла помилка отримання вашого першого реставраційного досвіду з бази даних' + str(e))
            flash('Нажаль виникла помилка отримання вашого першого реставраційного досвіду з бази даних',
                  category='error')

    def get_practices_preview_2(self, author_of_practice_id):
        try:
            self.__cur.execute(
                f'SELECT id, experienced_material_2 FROM practice_2 WHERE author_of_experience_id = {author_of_practice_id} ORDER BY time DESC')
            practices_preview_2 = self.__cur.fetchall()
            if practices_preview_2:
                return practices_preview_2
            if not practices_preview_2:
                return print('Нажаль у вас ще немає досвіду з другої практики')
        except sqlite3.Error as e:
            print('Нажаль виникла помилка отримання вашого першого реставраційного досвіду з бази даних' + str(e))
            flash('Нажаль виникла помилка отримання вашого першого реставраційного досвіду з бази даних',
                  category='error')

    def get_practices_preview_3(self, author_of_practice_id):
        try:
            self.__cur.execute(
                f'SELECT id, experienced_material_3 FROM practice_3 WHERE author_of_experience_id = {author_of_practice_id} ORDER BY time DESC')
            practices_preview_3 = self.__cur.fetchall()
            if practices_preview_3:
                return practices_preview_3
            if not practices_preview_3:
                return print('Нажаль у вас ще немає досвіду з другої практики')
        except sqlite3.Error as e:
            print('Нажаль виникла помилка отримання вашого першого реставраційного досвіду з бази даних' + str(e))
            flash('Нажаль виникла помилка отримання вашого першого реставраційного досвіду з бази даних',
                  category='error')

    def store_practice(self, experienced_material, experienced_description, experienced_damages_description, experienced_research_title, experienced_research_description, experienced_restoration_program, experienced_treatments_descriptions, experienced_treatments_chemicals, author_of_experience_id):
        try:
            tm = math.floor(time.time())
            self.__cur.execute(f'INSERT INTO practice VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                              (experienced_material, experienced_description, experienced_damages_description, experienced_research_title, experienced_research_description, experienced_restoration_program, experienced_treatments_descriptions, experienced_treatments_chemicals, author_of_experience_id, tm))
            self.__db.commit()
        except sqlite3.Error as e:
            print('Нажаль виникла помилка отримання досвіду з бази даних (Практика1)' + str(e))
            flash('Нажаль виникла помилка отримання досвіду з бази даних (Практика1)', category='error')
        return []

    def store_practice_2(self, experienced_material_2, experienced_description_2, experienced_damages_description_2, experienced_research_title_2, experienced_research_description_2, experienced_restoration_program_2, experienced_treatments_descriptions_2, experienced_treatments_chemicals_2, author_of_experience_id):
        try:
            tm = math.floor(time.time())
            self.__cur.execute(f'INSERT INTO practice_2 VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                              (experienced_material_2, experienced_description_2, experienced_damages_description_2, experienced_research_title_2, experienced_research_description_2, experienced_restoration_program_2, experienced_treatments_descriptions_2, experienced_treatments_chemicals_2, author_of_experience_id, tm))
            self.__db.commit()
        except sqlite3.Error as e:
            print('Нажаль виникла помилка отримання досвіду з бази даних (Практика2)' + str(e))
            flash('Нажаль виникла помилка отримання досвіду з бази даних (Практика2)', category='error')
        return []

    def store_practice_3(self, experienced_material_3, experienced_description_3, experienced_damages_description_3, experienced_research_title_3, experienced_research_description_3, experienced_restoration_program_3, experienced_treatments_descriptions_3, experienced_treatments_chemicals_3, author_of_experience_id):
        try:
            tm = math.floor(time.time())
            self.__cur.execute(f'INSERT INTO practice_3 VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                              (experienced_material_3, experienced_description_3, experienced_damages_description_3, experienced_research_title_3, experienced_research_description_3, experienced_restoration_program_3, experienced_treatments_descriptions_3, experienced_treatments_chemicals_3, author_of_experience_id, tm))
            self.__db.commit()
        except sqlite3.Error as e:
            print('Нажаль виникла помилка отримання досвіду з бази даних (Практика3)' + str(e))
            flash('Нажаль виникла помилка отримання досвіду з бази даних (Практика3)', category='error')
        return []

    def check_practice(self, author_of_experience_id):
        self.__cur.execute(f"SELECT experienced_material, experienced_description, experienced_damages_description, experienced_research_title, experienced_research_description, experienced_restoration_program, experienced_treatments_descriptions, experienced_treatments_chemicals FROM practice WHERE author_of_experience_id = '{author_of_experience_id}' LIMIT 1")
        practice = self.__cur.fetchone()
        if practice:
            return True
        else:
            return False

    def check_practice_2(self, author_of_experience_id):
        self.__cur.execute(f"SELECT experienced_material_2, experienced_description_2, experienced_damages_description_2, experienced_research_title_2, experienced_research_description_2, experienced_restoration_program_2, experienced_treatments_descriptions_2, experienced_treatments_chemicals_2 FROM practice_2 WHERE author_of_experience_id = '{author_of_experience_id}' LIMIT 1")
        practice_2 = self.__cur.fetchone()
        if practice_2:
            return True
        else:
            return False

    def check_practice_3(self, author_of_experience_id):
        self.__cur.execute(f"SELECT experienced_material_3, experienced_description_3, experienced_damages_description_3, experienced_research_title_3, experienced_research_description_3, experienced_restoration_program_3, experienced_treatments_descriptions_3, experienced_treatments_chemicals_3 FROM practice_3 WHERE author_of_experience_id = '{author_of_experience_id}' LIMIT 1")
        practice_3 = self.__cur.fetchone()
        if practice_3:
            return True
        else:
            return False

    def get_practice(self, author_of_experience_id):
        try:
            self.__cur.execute(f"SELECT experienced_material, experienced_description, experienced_damages_description, experienced_research_title, experienced_research_description, experienced_restoration_program, experienced_treatments_descriptions, experienced_treatments_chemicals FROM practice WHERE author_of_experience_id = '{author_of_experience_id}' LIMIT 1")
            experienced_material, experienced_description, experienced_damages_description, experienced_research_title, experienced_research_description, experienced_restoration_program, experienced_treatments_descriptions, experienced_treatments_chemicals = self.__cur.fetchone()
            return experienced_material, experienced_description, experienced_damages_description, experienced_research_title, experienced_research_description, experienced_restoration_program, experienced_treatments_descriptions, experienced_treatments_chemicals
        except sqlite3.Error as e:
            print('Нажаль виникла помилка отримання досвіду з бази даних' + str(e))
            flash('Нажаль виникла помилка отримання досвіду з бази даних', category='error')
        return []

    def get_practice_2(self, author_of_experience_id):
        try:
            self.__cur.execute(f"SELECT experienced_material_2, experienced_description_2, experienced_damages_description_2, experienced_research_title_2, experienced_research_description_2, experienced_restoration_program_2, experienced_treatments_descriptions_2, experienced_treatments_chemicals_2 FROM practice_2 WHERE author_of_experience_id = '{author_of_experience_id}' LIMIT 1")
            experienced_material_2, experienced_description_2, experienced_damages_description_2, experienced_research_title_2, experienced_research_description_2, experienced_restoration_program_2, experienced_treatments_descriptions_2, experienced_treatments_chemicals_2 = self.__cur.fetchone()
            return experienced_material_2, experienced_description_2, experienced_damages_description_2, experienced_research_title_2, experienced_research_description_2, experienced_restoration_program_2, experienced_treatments_descriptions_2, experienced_treatments_chemicals_2
        except sqlite3.Error as e:
            print('Нажаль виникла помилка отримання досвіду з бази даних' + str(e))
            flash('Нажаль виникла помилка отримання досвіду з бази даних', category='error')
        return []

    def get_practice_3(self, author_of_experience_id):
        try:
            self.__cur.execute(f"SELECT experienced_material_3, experienced_description_3, experienced_damages_description_3, experienced_research_title_3, experienced_research_description_3, experienced_restoration_program_3, experienced_treatments_descriptions_3, experienced_treatments_chemicals_3 FROM practice_3 WHERE author_of_experience_id = '{author_of_experience_id}' LIMIT 1")
            experienced_material_3, experienced_description_3, experienced_damages_description_3, experienced_research_title_3, experienced_research_description_3, experienced_restoration_program_3, experienced_treatments_descriptions_3, experienced_treatments_chemicals_3 = self.__cur.fetchone()
            return experienced_material_3, experienced_description_3, experienced_damages_description_3, experienced_research_title_3, experienced_research_description_3, experienced_restoration_program_3, experienced_treatments_descriptions_3, experienced_treatments_chemicals_3
        except sqlite3.Error as e:
            print('Нажаль виникла помилка отримання досвіду з бази даних' + str(e))
            flash('Нажаль виникла помилка отримання досвіду з бази даних', category='error')
        return []


    def get_practice_to_show(self, id_post):
        try:
            self.__cur.execute(
                f'SELECT experienced_material, experienced_description, experienced_damages_description,'
                f'experienced_research_title, experienced_research_description,'
                f'experienced_restoration_program, experienced_treatments_descriptions,'
                f'experienced_treatments_chemicals FROM practice WHERE id = {id_post} LIMIT 1')
            practice_fields_output = self.__cur.fetchone()
            if practice_fields_output:
                return practice_fields_output
            if not practice_fields_output:
                empty_practice_fields_output = '', '', '', '', '', '', '', ''
                return empty_practice_fields_output
        except sqlite3.Error as e:
            print('Нажаль виникла помилка отримання досвіду з бази даних' + str(e))
            flash('Нажаль виникла помилка отримання досвіду з бази даних', category='error')

    def get_practice_to_show_2(self, id_post):
        try:
            self.__cur.execute(
                f'SELECT experienced_material_2, experienced_description_2, experienced_damages_description_2,'
                f'experienced_research_title_2, experienced_research_description_2,'
                f'experienced_restoration_program_2, experienced_treatments_descriptions_2,'
                f'experienced_treatments_chemicals_2 FROM practice_2 WHERE id = {id_post} LIMIT 1')
            practice_fields_output_2 = self.__cur.fetchone()
            if practice_fields_output_2:
                return practice_fields_output_2
            if not practice_fields_output_2:
                empty_practice_fields_output = '', '', '', '', '', '', '', ''
                return empty_practice_fields_output
        except sqlite3.Error as e:
            print('Нажаль виникла помилка отримання досвіду з бази даних' + str(e))
            flash('Нажаль виникла помилка отримання досвіду з бази даних', category='error')

    def get_practice_to_show_3(self, id_post):
        try:
            self.__cur.execute(
                f'SELECT experienced_material_3, experienced_description_3, experienced_damages_description_3,'
                f'experienced_research_title_3, experienced_research_description_3,'
                f'experienced_restoration_program_3, experienced_treatments_descriptions_3,'
                f'experienced_treatments_chemicals_3 FROM practice_3 WHERE id = {id_post} LIMIT 1')
            practice_fields_output_3 = self.__cur.fetchone()
            if practice_fields_output_3:
                return practice_fields_output_3
            if not practice_fields_output_3:
                empty_practice_fields_output = '', '', '', '', '', '', '', ''
                return empty_practice_fields_output
        except sqlite3.Error as e:
            print('Нажаль виникла помилка отримання досвіду з бази даних' + str(e))
            flash('Нажаль виникла помилка отримання досвіду з бази даних', category='error')

    def get_practice_to_update(self, id_post):
        try:
            self.__cur.execute(
                f'SELECT experienced_material, experienced_description, experienced_damages_description, '
                f'experienced_research_title, experienced_research_description, '
                f'experienced_restoration_program, experienced_treatments_descriptions, '
                f'experienced_treatments_chemicals FROM practice WHERE id = {id_post} LIMIT 1')
            experienced_material, experienced_description, experienced_damages_description, \
            experienced_research_title, experienced_research_description, experienced_restoration_program, \
            experienced_treatments_descriptions, experienced_treatments_chemicals = self.__cur.fetchone()

            return experienced_material, experienced_description, experienced_damages_description, \
                   experienced_research_title, experienced_research_description, experienced_restoration_program, \
                   experienced_treatments_descriptions, experienced_treatments_chemicals
        except sqlite3.Error as e:
            print('Нажаль виникла помилка отримання досвіду з бази даних для редагування' + str(e))
            flash('Нажаль виникла помилка отримання досвіду з бази даних для додавання подібного досвіду',
                  category='error')

    def get_practice_to_update_2(self, id_post):
        try:
            self.__cur.execute(
                f'SELECT experienced_material_2, experienced_description_2, experienced_damages_description_2, '
                f'experienced_research_title_2, experienced_research_description_2, '
                f'experienced_restoration_program_2, experienced_treatments_descriptions_2, '
                f'experienced_treatments_chemicals_2 FROM practice_2 WHERE id = {id_post} LIMIT 1')
            experienced_material_2, experienced_description_2, experienced_damages_description_2, \
            experienced_research_title_2, experienced_research_description_2, experienced_restoration_program_2, \
            experienced_treatments_descriptions_2, experienced_treatments_chemicals_2 = self.__cur.fetchone()

            return experienced_material_2, experienced_description_2, experienced_damages_description_2, \
                   experienced_research_title_2, experienced_research_description_2, experienced_restoration_program_2,\
                   experienced_treatments_descriptions_2, experienced_treatments_chemicals_2
        except sqlite3.Error as e:
            print('Нажаль виникла помилка отримання досвіду з бази даних для редагування' + str(e))
            flash('Нажаль виникла помилка отримання досвіду з бази даних для додавання подібного досвіду',
                  category='error')

    def get_practice_to_update_3(self, id_post):
        try:
            self.__cur.execute(
                f'SELECT experienced_material_3, experienced_description_3, experienced_damages_description_3, '
                f'experienced_research_title_3, experienced_research_description_3, '
                f'experienced_restoration_program_3, experienced_treatments_descriptions_3, '
                f'experienced_treatments_chemicals_3 FROM practice_3 WHERE id = {id_post} LIMIT 1')
            experienced_material_3, experienced_description_3, experienced_damages_description_3, \
            experienced_research_title_3, experienced_research_description_3, experienced_restoration_program_3, \
            experienced_treatments_descriptions_3, experienced_treatments_chemicals_3 = self.__cur.fetchone()

            return experienced_material_3, experienced_description_3, experienced_damages_description_3, \
                   experienced_research_title_3, experienced_research_description_3, experienced_restoration_program_3,\
                   experienced_treatments_descriptions_3, experienced_treatments_chemicals_3
        except sqlite3.Error as e:
            print('Нажаль виникла помилка отримання досвіду з бази даних для редагування' + str(e))
            flash('Нажаль виникла помилка отримання досвіду з бази даних для додавання подібного досвіду',
                  category='error')

    def get_current_practice_id(self, id_post):
        try:
            self.__cur.execute(f'SELECT id FROM practice WHERE id = {id_post} LIMIT 1')
            experience_fields_output = self.__cur.fetchone()
            return experience_fields_output
        except sqlite3.Error as e:
            print('Нажаль виникла помилка отримання досвіду з бази даних для редагування' + str(e))
            flash('Нажаль виникла помилка отримання досвіду з бази даних для додавання подібного досвіду',
                  category='error')

    def get_current_practice_id_2(self, id_post):
        try:
            self.__cur.execute(f'SELECT id FROM practice_2 WHERE id = {id_post} LIMIT 1')
            experience_fields_output = self.__cur.fetchone()
            if experience_fields_output:
                return experience_fields_output
        except sqlite3.Error as e:
            print('Нажаль виникла помилка отримання другого досвіду з бази даних для редагування' + str(e))
            flash('Нажаль виникла помилка отримання другого досвіду з бази даних для додавання подібного досвіду',
                  category='error')

    def get_current_practice_id_3(self, id_post):
        try:
            self.__cur.execute(f'SELECT id FROM practice_3 WHERE id = {id_post} LIMIT 1')
            experience_fields_output = self.__cur.fetchone()
            if experience_fields_output:
                return experience_fields_output
        except sqlite3.Error as e:
            print('Нажаль виникла помилка отримання другого досвіду з бази даних для редагування' + str(e))
            flash('Нажаль виникла помилка отримання другого досвіду з бази даних для додавання подібного досвіду',
                  category='error')

    def get_current_experience_deletion_warning_data(self, id_post):
        try:
            self.__cur.execute(f'SELECT id, experienced_material FROM practice WHERE id = {id_post} LIMIT 1')
            experience_deletion_warning_data = self.__cur.fetchone()
            if experience_deletion_warning_data:
                return experience_deletion_warning_data
        except sqlite3.Error as e:
            print('Нажаль виникла помилка отримання поточного досвіду з бази даних при редагуванні' + str(e))
            flash('Нажаль виникла помилка отримання поточного досвіду з бази даних при редагуванні', category='error')

        return []

    def get_current_experience_deletion_warning_data_2(self, id_post):
        try:
            self.__cur.execute(f'SELECT id, experienced_material_2 FROM practice_2 WHERE id = {id_post} LIMIT 1')
            experience_deletion_warning_data = self.__cur.fetchone()
            if experience_deletion_warning_data:
                return experience_deletion_warning_data
        except sqlite3.Error as e:
            print('Нажаль виникла помилка отримання поточного другого досвіду з бази даних при редагуванні' + str(e))
            flash('Нажаль виникла помилка отримання поточного другого досвіду з бази даних при редагуванні',
                  category='error')

        return []

    def get_current_experience_deletion_warning_data_3(self, id_post):
        try:
            self.__cur.execute(f'SELECT id, experienced_material_3 FROM practice_3 WHERE id = {id_post} LIMIT 1')
            experience_deletion_warning_data = self.__cur.fetchone()
            if experience_deletion_warning_data:
                return experience_deletion_warning_data
        except sqlite3.Error as e:
            print('Нажаль виникла помилка отримання поточного третього досвіду з бази даних при редагуванні' + str(e))
            flash('Нажаль виникла помилка отримання поточного третього досвіду з бази даних при редагуванні',
                  category='error')

        return []

    def delete_experience(self, id_post):
        try:
            self.__cur.execute(f'DELETE FROM practice WHERE id == {id_post}')
            self.__db.commit()
        except sqlite3.Error as error:
            print('Нажаль виникла помилка видалення досвіду з бази даних' + str(error))
            flash('Нажаль виникла помилка видалення досвіду', category='error')
            return True

    def delete_experience_2(self, id_post):
        try:
            self.__cur.execute(f'DELETE FROM practice_2 WHERE id == {id_post}')
            self.__db.commit()
        except sqlite3.Error as error:
            print('Нажаль виникла помилка видалення другого досвіду з бази даних' + str(error))
            flash('Нажаль виникла помилка видалення другого досвіду', category='error')
            return True

    def delete_experience_3(self, id_post):
        try:
            self.__cur.execute(f'DELETE FROM practice_3 WHERE id == {id_post}')
            self.__db.commit()
        except sqlite3.Error as error:
            print('Нажаль виникла помилка видалення третього досвіду з бази даних' + str(error))
            flash('Нажаль виникла помилка видалення третього досвіду', category='error')
            return True
