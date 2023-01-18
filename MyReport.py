import os

from flask import Flask, render_template, url_for, request, flash, redirect, abort, g, send_file
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user

from DataBase import DataBase
from printable.PrintPassportPaper import Passport
from Login import RestorerLogin

DATABASE = '/tmp/flsite.db'

app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(dict(DATABASE=os.path.join(app.root_path, 'MyReport_DataTable,db')))
app.config['SECRET_KEY'] = '467dfc20ddc0d0de73c86d5fe37ef2ee132d3be0'

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Вітаємо! Увійдіть в особистий кабінет для створення публікацій та їх перегляду'
login_manager.login_message_category = 'success'


@login_manager.user_loader
def load_restorer(restorer_id):
    db = get_db()
    dbase = DataBase(db)
    return RestorerLogin().from_data_base(restorer_id, dbase)


def create_db():
    db = connect_db()
    with app.open_resource('DataTables_building.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


def connect_db():
    connection = sqlite3.connect(app.config['DATABASE'])
    connection.row_factory = sqlite3.Row
    return connection


def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()


@app.route('/')
def index():
    print(url_for('index'))
    db = get_db()
    dbase = DataBase(db)
    return render_template('index.html', main_menu=dbase.get_main_menu(), web_page_title='Головна')


@app.route('/portfolio')
@login_required
def portfolio():
    print(url_for('portfolio'))
    db = get_db()
    dbase = DataBase(db)
    current_restorer_id = current_user.get_id()
    return render_template('portfolio.html', main_menu=dbase.get_main_menu(), web_page_title='Портфоліо',
                           passports=dbase.get_passports_preview(current_restorer_id))


@app.route('/add_passport', methods=['POST', 'GET'])
@login_required
def add_passport():
    db = get_db()
    dbase = DataBase(db)
    current_restorer_id = current_user.get_id()

    experience = bool(dbase.check_experience(current_restorer_id))
    experience_2 = bool(dbase.check_experience_2(current_restorer_id))
    experience_3 = bool(dbase.check_experience_3(current_restorer_id))

    if experience:
        experienced_material, experienced_description, experienced_damages_description, experienced_research_title, experienced_research_description, experienced_restoration_program, experienced_treatments_descriptions, experienced_treatments_chemicals = dbase.get_experience(current_restorer_id)
    else:
        experienced_material, experienced_description, experienced_damages_description, experienced_research_title, experienced_research_description, experienced_restoration_program, experienced_treatments_descriptions, experienced_treatments_chemicals = '', '', '', '', '', '', '', ''

    if experience_2:
        experienced_material_2, experienced_description_2, experienced_damages_description_2, experienced_research_title_2, experienced_research_description_2, experienced_restoration_program_2, experienced_treatments_descriptions_2, experienced_treatments_chemicals_2 = dbase.get_experience_2(current_restorer_id)
    else:
        experienced_material_2, experienced_description_2, experienced_damages_description_2, experienced_research_title_2, experienced_research_description_2, experienced_restoration_program_2, experienced_treatments_descriptions_2, experienced_treatments_chemicals_2 = '', '', '', '', '', '', '', ''

    if experience_3:
        experienced_material_3, experienced_description_3, experienced_damages_description_3, experienced_research_title_3, experienced_research_description_3, experienced_restoration_program_3, experienced_treatments_descriptions_3, experienced_treatments_chemicals_3 = dbase.get_experience_3(current_restorer_id)
    else:
        experienced_material_3, experienced_description_3, experienced_damages_description_3, experienced_research_title_3, experienced_research_description_3, experienced_restoration_program_3, experienced_treatments_descriptions_3, experienced_treatments_chemicals_3 = '', '', '', '', '', '', '', ''

    if request.method == 'POST':
        if len(request.form['inventory_number']) > 0 and len(request.form['acceptance_number']) > 0:

            dbase.store_passport(request.form['passport_number'],
                                 request.form['inventory_number'],
                                 request.form['acceptance_number'],
                                 request.form['institution_name'],
                                 request.form['department_name'],
                                 request.form['definition'],
                                 request.form['typological'],
                                 request.form['object_owner'],
                                 request.form['author'],
                                 request.form['clarified_author'],
                                 request.form['object_name'],
                                 request.form['clarified_object_name'],
                                 request.form['time_of_creation'],
                                 request.form['clarified_time_of_creation'],
                                 request.form['material'],
                                 request.form['clarified_material'],
                                 request.form['technique'],
                                 request.form['clarified_technique'],
                                 request.form['object_size'],
                                 request.form['clarified_size'],
                                 request.form['weight'],
                                 request.form['clarified_weight'],
                                 request.form['reason'],
                                 request.form['object_input_date'],
                                 request.form['execute_restorer'],
                                 request.form['object_output_date'],
                                 request.form['responsible_restorer'],
                                 request.form['origin_description'],
                                 request.form['appearance_description'],
                                 request.form['damages_description'],
                                 request.form['signs_description'],
                                 request.form['size_description'],
                                 request.form['purposes_researches'],
                                 request.form['methods_researches'],
                                 request.form['executor_date_researches'],
                                 request.form['results_researches'],
                                 request.form['restoration_program'],
                                 request.form['treatments_descriptions'],
                                 request.form['treatments_chemicals'],
                                 request.form['treatments_executor_date'],
                                 request.form['treatments_results'],
                                 current_restorer_id)

            flash('Успішно опубліковано!', category='success')
            return redirect(url_for('portfolio'), code=301)

        else:
            flash("Спочатку введіть, будь ласка, інвентарний номер та дані акта приймання пам'ятки.", category='error')
    return render_template('add_passport.html', main_menu=dbase.get_main_menu(), web_page_title='Публікація',
                            experienced_material=experienced_material,
                            experienced_damages_description=experienced_damages_description,
                            experienced_research_title=experienced_research_title,
                            experienced_research_description=experienced_research_description,
                            experienced_restoration_program=experienced_restoration_program,
                            experienced_treatments_descriptions=experienced_treatments_descriptions,
                            experienced_treatments_chemicals=experienced_treatments_chemicals,
                            experienced_description=experienced_description,
                            experienced_material_2=experienced_material_2,
                            experienced_damages_description_2=experienced_damages_description_2,
                            experienced_research_title_2=experienced_research_title_2,
                            experienced_research_description_2=experienced_research_description_2,
                            experienced_restoration_program_2=experienced_restoration_program_2,
                            experienced_treatments_descriptions_2=experienced_treatments_descriptions_2,
                            experienced_treatments_chemicals_2=experienced_treatments_chemicals_2,
                            experienced_description_2=experienced_description_2,
                            experienced_material_3=experienced_material_3,
                            experienced_damages_description_3=experienced_damages_description_3,
                            experienced_research_title_3=experienced_research_title_3,
                            experienced_research_description_3=experienced_research_description_3,
                            experienced_restoration_program_3=experienced_restoration_program_3,
                            experienced_treatments_descriptions_3=experienced_treatments_descriptions_3,
                            experienced_treatments_chemicals_3=experienced_treatments_chemicals_3,
                            experienced_description_3=experienced_description_3)


@app.route('/show_passport/<string:id_post>')
@login_required
def show_passport(id_post):
    db = get_db()
    dbase = DataBase(db)
    passport = Passport()

    passport_number, inventory_number, acceptance_number, institution_name, department_name, definition, typological, \
    object_owner, author, clarified_author, object_name, clarified_object_name, time_of_creation, \
    clarified_time_of_creation, material, clarified_material, technique, clarified_technique, \
    object_size, clarified_size, weight, clarified_weight, reason, object_input_date, execute_restorer, \
    object_output_date, responsible_restorer, origin_description, appearance_description, damages_description, \
    signs_description, size_description, purposes_researches, methods_researches, executor_date_researches, \
    results_researches, restoration_program, treatments_descriptions, treatments_chemicals, treatments_executor_date, \
    treatments_results = dbase.get_passport(id_post)

    passport.build_passport(passport_number, inventory_number, acceptance_number, institution_name, department_name,
                            definition, typological, object_owner, author, clarified_author, object_name,
                            clarified_object_name, time_of_creation, clarified_time_of_creation, material,
                            clarified_material, technique, clarified_technique, object_size, clarified_size, weight,
                            clarified_weight, reason, object_input_date, execute_restorer, object_output_date,
                            responsible_restorer, origin_description, appearance_description, damages_description,
                            signs_description, size_description, purposes_researches, methods_researches,
                            executor_date_researches, results_researches, restoration_program, treatments_descriptions,
                            treatments_chemicals, treatments_executor_date, treatments_results)

    if not inventory_number:
        abort(404)

    return render_template('show_passport.html', main_menu=dbase.get_main_menu(),
                           web_page_title=inventory_number, passport_number=passport_number,
                           inventory_number=inventory_number,
                           acceptance_number=acceptance_number,
                           institution_name=institution_name,
                           department_name=department_name, definition=definition,
                           typological=typological, object_owner=object_owner,
                           author=author, clarified_author=clarified_author,
                           object_name=object_name,
                           clarified_object_name=clarified_object_name,
                           time_of_creation=time_of_creation,
                           clarified_time_of_creation=clarified_time_of_creation,
                           material=material, clarified_material=clarified_material,
                           technique=technique, clarified_technique=clarified_technique,
                           object_size=object_size, clarified_size=clarified_size,
                           weight=weight, clarified_weight=clarified_weight,
                           reason=reason, object_input_date=object_input_date,
                           execute_restorer=execute_restorer, object_output_date=object_output_date,
                           responsible_restorer=responsible_restorer, origin_description=origin_description,
                           appearance_description=appearance_description, damages_description=damages_description,
                           signs_description=signs_description, size_description=size_description,
                           purposes_researches=purposes_researches, methods_researches=methods_researches,
                           executor_date_researches=executor_date_researches, results_researches=results_researches,
                           restoration_program=restoration_program, treatments_descriptions=treatments_descriptions,
                           treatments_chemicals=treatments_chemicals, treatments_executor_date=treatments_executor_date,
                           treatments_results=treatments_results)


@app.route('/update_passport/<string:id_post>', methods=['POST', 'GET'])
@login_required
def update_passport(id_post):
    db = get_db()
    dbase = DataBase(db)
    current_restorer_id = current_user.get_id()

    passport_number, inventory_number, acceptance_number, institution_name, department_name, definition, typological, \
    object_owner, author, clarified_author, object_name, clarified_object_name, time_of_creation, \
    clarified_time_of_creation, material, clarified_material, technique, clarified_technique, object_size, \
    clarified_size, weight, clarified_weight, reason, object_input_date, execute_restorer, object_output_date, \
    responsible_restorer, origin_description, appearance_description, damages_description, signs_description, \
    size_description, purposes_researches, methods_researches, executor_date_researches, results_researches, \
    restoration_program, treatments_descriptions, treatments_chemicals, treatments_executor_date, \
    treatments_results = dbase.get_passport(id_post)

    if request.method == 'POST':
        if len(request.form['inventory_number']) > 0 and len(request.form['acceptance_number']) > 0:

            dbase.store_passport(request.form['passport_number'],
                                 request.form['inventory_number'],
                                 request.form['acceptance_number'],
                                 request.form['institution_name'],
                                 request.form['department_name'],
                                 request.form['definition'],
                                 request.form['typological'],
                                 request.form['object_owner'],
                                 request.form['author'],
                                 request.form['clarified_author'],
                                 request.form['object_name'],
                                 request.form['clarified_object_name'],
                                 request.form['time_of_creation'],
                                 request.form['clarified_time_of_creation'],
                                 request.form['material'],
                                 request.form['clarified_material'],
                                 request.form['technique'],
                                 request.form['clarified_technique'],
                                 request.form['object_size'],
                                 request.form['clarified_size'],
                                 request.form['weight'],
                                 request.form['clarified_weight'],
                                 request.form['reason'],
                                 request.form['object_input_date'],
                                 request.form['execute_restorer'],
                                 request.form['object_output_date'],
                                 request.form['responsible_restorer'],
                                 request.form['origin_description'],
                                 request.form['appearance_description'],
                                 request.form['damages_description'],
                                 request.form['signs_description'],
                                 request.form['size_description'],
                                 request.form['purposes_researches'],
                                 request.form['methods_researches'],
                                 request.form['executor_date_researches'],
                                 request.form['results_researches'],
                                 request.form['restoration_program'],
                                 request.form['treatments_descriptions'],
                                 request.form['treatments_chemicals'],
                                 request.form['treatments_executor_date'],
                                 request.form['treatments_results'],
                                 current_restorer_id)

            flash('Успішно опубліковано!', category='success')
            return redirect(url_for('portfolio'), code=301)

        else:
            flash("Спочатку введіть, будь ласка, інвентарний номер та дані акта приймання пам'ятки.", category='error')

    return render_template('update_passport.html', main_menu=dbase.get_main_menu(), web_page_title='Публікація',
                           passport=dbase.get_current_passport_id(id_post), passport_number=passport_number,
                           inventory_number=inventory_number, acceptance_number=acceptance_number,
                           institution_name=institution_name,
                           department_name=department_name, definition=definition, typological=typological,
                           object_owner=object_owner, author=author, clarified_author=clarified_author,
                           object_name=object_name,
                           clarified_object_name=clarified_object_name, time_of_creation=time_of_creation,
                           clarified_time_of_creation=clarified_time_of_creation, material=material,
                           clarified_material=clarified_material,
                           technique=technique, clarified_technique=clarified_technique, object_size=object_size,
                           clarified_size=clarified_size,
                           weight=weight, clarified_weight=clarified_weight, reason=reason,
                           object_input_date=object_input_date, execute_restorer=execute_restorer,
                           object_output_date=object_output_date, responsible_restorer=responsible_restorer,
                           origin_description=origin_description, appearance_description=appearance_description,
                           damages_description=damages_description, signs_description=signs_description,
                           size_description=size_description, purposes_researches=purposes_researches,
                           methods_researches=methods_researches, executor_date_researches=executor_date_researches,
                           results_researches=results_researches, restoration_program=restoration_program,
                           treatments_descriptions=treatments_descriptions, treatments_chemicals=treatments_chemicals,
                           treatments_executor_date=treatments_executor_date, treatments_results=treatments_results)


@app.route('/delete_passport/<string:id_post>')
@login_required
def delete_passport(id_post):
    db = get_db()
    dbase = DataBase(db)

    passport_number, inventory_number, acceptance_number, institution_name, department_name, definition, typological, \
    object_owner, author, clarified_author, object_name, clarified_object_name, time_of_creation, \
    clarified_time_of_creation, material, clarified_material, technique, clarified_technique, object_size, \
    clarified_size, weight, clarified_weight, reason, object_input_date, execute_restorer, object_output_date, \
    responsible_restorer, origin_description, appearance_description, damages_description, signs_description, \
    size_description, purposes_researches, methods_researches, executor_date_researches, results_researches, \
    restoration_program, treatments_descriptions, treatments_chemicals, treatments_executor_date, \
    treatments_results = dbase.get_passport(id_post)

    return render_template('delete_passport.html', main_menu=dbase.get_main_menu(), web_page_title='Видалення',
                           passport=dbase.get_current_passport_deletion_warning_data(id_post),
                           passport_number=passport_number,
                           inventory_number=inventory_number, acceptance_number=acceptance_number,
                           institution_name=institution_name,
                           department_name=department_name, definition=definition, typological=typological,
                           object_owner=object_owner, author=author, clarified_author=clarified_author,
                           object_name=object_name,
                           clarified_object_name=clarified_object_name, time_of_creation=time_of_creation,
                           clarified_time_of_creation=clarified_time_of_creation, material=material,
                           clarified_material=clarified_material,
                           technique=technique, clarified_technique=clarified_technique, object_size=object_size,
                           clarified_size=clarified_size,
                           weight=weight, clarified_weight=clarified_weight, reason=reason,
                           object_input_date=object_input_date, execute_restorer=execute_restorer,
                           object_output_date=object_output_date, responsible_restorer=responsible_restorer,
                           origin_description=origin_description, appearance_description=appearance_description,
                           damages_description=damages_description, signs_description=signs_description,
                           size_description=size_description, purposes_researches=purposes_researches,
                           methods_researches=methods_researches, executor_date_researches=executor_date_researches,
                           results_researches=results_researches, restoration_program=restoration_program,
                           treatments_descriptions=treatments_descriptions, treatments_chemicals=treatments_chemicals,
                           treatments_executor_date=treatments_executor_date, treatments_results=treatments_results)


@app.route('/deleted_passport_report/<string:id_post>')
@login_required
def deleted_passport_report(id_post):
    db = get_db()
    dbase = DataBase(db)
    dbase.delete_passport(id_post)
    return render_template('deleted_passport_report.html', main_menu=dbase.get_main_menu(),
                           web_page_title='Публікацію видалено')


@app.route('/download_passport')
@login_required
def download_passport():
    printable_passport = 'filled_passport.docx'
    return send_file(printable_passport, as_attachment=True, download_name='YourFilledPassport.docx')


@app.route('/login', methods=['POST', 'GET'])
def login():
    db = get_db()
    dbase = DataBase(db)
    if current_user.is_authenticated:
        return redirect(url_for('cabinet'))

    if request.method == 'POST':
        restorer_email = request.form['restorer_email']
        restorer_password_from_login = request.form['restorer_password']

        restorer = dbase.get_restorer_by_email(restorer_email)
        hashed_restorer_password_from_data_base = restorer['hashed_restorer_password']

        checked_password = check_password_hash(hashed_restorer_password_from_data_base, restorer_password_from_login)
        if restorer and checked_password:
            restorer_login = RestorerLogin().create(restorer)
            restorer_remembered = True if request.form.get('remember_restorer') else False
            login_user(restorer_login, remember=restorer_remembered)
            return redirect(url_for('cabinet'))

        flash('Будь ласка, перевірте введену електронну адресу та пароль і спробуйте ще', 'error')

    return render_template('login.html', main_menu=dbase.get_main_menu(), web_page_title='Увійти в кабінет')


@app.route('/register', methods=['POST', 'GET'])
def register():
    db = get_db()
    dbase = DataBase(db)
    if request.method == 'POST':
        if len(request.form['restorer_name']) > 0 and len(request.form['restorer_email']) > 0 \
                and len(request.form['restorer_password']) == 4 \
                and request.form['restorer_password'] == request.form['repeated_restorer_password']:

            hashed_restorer_password = generate_password_hash(request.form['restorer_password'])
            result = dbase.add_restorer(request.form['restorer_name'], request.form['restorer_email'],
                                        hashed_restorer_password)
            if result:
                flash('Вітаємо, ви створили свій кабінет!', category='success')
                return redirect(url_for('cabinet'), code=301)
            else:
                flash('Будь ласка, перевірте введені дані і спробуйте ще', category='error')
        else:
            flash('Будь ласка, перевірте коректність введених даних і спробуйте ще', category='error')
    return render_template('register.html', main_menu=dbase.get_main_menu(), web_page_title='Створення кабінета')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Ви вийшли з кабінету', 'success')
    return redirect(url_for('login'))


@app.route('/cabinet')
@login_required
def cabinet():
    db = get_db()
    dbase = DataBase(db)
    return render_template('cabinet.html', main_menu=dbase.get_main_menu(), web_page_title='Кабінет',
                           current_restorer_id=current_user.get_id(), current_restorer_name=current_user.get_name())


@app.route('/about_us')
def about_us():
    print(url_for('about_us'))
    db = get_db()
    dbase = DataBase(db)
    return render_template('about.html', main_menu=dbase.get_main_menu(), web_page_title='Про нас')


@app.route('/experiences')
@login_required
def experiences():
    print(url_for('experiences'))
    db = get_db()
    dbase = DataBase(db)
    current_restorer_id = current_user.get_id()

    return render_template('experiences.html', main_menu=dbase.get_main_menu(), web_page_title='Досвід',
                           experiences=dbase.get_experiences_preview(current_restorer_id),
                           experiences_2=dbase.get_experiences_preview_2(current_restorer_id),
                           experiences_3=dbase.get_experiences_preview_3(current_restorer_id))


@app.route('/add_experience', methods=['POST', 'GET'])
def add_experience():
    print(url_for('add_experience'))
    db = get_db()
    dbase = DataBase(db)
    author_of_experience_id = current_user.get_id()

    experiences_amount = dbase.count_experiences_preview(author_of_experience_id)
    experiences_amount_2 = dbase.count_experiences_preview_2(author_of_experience_id)
    experiences_amount_3 = dbase.count_experiences_preview_3(author_of_experience_id)

    if experiences_amount != 'empty' and experiences_amount_2 != 'empty' and experiences_amount_3 != 'empty':
        flash('Ви додали максимальну кількість досвіду. Видаліть один досвід для публікування.', category='error')
        return redirect(url_for('experiences'), code=301)

    if request.method == 'POST':
        if experiences_amount == 'empty':
            if len(request.form['experienced_material']) > 0:

                dbase.store_experience(request.form['experienced_material'],
                                       request.form['experienced_description'],
                                       request.form['experienced_damages_description'],
                                       request.form['experienced_research_title'],
                                       request.form['experienced_research_description'],
                                       request.form['experienced_restoration_program'],
                                       request.form['experienced_treatments_descriptions'],
                                       request.form['experienced_treatments_chemicals'],
                                       author_of_experience_id)

                flash('Успішно опубліковано!', category='success')
                return redirect(url_for('cabinet'), code=301)

            else:
                flash('Введіть назву матеріалу, будь ласка', category='error')

        if experiences_amount != 'empty' and experiences_amount_2 == 'empty':
            if len(request.form['experienced_material']) > 0:

                dbase.store_experience_2(request.form['experienced_material'],
                                         request.form['experienced_description'],
                                         request.form['experienced_damages_description'],
                                         request.form['experienced_research_title'],
                                         request.form['experienced_research_description'],
                                         request.form['experienced_restoration_program'],
                                         request.form['experienced_treatments_descriptions'],
                                         request.form['experienced_treatments_chemicals'],
                                         author_of_experience_id)

                flash('Успішно опубліковано!', category='success')
                return redirect(url_for('cabinet'), code=301)

            else:
                flash('Введіть назву матеріалу, будь ласка', category='error')

        if experiences_amount != 'empty' and experiences_amount_2 != 'empty' and experiences_amount_3 == 'empty':
            if len(request.form['experienced_material']) > 0:

                dbase.store_experience_3(request.form['experienced_material'],
                                         request.form['experienced_description'],
                                         request.form['experienced_damages_description'],
                                         request.form['experienced_research_title'],
                                         request.form['experienced_research_description'],
                                         request.form['experienced_restoration_program'],
                                         request.form['experienced_treatments_descriptions'],
                                         request.form['experienced_treatments_chemicals'],
                                         author_of_experience_id)

                flash('Успішно опубліковано!', category='success')
                return redirect(url_for('cabinet'), code=301)

            else:
                flash('Введіть назву матеріалу, будь ласка', category='error')

    return render_template('add_experience.html', main_menu=dbase.get_main_menu(), web_page_title='Додати досвід')


@app.route('/update_experience/<string:id_post>', methods=['POST', 'GET'])
@login_required
def update_experience(id_post):
    db = get_db()
    dbase = DataBase(db)
    author_of_experience_id = current_user.get_id()

    experienced_material, experienced_description, experienced_damages_description, experienced_research_title, \
    experienced_research_description, experienced_restoration_program, experienced_treatments_descriptions, \
    experienced_treatments_chemicals = dbase.get_experience_to_update(id_post)

    if request.method == 'POST':
        if len(request.form['experienced_material']) > 0:
            dbase.delete_experience(id_post)

            dbase.store_experience(request.form['experienced_material'],
                                   request.form['experienced_description'],
                                   request.form['experienced_damages_description'],
                                   request.form['experienced_research_title'],
                                   request.form['experienced_research_description'],
                                   request.form['experienced_restoration_program'],
                                   request.form['experienced_treatments_descriptions'],
                                   request.form['experienced_treatments_chemicals'],
                                   author_of_experience_id)

            flash('Успішно опубліковано!', category='success')
            return redirect(url_for('experiences'), code=301)

    return render_template('update_experience.html', main_menu=dbase.get_main_menu(),
                           web_page_title=experienced_material,
                           experience_number='update_experience',
                           experience=dbase.get_current_experience_id(id_post),
                           experienced_material=experienced_material,
                           experienced_description=experienced_description,
                           experienced_damages_description=experienced_damages_description,
                           experienced_research_title=experienced_research_title,
                           experienced_research_description=experienced_research_description,
                           experienced_restoration_program=experienced_restoration_program,
                           experienced_treatments_descriptions=experienced_treatments_descriptions,
                           experienced_treatments_chemicals=experienced_treatments_chemicals)


@app.route('/update_experience_2/<string:id_post>', methods=['POST', 'GET'])
@login_required
def update_experience_2(id_post):
    db = get_db()
    dbase = DataBase(db)
    author_of_experience_id = current_user.get_id()

    experienced_material_2, experienced_description_2, experienced_damages_description_2, experienced_research_title_2,\
    experienced_research_description_2, experienced_restoration_program_2, experienced_treatments_descriptions_2, \
    experienced_treatments_chemicals_2 = dbase.get_experience_to_update_2(id_post)

    if request.method == 'POST':
        if len(request.form['experienced_material']) > 0:

            dbase.delete_experience_2(id_post)

            dbase.store_experience_2(request.form['experienced_material'],
                                     request.form['experienced_description'],
                                     request.form['experienced_damages_description'],
                                     request.form['experienced_research_title'],
                                     request.form['experienced_research_description'],
                                     request.form['experienced_restoration_program'],
                                     request.form['experienced_treatments_descriptions'],
                                     request.form['experienced_treatments_chemicals'],
                                     author_of_experience_id)

            flash('Успішно опубліковано!', category='success')
            return redirect(url_for('experiences'), code=301)

    return render_template('update_experience.html', main_menu=dbase.get_main_menu(),
                           web_page_title=experienced_material_2,
                           experience_number='update_experience_2',
                           experience=dbase.get_current_experience_id_2(id_post),
                           experienced_material=experienced_material_2,
                           experienced_description=experienced_description_2,
                           experienced_damages_description=experienced_damages_description_2,
                           experienced_research_title=experienced_research_title_2,
                           experienced_research_description=experienced_research_description_2,
                           experienced_restoration_program=experienced_restoration_program_2,
                           experienced_treatments_descriptions=experienced_treatments_descriptions_2,
                           experienced_treatments_chemicals=experienced_treatments_chemicals_2)


@app.route('/update_experience_3/<string:id_post>', methods=['POST', 'GET'])
@login_required
def update_experience_3(id_post):
    db = get_db()
    dbase = DataBase(db)
    author_of_experience_id = current_user.get_id()

    experienced_material_3, experienced_description_3, experienced_damages_description_3, experienced_research_title_3,\
    experienced_research_description_3, experienced_restoration_program_3, experienced_treatments_descriptions_3, \
    experienced_treatments_chemicals_3 = dbase.get_experience_to_update_3(id_post)

    if request.method == 'POST':
        if len(request.form['experienced_material']) > 0:

            dbase.delete_experience_3(id_post)

            dbase.store_experience_3(request.form['experienced_material'],
                                     request.form['experienced_description'],
                                     request.form['experienced_damages_description'],
                                     request.form['experienced_research_title'],
                                     request.form['experienced_research_description'],
                                     request.form['experienced_restoration_program'],
                                     request.form['experienced_treatments_descriptions'],
                                     request.form['experienced_treatments_chemicals'],
                                     author_of_experience_id)

            flash('Успішно опубліковано!', category='success')
            return redirect(url_for('experiences'), code=301)

    return render_template('update_experience.html', main_menu=dbase.get_main_menu(),
                           web_page_title=experienced_material_3,
                           experience_number='update_experience_3',
                           experience=dbase.get_current_experience_id_3(id_post),
                           experienced_material=experienced_material_3,
                           experienced_description=experienced_description_3,
                           experienced_damages_description=experienced_damages_description_3,
                           experienced_research_title=experienced_research_title_3,
                           experienced_research_description=experienced_research_description_3,
                           experienced_restoration_program=experienced_restoration_program_3,
                           experienced_treatments_descriptions=experienced_treatments_descriptions_3,
                           experienced_treatments_chemicals=experienced_treatments_chemicals_3)


@app.route('/delete_experience/<string:id_post>')
@login_required
def delete_experience(id_post):
    db = get_db()
    dbase = DataBase(db)

    experienced_material, experienced_description, experienced_damages_description, experienced_research_title, \
    experienced_research_description, experienced_restoration_program, experienced_treatments_descriptions, \
    experienced_treatments_chemicals = dbase.get_experience_to_show(id_post)

    return render_template('delete_experience.html', main_menu=dbase.get_main_menu(), web_page_title='Видалення',
                           experience=dbase.get_current_experience_deletion_warning_data(id_post),
                           experienced_material=experienced_material)


@app.route('/delete_experience_2/<string:id_post>')
@login_required
def delete_experience_2(id_post):
    db = get_db()
    dbase = DataBase(db)

    experienced_material_2, experienced_description_2, experienced_damages_description_2, experienced_research_title_2,\
    experienced_research_description_2, experienced_restoration_program_2, experienced_treatments_descriptions_2, \
    experienced_treatments_chemicals_2 = dbase.get_experience_to_show_2(id_post)

    return render_template('delete_experience.html', main_menu=dbase.get_main_menu(), web_page_title='Видалення',
                           experience=dbase.get_current_experience_deletion_warning_data_2(id_post),
                           experienced_material=experienced_material_2)


@app.route('/delete_experience_3/<string:id_post>')
@login_required
def delete_experience_3(id_post):
    db = get_db()
    dbase = DataBase(db)

    experienced_material_3, experienced_description_3, experienced_damages_description_3, experienced_research_title_3,\
    experienced_research_description_3, experienced_restoration_program_3, experienced_treatments_descriptions_3, \
    experienced_treatments_chemicals_3 = dbase.get_experience_to_show_3(id_post)

    return render_template('delete_experience.html', main_menu=dbase.get_main_menu(), web_page_title='Видалення',
                           experience=dbase.get_current_experience_deletion_warning_data_3(id_post),
                           experienced_material=experienced_material_3,
                           experienced_description=experienced_description_3,
                           experienced_damages_description=experienced_damages_description_3,
                           experienced_research_title=experienced_research_title_3,
                           experienced_research_description=experienced_research_description_3,
                           experienced_restoration_program=experienced_restoration_program_3,
                           experienced_treatments_descriptions=experienced_treatments_descriptions_3,
                           experienced_treatments_chemicals=experienced_treatments_chemicals_3)


@app.route('/deleted_experience_report/<string:id_post>')
@login_required
def deleted_experience_report(id_post):
    db = get_db()
    dbase = DataBase(db)
    dbase.delete_experience(id_post)
    return render_template('deleted_experience_report.html', main_menu=dbase.get_main_menu(),
                           web_page_title='Досвід видалено')


@app.route('/deleted_experience_report_2/<string:id_post>')
@login_required
def deleted_experience_report_2(id_post):
    db = get_db()
    dbase = DataBase(db)
    dbase.delete_experience_2(id_post)
    return render_template('deleted_experience_report.html', main_menu=dbase.get_main_menu(),
                           web_page_title='Досвід видалено')


@app.route('/deleted_experience_report_3/<string:id_post>')
@login_required
def deleted_experience_report_3(id_post):
    db = get_db()
    dbase = DataBase(db)
    dbase.delete_experience_3(id_post)
    return render_template('deleted_experience_report.html', main_menu=dbase.get_main_menu(),
                           web_page_title='Досвід видалено')


@app.errorhandler(404)
def page_not_found(error):
    db = get_db()
    dbase = DataBase(db)
    return render_template('page404.html', main_menu=dbase.get_main_menu(), web_page_title='Не знайдено'), 404


@app.errorhandler(500)
def internal_server_error(error):
    db = get_db()
    dbase = DataBase(db)
    return render_template('page500.html', main_menu=dbase.get_main_menu(), web_page_title='Проблема'), 500


if __name__ == '__main__':
    app.run(debug=True)
