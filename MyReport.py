# 10
import sqlite3
import os
from flask import Flask, render_template, url_for, request, flash, session, redirect, abort, g
from FDataBase import FDataBase
from heritageLogic import ReportTreatment
from heritageLogic import GeneralHeritageDescription, Materials
import jyserver.Flask as jsf

DATABASE = '/tmp/flsite.db'
DEBUG = True
SECRET_KEY = 'fdgdfgdfggf786hfg6hfg6h7f'
MAX_CONTENT_LENGTH = 1024 * 1024

app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(dict(DATABASE=os.path.join(app.root_path, 'flsite,db')))


@jsf.use(app)
class ChangeFormsForMaterial:
    def __init__(self, initial_changed_value='>>>', fillInExamples=GeneralHeritageDescription.AppearanceDescription(),
                 fillInCeramics=Materials.Ceramics(), fillInIron=Materials.Iron(), fillInCuprum=Materials.Cuprum(),
                 fillInSilver=Materials.Silver(), fillInWood=Materials.Wood(), fillInMetal=Materials.Metal()):
        # General texts for any heritage object
        self.changed_appearance_description = fillInExamples.general_appearance_description
        self.changed_damages_description = fillInExamples.general_damages_description
        self.changed_ConductTitle, self.changed_ConductDescription, self.changed_restoration_program, \
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
        self.ironConductTitle = fillInIron.iron_research_titles
        self.ironConductDescription = fillInIron.iron_research_descriptions
        self.restoration_program_iron = fillInIron.iron_restoration_program
        self.iron_treatments_descriptions = fillInIron.iron_treatments_descriptions
        self.iron_treatments_chemicals = fillInIron.iron_treatments_chemicals
        # Cuprum
        self.cuprumConductTitle = fillInCuprum.cuprum_research_titles
        self.cuprumConductDescription = fillInCuprum.cuprum_research_descriptions
        self.restoration_program_cuprum = fillInCuprum.cuprum_restoration_program
        self.cuprum_treatments_descriptions = fillInCuprum.cuprum_treatments_descriptions
        self.cuprum_treatments_chemicals = fillInCuprum.cuprum_treatments_chemicals
        # Silver
        self.silverConductTitle = fillInSilver.silver_research_titles
        self.silverConductDescription = fillInSilver.silver_research_descriptions
        self.restoration_program_silver = fillInSilver.silver_restoration_program
        self.silver_treatments_descriptions = fillInSilver.silver_treatments_descriptions
        self.silver_treatments_chemicals = fillInSilver.silver_treatments_chemicals

    def addCeramics(self):
        self.changed_appearance_description += self.ceramics_appearance_description
        self.js.document.getElementById("changed_appearance_description").innerHTML = self.changed_appearance_description
        self.changed_damages_description += self.ceramics_damage_description
        self.js.document.getElementById("changed_damages_description").innerHTML = self.changed_damages_description

    def addWood(self):
        self.changed_appearance_description += self.wood_appearance_description
        self.js.document.getElementById("changed_appearance_description").innerHTML = self.changed_appearance_description
        self.changed_damages_description += self.wood_damage_description
        self.js.document.getElementById("changed_damages_description").innerHTML = self.changed_damages_description

    def addMetal(self):
        self.changed_appearance_description += self.metal_appearance_description
        self.js.document.getElementById("changed_appearance_description").innerHTML = self.changed_appearance_description
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
        self.changed_ConductTitle += self.ironConductTitle
        self.js.document.getElementById("purposes_of_conduction").innerHTML = self.changed_ConductTitle
        self.changed_ConductDescription += self.ironConductDescription
        self.js.document.getElementById("methods_conduction").innerHTML = self.changed_ConductDescription
        self.changed_restoration_program += self.restoration_program_iron
        self.js.document.getElementById("restoration_program_by_material").innerHTML = self.changed_restoration_program
        self.changed_treatments_descriptions += self.iron_treatments_descriptions
        self.js.document.getElementById("treatments_descriptions_by_material").innerHTML = self.changed_treatments_descriptions
        self.changed_treatments_chemicals += self.iron_treatments_chemicals
        self.js.document.getElementById("treatments_chemicals_by_material").innerHTML = self.changed_treatments_chemicals

    def fillInCuprumForm(self):
        self.changed_ConductTitle += self.cuprumConductTitle
        self.js.document.getElementById("purposes_of_conduction").innerHTML = self.changed_ConductTitle
        self.changed_ConductDescription += self.cuprumConductDescription
        self.js.document.getElementById("methods_conduction").innerHTML = self.changed_ConductDescription
        self.changed_restoration_program += self.restoration_program_cuprum
        self.js.document.getElementById("restoration_program_by_material").innerHTML = self.changed_restoration_program
        self.changed_treatments_descriptions += self.cuprum_treatments_descriptions
        self.js.document.getElementById(
            "treatments_descriptions_by_material").innerHTML = self.changed_treatments_descriptions
        self.changed_treatments_chemicals += self.cuprum_treatments_chemicals
        self.js.document.getElementById(
            "treatments_chemicals_by_material").innerHTML = self.changed_treatments_chemicals

    def fillInSilverForm(self):
        self.changed_ConductTitle += self.silverConductTitle
        self.js.document.getElementById("purposes_of_conduction").innerHTML = self.changed_ConductTitle
        self.changed_ConductDescription += self.silverConductDescription
        self.js.document.getElementById("methods_conduction").innerHTML = self.changed_ConductDescription
        self.changed_restoration_program += self.restoration_program_silver
        self.js.document.getElementById("restoration_program_by_material").innerHTML = self.changed_restoration_program
        self.changed_treatments_descriptions += self.silver_treatments_descriptions
        self.js.document.getElementById(
            "treatments_descriptions_by_material").innerHTML = self.changed_treatments_descriptions
        self.changed_treatments_chemicals += self.silver_treatments_chemicals
        self.js.document.getElementById(
            "treatments_chemicals_by_material").innerHTML = self.changed_treatments_chemicals


def connect_db():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn


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
    dbase = FDataBase(db)
    print(url_for('index'))
    return render_template('index.html', menu=dbase.getMenu(), web_page_title='Головна', posts=dbase.getPostsAnonce())


@app.route('/add_post', methods=['POST', 'GET'])
def addPost():
    db = get_db()
    dbase = FDataBase(db)
    RestorerPassport = ReportTreatment.Passport()

    if request.method == 'POST':
        if len(request.form['name']) > 0 and len(request.form['post']) > 0:
            res = dbase.addPost(request.form['passport_number'], request.form['name'], request.form['post'],
                                request.form['institution_name'], request.form['department_name'],
                                request.form['definition'], request.form['typological'],
                                request.form['object_owner'], request.form['author'], request.form['clarified_author'],
                                request.form['object_title'],
                                request.form['clarified_object_title'], request.form['time_of_creation'],
                                request.form['clarified_time_of_creation'],
                                request.form['material'], request.form['clarified_material'], request.form['technique'],
                                request.form['clarified_technique'],
                                request.form['object_size'], request.form['clarified_size'], request.form['weight'],
                                request.form['clarified_weight'], request.form['reason'],
                                request.form['object_input_date'], request.form['execute_restorer'],
                                request.form['object_output_date'], request.form['responsible_restorer'],
                                request.form['origin_description'], request.form['appearance_description'],
                                request.form['damages_description'], request.form['signs_description'],
                                request.form['size_description'], request.form['purposes_researches'],
                                request.form['methods_researches'], request.form['executor_date_researches'],
                                request.form['results_researches'], request.form['restoration_program'],
                                request.form['treatments_descriptions'], request.form['treatments_chemicals'],
                                request.form['treatments_executor_date'], request.form['treatments_results'])
            if not res:
                flash('Виникла, помилка публікування', category='error')
            else:
                flash('Успішно опубліковано!', category='success')
        else:
            flash("Спочатку введіть, будь ласка, інвентарний номер та дані акта приймання пам'ятки.", category='error')
    return ChangeFormsForMaterial.render(
        render_template('add_post.html', menu=dbase.getMenu(), web_page_title='Публікація', ))


@app.route('/post/<int:id_post>')
def showPost(id_post):
    db = get_db()
    dbase = FDataBase(db)
    passport_number, title, post, institution_name, department_name, definition, typological, object_owner, author, clarified_author, object_title, clarified_object_title, time_of_creation, clarified_time_of_creation, material, clarified_material, technique, clarified_technique, object_size, clarified_size, weight, clarified_weight, reason, object_input_date, execute_restorer, object_output_date, responsible_restorer, origin_description, appearance_description, damages_description, signs_description, size_description, purposes_researches, methods_researches, executor_date_researches, results_researches, restoration_program, treatments_descriptions, treatments_chemicals, treatments_executor_date, treatments_results = dbase.getPost(
        id_post)
    if not title:
        abort(404)

    return render_template('post.html', menu=dbase.getMenu(), web_page_title=title, passport_number=passport_number,
                           title=title, post=post, institution_name=institution_name,
                           department_name=department_name, definition=definition, typological=typological,
                           object_owner=object_owner, author=author, clarified_author=clarified_author,
                           object_title=object_title,
                           clarified_object_title=clarified_object_title, time_of_creation=time_of_creation,
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


@app.route('/about_us')
def about_us():
    db = get_db()
    dbase = FDataBase(db)
    print(url_for('about_us'))
    return render_template('about.html', menu=dbase.getMenu(), web_page_title='Про нас')


@app.errorhandler(404)
def pageNotFound(error):
    db = get_db()
    dbase = FDataBase(db)
    return render_template('page404.html', menu=dbase.getMenu(), web_page_title='Не знайдено'), 404


@app.route('/contact', methods=['POST', 'GET'])
def contact():
    db = get_db()
    dbase = FDataBase(db)
    if request.method == 'POST':
        if len(request.form['user_name']) > 2:
            flash('Ваше повідомлення відправлено. Ми вдосконалюємося.', category='success')
        else:
            flash('На жаль, виникла помилка відправлення', category='error')

    return render_template('contact.html', menu=dbase.getMenu(), web_page_title='Повідомити')


if __name__ == '__main__':
    app.run(debug=True)
