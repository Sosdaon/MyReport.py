# 10
import sqlite3
import os
from flask import Flask, render_template, url_for, request, flash, session, redirect, abort, g
from FDataBase import FDataBase
from heritageLogic import ReportTreatment
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
    def __init__(self, material='Опис обраного матеріалу', damages='Пошкодження та втрати'):
#Iron
        self.changed_appearance_description = '''За візуальним спостереженням: ...
I. Візуальне дослідження (опис пам’ятки):
    1.Вказати назву (якщо є спеціальний термін).
    2.Описати форму та колір.
II. Описати вигляд предмета:
    1. Складові предмета, їх геометрична форма;
III. Забруднення:
    1.Нестійкі (пилові, брудові, ґрунтові) .
    2.Стійкі (вапнякові, природні та синтетичні смоли, висоли, гіпсові забруднення, плями кислів металів, сліди кіптяви,
        пеку, жиру, плями від пластиліну, масляної фарби, воску, клейові забруднення, чорнила, туш,
        записи фарбами (якого кольору), забруднення фарбами  від попередніх тонувань – місцезнаходження фарби,
        забруднення на зламах фрагментів (від клею, вапнякових нашарувань, пило брудові, ґрунтові і т.д.).
    3.Визначити за візуальним спостереженням яким клеєм склеєно фрагменти (клеєм БФ (світло-коричневого, коричневого, червоного кольору, прозорий),
        ПВА (полівінилацетатний клей молочного кольору, непрозорий, безбарвний, прозорий)
Визначити форму забруднення (у вигляді локальних плям, неправильної форми, повсюдно, забруднення якоїсь частини пам’ятки).
    Матеріали:'''
        self.changed_damages_description = '''ІV. Попередня реставрація:
    1. Якщо була – описати якість попередньої реставрації).
    2. Свідчення про попередню реставрацію (відсутні, якщо є вказати джерело чи з чиїх слів записано).
    3. Реставрація не повна якщо:
        -  фрагменти склеєні, а втрати не восповнені;
        -восповнені частково;
        -є втрати у будь-якій частині виробу (вказати місце втрати, форму, розмір).
V. Опис наявних втрат та пошкоджень:
    1. Вказати із якої кількості фрагментів складається пам’ятка.
    2. Вказати на якість попереднього склеювання, доповнення.
    3. Вказати які частини пам’ятки відсутні (вказати розмір в см/мм та кв. см/мм).
    4. Вказати пошкодження, відслоюваня, розшарування, деформації.
    5. Визначити дефекти:
        -привнесені від археологічного чи реставраційного інструменту, помітки олівцем і т.д.;
        -виробничі;
        -тріщини (наскрізні, не наскрізні, волосяні (вказати форму, розмір, розташування);
        -сколи, вибоїни, незначні втрати, каверни, пробоїни, викришування, потертості, подряпини (вказати форму, розмір, розташування);
        -визначити дефекти тонувань (якщо є розпис, консерваційного покриття – описати колір, стан збереження,
        наявні значні або незначні, часткові, локальні втрати, потертості відшарування (вказати форму, розмір, розташування);
VІ. Біологічні пошкодження і руйнування:
    6.Бактерії, гриби та продукти їх життєдіяльності.'''
        self.changed_ConductTitle = '=>'
        self.changed_ConductDescription = '->'
        self.changed_restoration_program = '}'
        self.changed_treatments_descriptions = '>'
        self.changed_treatments_chemicals = ')'
        self.ironConductTitle = '''Визначення заліза фізичним методом\n\n\n\n
Визначення продуктів корозії заліза методом світлової мікроскопії\n\n\n\n\n\n'''
        self.ironConductDescription = '''Для визначення заліза використовувався магніт.
Висновок:
Усі деталі предмета мають магнітні властивості та виготовлені з заліза

Під мікроскопом МБС-10 були виявлені продукти корозії заліза,
колір яких характерний для :
-оксидів заліза
-гідроксидів заліза
Висновок:
сплав на основі заліза\n\n'''
        self.restoration_program_iron = '''(ЗАЛІЗО)\n1.Видалити поверхневі забруднення
2.Видалити стійкі забруднення
3.Видалити продукти корозії
4.Виготовити втрачений елемент
5.Провести стабілізацію продуктів корозії
6.Провести консервацію\n'''
        self.iron_treatments_descriptions = '''(ЗАЛІЗО)\nВидалення поверхневих забруднень:
Проводили м'яким щетинним пензлем.\n
Видалення стійних забруднень:
Проводили тампонами змоченими в нафтовому розчиннику нефрас "Калоша".\n
Видалення продуктів корозії:
Проводили механічно, за допомогою скальпелю, бор машинки та з використанням спец. інструментів.\n
Виготовлення втраченого елементу:
Було виготовлено втрачений елемент в авторській техніці з заліза відповідно до аналогів.\n
Проведення стабілізації:
Нанесення розчину проводилося один раз. Після дії реагенту,
розчин було видалено за допомогою ватних тампонів змочених у розчині спирту.\n
Провести консервацію:
Проводили шляхом нанесення синтетичного воску Cosmoloid H80
за допомогою пензля по всій поверхні предмета.\n'''
        self.iron_treatments_chemicals = '''(ЗАЛІЗО)
-\n\n
Нефрас "Калоша".\n\n\n
-\n\n\n
-\n\n\n
Танін-20%;
C2H5OH-50%(Спирт етиловий-96%);
H2O-50%(дист.)\n\n
Cosmoloid H80;
Ацетон-97%.\n\n'''
#Cuprum
        self.cuprumConductTitle = '''Визначення металу мідного кольору\n\n\n\n\n\n\n\n\n\n\n\n\n\n
Визначення продуктів корозії міді методом світлової мікроскопії\n\n\n\n\n'''
        self.cuprumConductDescription = '''Метал мідного кольору визначено за допомогою 50% азотної кислоти.
На очищену поверхню досліджуваного матеріалу було нанесено краплю розчину азотної кислоти з водою в співвідношенні 1:1.
Після початку реакції і газовиділення крплю обережно промокнули фільтрувальним папером.
Папір було вміщено в пари аміаку, після чого пляма на папері забарвилась у темно-блакитний колір.
Висновок:
сплав на основі міді.\n
Під мікроскопом МБС-10 були виявлені продукти корозії міді,
колір яких характерний для:
-вуглекислих солей міді.
Висновок:
сплав  на основі міді.\n\n'''
        self.restoration_program_cuprum = '''(МІДЬ)\n1.Видалити поверхневі забруднення
2.Видалити стійкі забруднення
3.Видалити продукти корозії
4.Провести стабілізацію продуктів корозії
5.Провести консервацію\n'''
        self.cuprum_treatments_descriptions = '''(МІДЬ)\nВидалення поверхневих забруднень:
Проводили м'яким щетинним пензлем.\n
Видалення стійних забруднень:
Проводили тампонами змоченими в нафтовому розчиннику нефрас "Калоша".\n
Видалення продуктів корозії:
Проводили механічно, за допомогою скальпелю, бор машинки та з використанням спец. інструментів.\n
Проведення стабілізації:
Проводили шляхом нанесення розчину бензотриазолу на всю поверхню металу за допомогою щетинного пензля.\n
Проведення консервації:
Проводили шляхом нанесення синтетичного воску Cosmoloid H80
за допомогою пензля по всій поверхні предмета.\n'''
        self.cuprum_treatments_chemicals = '''(МІДЬ)
-\n\n
Нефрас "Калоша".\n\n\n
-\n\n\n
C6H5N3(Бензотриазол)-2%;
C2H5OH-98%(Спирт етиловий-96%).\n\n
Cosmoloid H80;
Ацетон-97%.\n\n'''
        self.material = material
        self.damages = damages

    def addOneMoreMaterialForm(self, material, damages):
        self.changed_appearance_description += material
        self.js.document.getElementById("changed_appearance_description").innerHTML = self.changed_appearance_description
        self.changed_damages_description += damages
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
        self.js.document.getElementById("treatments_descriptions_by_material").innerHTML = self.changed_treatments_descriptions
        self.changed_treatments_chemicals += self.cuprum_treatments_chemicals
        self.js.document.getElementById("treatments_chemicals_by_material").innerHTML = self.changed_treatments_chemicals

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
                                request.form['results_researches'],  request.form['restoration_program'],
                                request.form['treatments_descriptions'], request.form['treatments_chemicals'],
                                request.form['treatments_executor_date'], request.form['treatments_results'])
            if not res:
                flash('Виникла, помилка публікування', category='error')
            else:
                flash('Успішно опубліковано!', category='success')
        else:
            flash("Спочатку введіть, будь ласка, інвентарний номер та дані акта приймання пам'ятки.", category='error')
    return ChangeFormsForMaterial.render(render_template('add_post.html', menu=dbase.getMenu(), web_page_title='Публікація', ))


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
