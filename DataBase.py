import math
import time

from flask import flash
import sqlite3


class DataBase:
    def __init__(self, db):
        self.__db = db
        self.__cursor = db.cursor()

    def get_main_menu(self):
        main_menu = '''SELECT * FROM main_menu'''
        try:
            self.__cursor.execute(main_menu)
            main_menu_options = self.__cursor.fetchall()
            return main_menu_options
        except:
            print('На жаль, виникла помилка читання елементів меню з бази даних')
            flash('На жаль, виникла помилка і елементи меню не відображаються', category='error')
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
            self.__cursor.execute(
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
        except sqlite3.Error as error:
            print('На жаль, виникла помилка додавання паспорта в базу даних' + str(error))
            flash('На жаль, виникла помилка збереження паспорта', category='error')

    def get_passport(self, id_post):
        try:
            self.__cursor.execute(
                f'SELECT passport_number, inventory_number, acceptance_number, institution_name, department_name,'
                f'definition, typological, object_owner, author, clarified_author, object_name, clarified_object_name,'
                f'time_of_creation, clarified_time_of_creation, material, clarified_material, technique,'
                f'clarified_technique, object_size, clarified_size, weight, clarified_weight, reason,'
                f'object_input_date, execute_restorer, object_output_date, responsible_restorer, origin_description,'
                f'appearance_description, damages_description, signs_description, size_description,'
                f'purposes_researches, methods_researches, executor_date_researches, results_researches,'
                f'restoration_program, treatments_descriptions, treatments_chemicals, treatments_executor_date,'
                f' treatments_results FROM passports WHERE id = {id_post} LIMIT 1')
            passport = self.__cursor.fetchone()
            return passport
        except sqlite3.Error as error:
            print('На жаль, виникла помилка отримання паспорта з бази даних' + str(error))
            flash('На жаль, виникла помилка отримання паспорта з бази даних', category='error')

    def get_passports_preview(self, author_of_passport_id):
        try:
            self.__cursor.execute(
                f'SELECT id, inventory_number, object_name FROM passports WHERE author_of_passport_id = {author_of_passport_id} ORDER BY time DESC')
            passports_preview = self.__cursor.fetchall()
            if passports_preview:
                return passports_preview
        except sqlite3.Error as error:
            print('На жаль, виникла помилка отримання паспортів з бази даних для портфоліо' + str(error))
            flash('На жаль, виникла помилка відображення портфоліо', category='error')
        return []

    def get_current_passport_id(self, id_post):
        try:
            self.__cursor.execute(f'SELECT id FROM passports WHERE id = {id_post} LIMIT 1')
            passport_id = self.__cursor.fetchone()
            return passport_id
        except sqlite3.Error as error:
            print('На жаль, виникла помилка отримання поточного паспорта з бази даних при редагуванні' + str(error))
            flash('На жаль, виникла помилка отримання поточного паспорта з бази даних при редагуванні', category='error')

    def get_current_passport_deletion_warning_data(self, id_post):
        try:
            self.__cursor.execute(f'SELECT id, object_name, inventory_number FROM passports WHERE id = {id_post} LIMIT 1')
            passport_id = self.__cursor.fetchone()
            return passport_id
        except sqlite3.Error as error:
            print('На жаль, виникла помилка отримання поточного паспорта з бази даних при редагуванні' + str(error))
            flash('На жаль, виникла помилка отримання поточного паспорта з бази даних при редагуванні', category='error')

    def delete_passport(self, id_post):
        try:
            self.__cursor.execute(f'DELETE FROM passports WHERE id == {id_post}')
            self.__db.commit()
        except sqlite3.Error as error:
            print('На жаль, виникла помилка видалення паспорта з бази даних' + str(error))
            flash('На жаль, виникла помилка видалення паспорта', category='error')

    def add_restorer(self, restorer_name, restorer_email, hashed_restorer_password):
        try:
            self.__cursor.execute(f"SELECT COUNT() as 'count' FROM restorers WHERE restorer_name LIKE '{restorer_name}'")
            existed_restorer_name = self.__cursor.fetchone()
            if existed_restorer_name['count'] > 0:
                flash("Користувач з таким ім'ям вже має кабінет", category='error')
                return False
            self.__cursor.execute(f"SELECT COUNT() as 'count' FROM restorers WHERE restorer_email LIKE '{restorer_email}'")
            existed_restorer_email = self.__cursor.fetchone()
            if existed_restorer_email['count'] > 0:
                flash("Користувач з такою електронною адресою вже має кабінет", category='error')
                return False
            else:
                tm = math.floor(time.time())
                self.__cursor.execute('INSERT INTO restorers VALUES(NULL, ?, ?, ?, ?)',
                                   (restorer_name, restorer_email, hashed_restorer_password, tm))
                self.__db.commit()
        except sqlite3.Error as error:
            print('На жаль, виникла помилка додавання користувача в базу даних' + str(error))
            flash('На жаль, виникла помилка додавання користувача в базу даних', category='error')
            return False

        return True

    def get_restorer(self, restorer_id):
        try:
            self.__cursor.execute(f"SELECT * FROM restorers WHERE id = {restorer_id} LIMIT 1")
            result = self.__cursor.fetchone()
            if not result:
                print('На жаль, користувача за таким ай ді не знайдено')
                flash('На жаль, користувача не знайдено', category='error')
                return False

            return result
        except sqlite3.Error as error:
            print('На жаль, виникла помилка отримання даних про реставратора з бази даних за таким ай ді' + str(error))
            flash('На жаль, виникла помилка отримання даних про реставратора з бази даних', category='error')

        return False

    def get_restorer_by_email(self, restorer_email):
        try:
            self.__cursor.execute(f"SELECT * FROM restorers WHERE restorer_email = '{restorer_email}' LIMIT 1")
            result = self.__cursor.fetchone()
            if not result:
                print('На жаль, користувача за такою електронною адресою не знайдено')
                flash('На жаль, користувача за такою електронною адресою не знайдено', category='error')
                return False

            return result
        except sqlite3.Error as error:
            print('На жаль, виникла помилка отримання електронної адреси з бази даних' + str(error))
            flash('На жаль, виникла помилка отримання електронної адреси реставратора з бази даних', category='error')

        return False

    def check_experience(self, author_of_experience_id):
        self.__cursor.execute(f"SELECT experienced_material, experienced_description, experienced_damages_description, experienced_research_title, experienced_research_description, experienced_restoration_program, experienced_treatments_descriptions, experienced_treatments_chemicals FROM experience WHERE author_of_experience_id = '{author_of_experience_id}' LIMIT 1")
        experience = self.__cursor.fetchone()
        if experience:
            return True
        else:
            return False

    def check_experience_2(self, author_of_experience_id):
        self.__cursor.execute(f"SELECT experienced_material_2, experienced_description_2, experienced_damages_description_2, experienced_research_title_2, experienced_research_description_2, experienced_restoration_program_2, experienced_treatments_descriptions_2, experienced_treatments_chemicals_2 FROM experience_2 WHERE author_of_experience_id = '{author_of_experience_id}' LIMIT 1")
        experience_2 = self.__cursor.fetchone()
        if experience_2:
            return True
        else:
            return False

    def check_experience_3(self, author_of_experience_id):
        self.__cursor.execute(f"SELECT experienced_material_3, experienced_description_3, experienced_damages_description_3, experienced_research_title_3, experienced_research_description_3, experienced_restoration_program_3, experienced_treatments_descriptions_3, experienced_treatments_chemicals_3 FROM experience_3 WHERE author_of_experience_id = '{author_of_experience_id}' LIMIT 1")
        experience_3 = self.__cursor.fetchone()
        if experience_3:
            return True
        else:
            return False

    def store_experience(self, experienced_material, experienced_description, experienced_damages_description, experienced_research_title, experienced_research_description, experienced_restoration_program, experienced_treatments_descriptions, experienced_treatments_chemicals, author_of_experience_id):
        try:
            tm = math.floor(time.time())
            self.__cursor.execute(f'INSERT INTO experience VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                                 (experienced_material, experienced_description, experienced_damages_description, experienced_research_title, experienced_research_description, experienced_restoration_program, experienced_treatments_descriptions, experienced_treatments_chemicals, author_of_experience_id, tm))
            self.__db.commit()
        except sqlite3.Error as error:
            print('На жаль, виникла помилка отримання першого досвіду з бази даних' + str(error))
            flash('На жаль, виникла помилка отримання першого досвіду з бази даних', category='error')

    def store_experience_2(self, experienced_material_2, experienced_description_2, experienced_damages_description_2, experienced_research_title_2, experienced_research_description_2, experienced_restoration_program_2, experienced_treatments_descriptions_2, experienced_treatments_chemicals_2, author_of_experience_id):
        try:
            tm = math.floor(time.time())
            self.__cursor.execute(f'INSERT INTO experience_2 VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                                 (experienced_material_2, experienced_description_2, experienced_damages_description_2, experienced_research_title_2, experienced_research_description_2, experienced_restoration_program_2, experienced_treatments_descriptions_2, experienced_treatments_chemicals_2, author_of_experience_id, tm))
            self.__db.commit()
        except sqlite3.Error as error:
            print('На жаль, виникла помилка отримання другого досвіду з бази даних' + str(error))
            flash('На жаль, виникла помилка отримання другого досвіду з бази даних', category='error')

    def store_experience_3(self, experienced_material_3, experienced_description_3, experienced_damages_description_3, experienced_research_title_3, experienced_research_description_3, experienced_restoration_program_3, experienced_treatments_descriptions_3, experienced_treatments_chemicals_3, author_of_experience_id):
        try:
            tm = math.floor(time.time())
            self.__cursor.execute(f'INSERT INTO experience_3 VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                                 (experienced_material_3, experienced_description_3, experienced_damages_description_3, experienced_research_title_3, experienced_research_description_3, experienced_restoration_program_3, experienced_treatments_descriptions_3, experienced_treatments_chemicals_3, author_of_experience_id, tm))
            self.__db.commit()
        except sqlite3.Error as error:
            print('На жаль, виникла помилка отримання третього досвіду з бази даних' + str(error))
            flash('На жаль, виникла помилка отримання третього досвіду з бази даних', category='error')

    def get_experience(self, author_of_experience_id):
        try:
            self.__cursor.execute(f"SELECT experienced_material, experienced_description, experienced_damages_description, experienced_research_title, experienced_research_description, experienced_restoration_program, experienced_treatments_descriptions, experienced_treatments_chemicals FROM experience WHERE author_of_experience_id = '{author_of_experience_id}' LIMIT 1")
            experienced_material, experienced_description, experienced_damages_description, experienced_research_title, experienced_research_description, experienced_restoration_program, experienced_treatments_descriptions, experienced_treatments_chemicals = self.__cursor.fetchone()
            return experienced_material, experienced_description, experienced_damages_description, experienced_research_title, experienced_research_description, experienced_restoration_program, experienced_treatments_descriptions, experienced_treatments_chemicals
        except sqlite3.Error as error:
            print('На жаль, виникла помилка отримання першого досвіду з бази даних для друку' + str(error))
            flash('На жаль, виникла помилка отримання першого досвіду з бази даних для друку', category='error')

    def get_experience_2(self, author_of_experience_id):
        try:
            self.__cursor.execute(f"SELECT experienced_material_2, experienced_description_2, experienced_damages_description_2, experienced_research_title_2, experienced_research_description_2, experienced_restoration_program_2, experienced_treatments_descriptions_2, experienced_treatments_chemicals_2 FROM experience_2 WHERE author_of_experience_id = '{author_of_experience_id}' LIMIT 1")
            experienced_material_2, experienced_description_2, experienced_damages_description_2, experienced_research_title_2, experienced_research_description_2, experienced_restoration_program_2, experienced_treatments_descriptions_2, experienced_treatments_chemicals_2 = self.__cursor.fetchone()
            return experienced_material_2, experienced_description_2, experienced_damages_description_2, experienced_research_title_2, experienced_research_description_2, experienced_restoration_program_2, experienced_treatments_descriptions_2, experienced_treatments_chemicals_2
        except sqlite3.Error as e:
            print('На жаль, виникла помилка отримання другого досвіду з бази даних для друку' + str(e))
            flash('На жаль, виникла помилка отримання другого досвіду з бази даних для друку', category='error')

    def get_experience_3(self, author_of_experience_id):
        try:
            self.__cursor.execute(f"SELECT experienced_material_3, experienced_description_3, experienced_damages_description_3, experienced_research_title_3, experienced_research_description_3, experienced_restoration_program_3, experienced_treatments_descriptions_3, experienced_treatments_chemicals_3 FROM experience_3 WHERE author_of_experience_id = '{author_of_experience_id}' LIMIT 1")
            experienced_material_3, experienced_description_3, experienced_damages_description_3, experienced_research_title_3, experienced_research_description_3, experienced_restoration_program_3, experienced_treatments_descriptions_3, experienced_treatments_chemicals_3 = self.__cursor.fetchone()
            return experienced_material_3, experienced_description_3, experienced_damages_description_3, experienced_research_title_3, experienced_research_description_3, experienced_restoration_program_3, experienced_treatments_descriptions_3, experienced_treatments_chemicals_3
        except sqlite3.Error as error:
            print('На жаль, виникла помилка отримання третього досвіду з бази даних для друку' + str(error))
            flash('На жаль, виникла помилка отримання третього досвіду з бази даних для друку', category='error')

    def get_experiences_preview(self, author_of_experience_id):
        try:
            self.__cursor.execute(f'SELECT id, experienced_material FROM experience WHERE author_of_experience_id = {author_of_experience_id} ORDER BY time DESC')
            experiences_preview = self.__cursor.fetchall()
            if experiences_preview:
                return experiences_preview
            if not experiences_preview:
                return print('На жаль, у вас ще немає досвіду з першої практики')
        except sqlite3.Error as error:
            print('На жаль, виникла помилка отримання частини вашого першого реставраційного досвіду з бази даних' + str(error))
            flash('На жаль, виникла помилка отримання частини вашого першого реставраційного досвіду з бази даних', category='error')

    def get_experiences_preview_2(self, author_of_experience_id):
        try:
            self.__cursor.execute(
                f'SELECT id, experienced_material_2 FROM experience_2 WHERE author_of_experience_id = {author_of_experience_id} ORDER BY time DESC')
            experiences_preview_2 = self.__cursor.fetchall()
            if experiences_preview_2:
                return experiences_preview_2
            if not experiences_preview_2:
                return print('На жаль, у вас ще немає досвіду з другої практики')
        except sqlite3.Error as error:
            print('На жаль, виникла помилка отримання частини вашого першого реставраційного досвіду з бази даних' + str(error))
            flash('На жаль, виникла помилка отримання частини вашого першого реставраційного досвіду з бази даних', category='error')

    def get_experiences_preview_3(self, author_of_experience_id):
        try:
            self.__cursor.execute(
                f'SELECT id, experienced_material_3 FROM experience_3 WHERE author_of_experience_id = {author_of_experience_id} ORDER BY time DESC')
            experiences_preview_3 = self.__cursor.fetchall()
            if experiences_preview_3:
                return experiences_preview_3
            if not experiences_preview_3:
                return print('На жаль, у вас ще немає досвіду з третьої практики')
        except sqlite3.Error as error:
            print('На жаль, виникла помилка отримання частини вашого першого реставраційного досвіду з бази даних' + str(error))
            flash('На жаль, виникла помилка отримання частини вашого першого реставраційного досвіду з бази даних', category='error')

    def get_experience_to_show(self, id_post):
        try:
            self.__cursor.execute(
                f'SELECT experienced_material, experienced_description, experienced_damages_description,'
                f'experienced_research_title, experienced_research_description,'
                f'experienced_restoration_program, experienced_treatments_descriptions,'
                f'experienced_treatments_chemicals FROM experience WHERE id = {id_post} LIMIT 1')
            experience_fields_output = self.__cursor.fetchone()
            return experience_fields_output
        except sqlite3.Error as error:
            print('На жаль, виникла помилка отримання першого досвіду з бази даних (Видалення)' + str(error))
            flash('На жаль, виникла помилка отримання першого досвіду з бази даних (Видалення)', category='error')

    def get_experience_to_show_2(self, id_post):
        try:
            self.__cursor.execute(
                f'SELECT experienced_material_2, experienced_description_2, experienced_damages_description_2,'
                f'experienced_research_title_2, experienced_research_description_2,'
                f'experienced_restoration_program_2, experienced_treatments_descriptions_2,'
                f'experienced_treatments_chemicals_2 FROM experience_2 WHERE id = {id_post} LIMIT 1')
            experience_fields_output_2 = self.__cursor.fetchone()
            return experience_fields_output_2
        except sqlite3.Error as error:
            print('На жаль, виникла помилка отримання другого досвіду з бази даних (Видалення)' + str(error))
            flash('На жаль, виникла помилка отримання другого досвіду з бази даних (Видалення)', category='error')

    def get_experience_to_show_3(self, id_post):
        try:
            self.__cursor.execute(
                f'SELECT experienced_material_3, experienced_description_3, experienced_damages_description_3,'
                f'experienced_research_title_3, experienced_research_description_3,'
                f'experienced_restoration_program_3, experienced_treatments_descriptions_3,'
                f'experienced_treatments_chemicals_3 FROM experience_3 WHERE id = {id_post} LIMIT 1')
            experience_fields_output_3 = self.__cursor.fetchone()
            return experience_fields_output_3
        except sqlite3.Error as error:
            print('На жаль, виникла помилка отримання третього досвіду з бази даних (Видалення)' + str(error))
            flash('На жаль, виникла помилка отримання третього досвіду з бази даних (Видалення)', category='error')

    def get_current_experience_id(self, id_post):
        try:
            self.__cursor.execute(f'SELECT id FROM experience WHERE id = {id_post} LIMIT 1')
            experience_id = self.__cursor.fetchone()
            return experience_id
        except sqlite3.Error as error:
            print('На жаль, виникла помилка отримання першого досвіду з бази даних для редагування' + str(error))
            flash('На жаль, виникла помилка отримання першого досвіду з бази даних для додавання подібного досвіду', category='error')

    def get_current_experience_id_2(self, id_post):
        try:
            self.__cursor.execute(f'SELECT id FROM experience_2 WHERE id = {id_post} LIMIT 1')
            experience_id_2 = self.__cursor.fetchone()
            return experience_id_2
        except sqlite3.Error as error:
            print('На жаль, виникла помилка отримання другого досвіду з бази даних для редагування' + str(error))
            flash('На жаль, виникла помилка отримання другого досвіду з бази даних для додавання подібного досвіду', category='error')

    def get_current_experience_id_3(self, id_post):
        try:
            self.__cursor.execute(f'SELECT id FROM experience_3 WHERE id = {id_post} LIMIT 1')
            experience_id_3 = self.__cursor.fetchone()
            return experience_id_3
        except sqlite3.Error as error:
            print('На жаль, виникла помилка отримання третього досвіду з бази даних для редагування' + str(error))
            flash('На жаль, виникла помилка отримання третього досвіду з бази даних для додавання подібного досвіду', category='error')

    def get_experience_to_update(self, id_post):
        try:
            self.__cursor.execute(
                f'SELECT experienced_material, experienced_description, experienced_damages_description, '
                f'experienced_research_title, experienced_research_description, '
                f'experienced_restoration_program, experienced_treatments_descriptions, '
                f'experienced_treatments_chemicals FROM experience WHERE id = {id_post} LIMIT 1')
            experienced_material, experienced_description, experienced_damages_description, \
            experienced_research_title, experienced_research_description, experienced_restoration_program, \
            experienced_treatments_descriptions, experienced_treatments_chemicals = self.__cursor.fetchone()

            return experienced_material, experienced_description, experienced_damages_description, \
                   experienced_research_title, experienced_research_description, experienced_restoration_program, \
                   experienced_treatments_descriptions, experienced_treatments_chemicals
        except sqlite3.Error as error:
            print('На жаль, виникла помилка отримання першого досвіду з бази даних для редагування' + str(error))
            flash('На жаль, виникла помилка отримання першого досвіду з бази даних для редагування', category='error')

    def get_experience_to_update_2(self, id_post):
        try:
            self.__cursor.execute(
                f'SELECT experienced_material_2, experienced_description_2, experienced_damages_description_2, '
                f'experienced_research_title_2, experienced_research_description_2, '
                f'experienced_restoration_program_2, experienced_treatments_descriptions_2, '
                f'experienced_treatments_chemicals_2 FROM experience_2 WHERE id = {id_post} LIMIT 1')
            experienced_material_2, experienced_description_2, experienced_damages_description_2, \
            experienced_research_title_2, experienced_research_description_2, experienced_restoration_program_2, \
            experienced_treatments_descriptions_2, experienced_treatments_chemicals_2 = self.__cursor.fetchone()

            return experienced_material_2, experienced_description_2, experienced_damages_description_2, \
                   experienced_research_title_2, experienced_research_description_2, experienced_restoration_program_2,\
                   experienced_treatments_descriptions_2, experienced_treatments_chemicals_2
        except sqlite3.Error as error:
            print('На жаль, виникла помилка отримання другого досвіду з бази даних для редагування' + str(error))
            flash('На жаль, виникла помилка отримання другого досвіду з бази даних для редагування', category='error')

    def get_experience_to_update_3(self, id_post):
        try:
            self.__cursor.execute(
                f'SELECT experienced_material_3, experienced_description_3, experienced_damages_description_3, '
                f'experienced_research_title_3, experienced_research_description_3, '
                f'experienced_restoration_program_3, experienced_treatments_descriptions_3, '
                f'experienced_treatments_chemicals_3 FROM experience_3 WHERE id = {id_post} LIMIT 1')
            experienced_material_3, experienced_description_3, experienced_damages_description_3, \
            experienced_research_title_3, experienced_research_description_3, experienced_restoration_program_3, \
            experienced_treatments_descriptions_3, experienced_treatments_chemicals_3 = self.__cursor.fetchone()

            return experienced_material_3, experienced_description_3, experienced_damages_description_3, \
                   experienced_research_title_3, experienced_research_description_3, experienced_restoration_program_3,\
                   experienced_treatments_descriptions_3, experienced_treatments_chemicals_3
        except sqlite3.Error as error:
            print('На жаль, виникла помилка отримання третього досвіду з бази даних для редагування' + str(error))
            flash('На жаль, виникла помилка отримання третього досвіду з бази даних для редагування', category='error')

    def get_current_experience_deletion_warning_data(self, id_post):
        try:
            self.__cursor.execute(f'SELECT id, experienced_material FROM experience WHERE id = {id_post} LIMIT 1')
            experience_deletion_warning_data = self.__cursor.fetchone()
            return experience_deletion_warning_data
        except sqlite3.Error as e:
            print('На жаль, виникла помилка отримання поточного досвіду з бази даних при редагуванні' + str(e))
            flash('На жаль, виникла помилка отримання поточного досвіду з бази даних при редагуванні', category='error')

    def get_current_experience_deletion_warning_data_2(self, id_post):
        try:
            self.__cursor.execute(f'SELECT id, experienced_material_2 FROM experience_2 WHERE id = {id_post} LIMIT 1')
            experience_deletion_warning_data_2 = self.__cursor.fetchone()
            return experience_deletion_warning_data_2
        except sqlite3.Error as e:
            print('На жаль, виникла помилка отримання поточного другого досвіду з бази даних при редагуванні' + str(e))
            flash('На жаль, виникла помилка отримання поточного другого досвіду з бази даних при редагуванні', category='error')

    def count_experiences_preview(self, author_of_experience_id):
        try:
            self.__cursor.execute(f'SELECT id FROM experience WHERE author_of_experience_id = {author_of_experience_id} LIMIT 1')
            experiences_preview = self.__cursor.fetchall()
            if experiences_preview:
                return experiences_preview
            if not experiences_preview:
                empty_table = 'empty'
                return empty_table
        except sqlite3.Error as error:
            print('На жаль, при переліку виникла помилка отримання вашого першого реставраційного досвіду з бази даних' + str(error))
            flash('На жаль, при переліку виникла помилка отримання вашого першого реставраційного досвіду з бази даних', category='error')

    def count_experiences_preview_2(self, author_of_experience_id):
        try:
            self.__cursor.execute(f'SELECT id FROM experience_2 WHERE author_of_experience_id = {author_of_experience_id} LIMIT 1')
            experiences_preview = self.__cursor.fetchall()
            if experiences_preview:
                return experiences_preview
            if not experiences_preview:
                empty_table = 'empty'
                return empty_table
        except sqlite3.Error as error:
            print('На жаль, при переліку виникла помилка отримання вашого друого реставраційного досвіду з бази даних' + str(error))
            flash('На жаль, при переліку виникла помилка отримання вашого другого реставраційного досвіду з бази даних', category='error')

    def count_experiences_preview_3(self, author_of_experience_id):
        try:
            self.__cursor.execute(
                f'SELECT id FROM experience_3 WHERE author_of_experience_id = {author_of_experience_id} LIMIT 1')
            experiences_preview = self.__cursor.fetchall()
            if experiences_preview:
                return experiences_preview
            if not experiences_preview:
                empty_table = 'empty'
                return empty_table
        except sqlite3.Error as error:
            print('На жаль, при переліку виникла помилка отримання вашого третього реставраційного досвіду з бази даних' + str(error))
            flash('На жаль, при переліку виникла помилка отримання вашого третього реставраційного досвіду з бази даних', category='error')

    def get_current_experience_deletion_warning_data_3(self, id_post):
        try:
            self.__cursor.execute(f'SELECT id, experienced_material_3 FROM experience_3 WHERE id = {id_post} LIMIT 1')
            experience_deletion_warning_data_3 = self.__cursor.fetchone()
            return experience_deletion_warning_data_3
        except sqlite3.Error as e:
            print('На жаль, виникла помилка отримання поточного третього досвіду з бази даних при редагуванні' + str(e))
            flash('На жаль, виникла помилка отримання поточного третього досвіду з бази даних при редагуванні', category='error')

    def delete_experience(self, id_post):
        try:
            self.__cursor.execute(f'DELETE FROM experience WHERE id == {id_post}')
            self.__db.commit()
        except sqlite3.Error as error:
            print('На жаль, виникла помилка видалення досвіду з бази даних' + str(error))
            flash('На жаль, виникла помилка видалення досвіду', category='error')

    def delete_experience_2(self, id_post):
        try:
            self.__cursor.execute(f'DELETE FROM experience_2 WHERE id == {id_post}')
            self.__db.commit()
        except sqlite3.Error as error:
            print('На жаль, виникла помилка видалення другого досвіду з бази даних' + str(error))
            flash('На жаль, виникла помилка видалення другого досвіду', category='error')

    def delete_experience_3(self, id_post):
        try:
            self.__cursor.execute(f'DELETE FROM experience_3 WHERE id == {id_post}')
            self.__db.commit()
        except sqlite3.Error as error:
            print('На жаль, виникла помилка видалення третього досвіду з бази даних' + str(error))
            flash('На жаль, виникла помилка видалення третього досвіду', category='error')
