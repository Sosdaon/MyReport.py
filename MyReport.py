import sqlite3
import os
from flask import Flask, render_template, url_for, request, flash, redirect, abort, g, send_file
from werkzeug.utils import secure_filename
from heritageLogic import GeneralHeritageDescription, Materials
from printable.PrintPassportPaper import Paperwork
import jyserver.Flask as jsf
from DataBase import DataBase

DATABASE = '/tmp/flsite.db'
DEBUG = True
SECRET_KEY = 'fdgdfgdfggf786hfg6hfg6h7f'
ALLOWED_EXTENSIONS = {'png'}
UPLOAD_FOLDER = 'C:/Users/ASUS/Desktop/pyCharm_projects/restoreConrol/static/Intelligible_illustrations'
MAX_CONTENT_LENGTH = 16 * 1000 * 1000
app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(dict(DATABASE=os.path.join(app.root_path, 'flsite,db')))


@jsf.use(app)
class ChangeFormsForMaterial:
    def __init__(self, initial_changed_value='', fillInExamples=GeneralHeritageDescription.AppearanceDescription(),
                 fillInCeramics=Materials.Ceramics(), fillInIron=Materials.Iron(), fillInCuprum=Materials.Cuprum(),
                 fillInSilver=Materials.Silver(), fillInWood=Materials.Wood(), fillInMetal=Materials.Metal()):
        # General texts for any heritage object
        self.changed_appearance_description = fillInExamples.general_appearance_description
        self.changed_damages_description = fillInExamples.general_damages_description
        self.changed_research_title, self.changed_research_description, self.changed_restoration_program, \
        self.changed_treatments_descriptions, self.changed_treatments_chemicals = initial_changed_value, \
                                                                                  initial_changed_value, initial_changed_value, initial_changed_value, initial_changed_value
        # Ceramics (wide material field)
        self.ceramics_appearance_description = fillInCeramics.ceramics_appearance_description
        self.ceramics_damage_description = fillInCeramics.ceramics_damage_description
        # Wood (wide material field)
        self.wood_appearance_description = fillInWood.wood_appearance_description
        self.wood_damage_description = fillInWood.wood_damage_description
        # Metal (wide material field)
        self.metal_appearance_description = fillInMetal.metal_appearance_description
        self.metal_damage_description = fillInMetal.metal_damage_description
        # Iron
        self.iron_research_title = fillInIron.iron_research_titles
        self.iron_research_description = fillInIron.iron_research_descriptions
        self.restoration_program_iron = fillInIron.iron_restoration_program
        self.iron_treatments_descriptions = fillInIron.iron_treatments_descriptions
        self.iron_treatments_chemicals = fillInIron.iron_treatments_chemicals
        # Cuprum
        self.cuprum_research_title = fillInCuprum.cuprum_research_titles
        self.cuprum_research_description = fillInCuprum.cuprum_research_descriptions
        self.restoration_program_cuprum = fillInCuprum.cuprum_restoration_program
        self.cuprum_treatments_descriptions = fillInCuprum.cuprum_treatments_descriptions
        self.cuprum_treatments_chemicals = fillInCuprum.cuprum_treatments_chemicals
        # Silver
        self.silver_research_title = fillInSilver.silver_research_titles
        self.silverConductDescription = fillInSilver.silver_research_descriptions
        self.restoration_program_silver = fillInSilver.silver_restoration_program
        self.silver_treatments_descriptions = fillInSilver.silver_treatments_descriptions
        self.silver_treatments_chemicals = fillInSilver.silver_treatments_chemicals

    def addCeramics(self):
        self.changed_appearance_description += self.ceramics_appearance_description
        self.js.document.getElementById(
            "changed_appearance_description").innerHTML = self.changed_appearance_description
        self.changed_damages_description += self.ceramics_damage_description
        self.js.document.getElementById("changed_damages_description").innerHTML = self.changed_damages_description

    def addWood(self):
        self.changed_appearance_description += self.wood_appearance_description
        self.js.document.getElementById(
            "changed_appearance_description").innerHTML = self.changed_appearance_description
        self.changed_damages_description += self.wood_damage_description
        self.js.document.getElementById("changed_damages_description").innerHTML = self.changed_damages_description

    def addMetal(self):
        self.changed_appearance_description += self.metal_appearance_description
        self.js.document.getElementById(
            "changed_appearance_description").innerHTML = self.changed_appearance_description
        self.changed_damages_description += self.metal_damage_description
        self.js.document.getElementById("changed_damages_description").innerHTML = self.changed_damages_description

    def hideMetalResearches(self):
        self.js.document.getElementById("choose_iron_cunduct").style.visibility = 'hidden'
        self.js.document.getElementById("choose_cuprum_cunduct").style.visibility = 'hidden'
        self.js.document.getElementById("choose_silver_cunduct").style.visibility = 'hidden'

    def showMetalResearches(self):
        self.js.document.getElementById("choose_iron_cunduct").style.visibility = 'visible'
        self.js.document.getElementById("choose_cuprum_cunduct").style.visibility = 'visible'
        self.js.document.getElementById("choose_silver_cunduct").style.visibility = 'visible'

    def fillInIronForm(self):
        self.changed_research_title += self.iron_research_title
        self.js.document.getElementById("purposes_of_conduction").innerHTML = self.changed_research_title
        self.changed_research_description += self.iron_research_description
        self.js.document.getElementById("methods_conduction").innerHTML = self.changed_research_description
        self.changed_restoration_program += self.restoration_program_iron
        self.js.document.getElementById("restoration_program_by_material").innerHTML = self.changed_restoration_program
        self.changed_treatments_descriptions += self.iron_treatments_descriptions
        self.js.document.getElementById(
            "treatments_descriptions_by_material").innerHTML = self.changed_treatments_descriptions
        self.changed_treatments_chemicals += self.iron_treatments_chemicals
        self.js.document.getElementById(
            "treatments_chemicals_by_material").innerHTML = self.changed_treatments_chemicals

    def fillInCuprumForm(self):
        self.changed_research_title += self.cuprum_research_title
        self.js.document.getElementById("purposes_of_conduction").innerHTML = self.changed_research_title
        self.changed_research_description += self.cuprum_research_description
        self.js.document.getElementById("methods_conduction").innerHTML = self.changed_research_description
        self.changed_restoration_program += self.restoration_program_cuprum
        self.js.document.getElementById("restoration_program_by_material").innerHTML = self.changed_restoration_program
        self.changed_treatments_descriptions += self.cuprum_treatments_descriptions
        self.js.document.getElementById(
            "treatments_descriptions_by_material").innerHTML = self.changed_treatments_descriptions
        self.changed_treatments_chemicals += self.cuprum_treatments_chemicals
        self.js.document.getElementById(
            "treatments_chemicals_by_material").innerHTML = self.changed_treatments_chemicals

    def fillInSilverForm(self):
        self.changed_research_title += self.silver_research_title
        self.js.document.getElementById("purposes_of_conduction").innerHTML = self.changed_research_title
        self.changed_research_description += self.silverConductDescription
        self.js.document.getElementById("methods_conduction").innerHTML = self.changed_research_description
        self.changed_restoration_program += self.restoration_program_silver
        self.js.document.getElementById("restoration_program_by_material").innerHTML = self.changed_restoration_program
        self.changed_treatments_descriptions += self.silver_treatments_descriptions
        self.js.document.getElementById(
            "treatments_descriptions_by_material").innerHTML = self.changed_treatments_descriptions
        self.changed_treatments_chemicals += self.silver_treatments_chemicals
        self.js.document.getElementById(
            "treatments_chemicals_by_material").innerHTML = self.changed_treatments_chemicals


def connect_db():
    connection = sqlite3.connect(app.config['DATABASE'])
    connection.row_factory = sqlite3.Row
    return connection


def create_db():
    db = connect_db()
    with app.open_resource('sq_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


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
    db = get_db()
    dbase = DataBase(db)
    print(url_for('index'))
    return render_template('index.html', main_menu=dbase.getMainMenu(), web_page_title='Головна',
                           passports=dbase.get_passports_preview())


def set_name_to_image(image_name, image):
    image_name = str(image_name)
    image.filename = image_name
    displayable_image = secure_filename(image.filename)
    image.save(os.path.join(app.config['UPLOAD_FOLDER'], displayable_image))


@app.route('/add_passport', methods=['POST', 'GET'])
def add_passport():
    db = get_db()
    dbase = DataBase(db)
    print(url_for('add_passport'))

    if request.method == 'POST':
        if len(request.form['inventory_number']) > 0 and len(request.form['acceptance_number']) > 0:

            names_and_images = {
                request.form['before_restoration_image_description']: request.files[
                    'before_restoration_image_of_object'],
                request.form['process_restoration_image_description']: request.files[
                    'process_restoration_image_of_object'],
                request.form['after_restoration_image_description']: request.files['after_restoration_image_of_object']
            }
            try:
                for image_name, image in names_and_images.copy().items():
                    set_name_to_image(image_name, image)
            except FileNotFoundError:
                flash('Назвіть фото латиницею без використання спец. символів та злитно', category='error')
                return redirect('/add_passport')

            passport_fields_input = dbase.store_passport(request.form['passport_number'],
                                                         request.form['inventory_number'],
                                                         request.form['acceptance_number'],
                                                         request.form['institution_name'],
                                                         request.form['department_name'],
                                                         request.form['definition'], request.form['typological'],
                                                         request.form['object_owner'],
                                                         request.form['author'], request.form['clarified_author'],
                                                         request.form['object_name'],
                                                         request.form['clarified_object_name'],
                                                         request.form['time_of_creation'],
                                                         request.form['clarified_time_of_creation'],
                                                         request.form['material'], request.form['clarified_material'],
                                                         request.form['technique'],
                                                         request.form['clarified_technique'],
                                                         request.form['object_size'], request.form['clarified_size'],
                                                         request.form['weight'],
                                                         request.form['clarified_weight'], request.form['reason'],
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
                                                         request.form['before_restoration_image_description'],
                                                         request.files['before_restoration_image_of_object'],
                                                         request.form['process_restoration_image_description'],
                                                         request.files['process_restoration_image_of_object'],
                                                         request.form['after_restoration_image_description'],
                                                         request.files['after_restoration_image_of_object'])

            if not passport_fields_input:
                flash('Виникла, помилка публікування', category='error')
            else:
                flash('Успішно опубліковано!', category='success')
        else:
            flash("Спочатку введіть, будь ласка, інвентарний номер та дані акта приймання пам'ятки.", category='error')
    return ChangeFormsForMaterial.render(
        render_template('passport_form.html', main_menu=dbase.getMainMenu(), web_page_title='Публікація', ))


@app.route('/post/<int:id_post>')
def show_post(id_post):
    db = get_db()
    dbase = DataBase(db)
    passport = Paperwork()

    passport_number, inventory_number, acceptance_number, institution_name, department_name, definition, typological, object_owner, author, clarified_author, object_name, clarified_object_name, time_of_creation, clarified_time_of_creation, material, clarified_material, technique, clarified_technique, object_size, clarified_size, weight, clarified_weight, reason, object_input_date, execute_restorer, object_output_date, responsible_restorer, origin_description, appearance_description, damages_description, signs_description, size_description, purposes_researches, methods_researches, executor_date_researches, results_researches, restoration_program, treatments_descriptions, treatments_chemicals, treatments_executor_date, treatments_results, before_restoration_image_description, before_restoration_image_of_object, process_restoration_image_description, process_restoration_image_of_object, after_restoration_image_description, after_restoration_image_of_object = dbase.get_passport(
        id_post)

    passport.build_passport(passport_number, inventory_number, acceptance_number, institution_name, department_name,
                            definition, typological, object_owner, author, clarified_author, object_name,
                            clarified_object_name, time_of_creation, clarified_time_of_creation, material,
                            clarified_material, technique, clarified_technique, object_size, clarified_size, weight,
                            clarified_weight, reason, object_input_date, execute_restorer, object_output_date,
                            responsible_restorer, origin_description, appearance_description, damages_description,
                            signs_description, size_description, purposes_researches, methods_researches,
                            executor_date_researches, results_researches, restoration_program, treatments_descriptions,
                            treatments_chemicals, treatments_executor_date, treatments_results,
                            before_restoration_image_description, process_restoration_image_description,
                            after_restoration_image_description)

    if not inventory_number:
        abort(404)

    return render_template('post.html', main_menu=dbase.getMainMenu(), web_page_title=inventory_number,
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
                           treatments_executor_date=treatments_executor_date, treatments_results=treatments_results,
                           before_restoration_image_description=before_restoration_image_description,
                           before_restoration_image_of_object=before_restoration_image_of_object,
                           process_restoration_image_description=process_restoration_image_description,
                           process_restoration_image_of_object=process_restoration_image_of_object,
                           after_restoration_image_description=after_restoration_image_description,
                           after_restoration_image_of_object=after_restoration_image_of_object)


@app.route('/download_passport')
def download_passport():
    printable_passport = 'filled_passport.docx'
    return send_file(printable_passport, as_attachment=True, download_name='YourFilledPassport.docx')


@app.route('/about_us')
def about_us():
    db = get_db()
    dbase = DataBase(db)
    print(url_for('about_us'))
    return render_template('about.html', main_menu=dbase.getMainMenu(), web_page_title='Про нас')


@app.errorhandler(413)
def uploaded_image_too_large(error):
    db = get_db()
    dbase = DataBase(db)
    return render_template('page413.html', main_menu=dbase.getMainMenu(), web_page_title='Змініть зображення'), 413


@app.errorhandler(404)
def page_not_found(error):
    db = get_db()
    dbase = DataBase(db)
    return render_template('page404.html', main_menu=dbase.getMainMenu(), web_page_title='Не знайдено'), 404


if __name__ == '__main__':
    app.run(debug=True)
    app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
