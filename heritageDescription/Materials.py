class Iron:
    def __init__(self):
        self.iron_appearance_description = '''\n(ЗАЛІЗО):
1.Вказати спосіб виготовлення (лиття, кування, слюсарні роботи)\n'''
        self.iron_damage_description = '''\n(ЗАЛІЗО):
1. Визначити ступінь збереженості:
    -Гарна збереженість (новий метал, локальна корозія, загальне забруднення);
    -Задовільна збереженість (новий метал, загальне забруднення, суцільна корозія або благородна патина, декор добре читається, металеве ядро не мінералізоване,наявні потертості, незначна деформація)
    -Новий метал поганої збереженості (загальні пило-брудові нашарування, суцільна корозія, наявні локальні рецедивуючі продукти корозії, значна деформація, втрати).
    -Археологічний метал (наявний товстий шар корозійного нашарування, міжкристалітна корозія, крихкість, тріщини, втрати, крізна корозія. Декор читається погано, форми предмета та металеве ядро збережені)
    -Археологічний метал з частково мінералізованим металевим ядром (форма предмету читається погано, механічна міцність слабка, можливі руйнування, крізна корозія, наявна часткова мінералізація металевого ядра).
    -Археологічний метал з повністю мінералізованим металевим ядром (предмет перетворився на безформну масу, що складається з продуктів корозії і не має механічної міцності).\n'''
        self.iron_research_titles = '''Визначення заліза фізичним методом\n\n\n\n
Визначення продуктів корозії заліза методом світлової мікроскопії\n\n\n\n\n\n'''
        self.iron_research_descriptions = '''Для визначення заліза використовувався магніт.
Висновок:
Усі деталі предмета мають магнітні властивості та виготовлені з заліза

Під мікроскопом МБС-10 були виявлені продукти корозії заліза,
колір яких характерний для :
-оксидів заліза
-гідроксидів заліза
Висновок:
сплав на основі заліза\n\n'''
        self.iron_restoration_program = '''(ЗАЛІЗО)\n1.Видалити поверхневі забруднення
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


class Cuprum:
    def __init__(self):
        self.cuprum_appearance_description = '''\n(МІДЬ):
1.Вказати спосіб виготовлення (лиття, прокат, травлення, гравіювання, мідне покриття, паяння, слюсарні роботи)\n'''
        self.cuprum_damage_description = '''\n(МІДЬ):
1. Визначити ступінь збереженості:
    -Гарна збереженість (новий метал, локальна корозія, загальне забруднення, патина відсутня);
    -Задовільна збереженість (новий метал, загальне забруднення, суцільна корозія або благородна патина, декор добре читається, металеве ядро не мінералізоване,наявні потертості, незначна деформація)
    -Новий метал поганої збереженості (загальні пило-брудові нашарування, суцільна корозія, наявні локальні рецедивуючі продукти корозії, значна деформація, втрати).
    -Археологічний метал з повністю мінералізованим металевим ядром (предмет перетворився на безформну масу, що складається з продуктів корозії і не має механічної міцності).
2. Вказати характерні особливості патини:
    - Патина рівномірного темно-оливкового кольору;
    - Патина має локальні світлозелені плями та уражена активними продуктами корозії міді;
    - Патина не рівномірна з низькою механічною міцністю та має пошкодження. Наявні ураженя активними продуктами корозії міді у вигляді світло-зелених плям;\n'''
        self.cuprum_research_titles = '''Визначення металу мідного кольору\n\n\n\n\n\n\n\n\n\n\n\n\n\n
Визначення продуктів корозії міді методом світлової мікроскопії\n\n\n\n\n'''
        self.cuprum_research_descriptions = '''Метал мідного кольору визначено \nза допомогою 50% азотної кислоти. 
На очищену поверхню досліджуваного \nматеріалу було нанесено краплю \nрозчину азотної кислоти з водою в співвідношенні 1:1. 
Після початку реакції і \nгазовиділення краплю обережно \nпромокнули фільтрувальним папером. 
Папір було вміщено в пари аміаку, \nпісля чого пляма на папері \nзабарвилась у темно-блакитний \nколір.
Висновок:
сплав на основі міді.\n
Під мікроскопом МБС-10 були виявлені продукти корозії міді,
колір яких характерний для:
-вуглекислих солей міді.
Висновок:
сплав  на основі міді.\n\n'''
        self.cuprum_restoration_program = '''(МІДЬ)\n1.Видалити поверхневі забруднення
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


class Silver:
    def __init__(self):
        self.silver_appearance_description = '''\n(СРІБЛО):
1.Вказати спосіб виготовлення (лиття, інкрустація, зернь, плакетування, гаптування, срібне покриття, паяння)\n'''
        self.silver_damage_description = '''\n(СРІБЛО):
1. Визначити ступінь збереженості:
    -Гарна збереженість (новий метал, загальне забруднення);
    -Задовільна збереженість (новий метал, загальне забруднення, благородна патина, декор добре читається, наявні потертості)
2. Вказати характерні особливості патини:
    - Сульфідна плівка рівномірного темного кольору;
    - Предмет має локальні світлозелені плями та уражена активними продуктами корозії міді;
    - Наявні ураженя активними продуктами корозії міді у вигляді світло-зелених плям.\n'''
        self.silver_research_titles = '''Визначення металу на вміст срібла\n\n\n\n\n\n\n
Визначення продуктів корозії методом світлової мікроскопії\n\n\n\n\n\n
Визначення якості металу\n\n\n\n'''
        self.silver_research_descriptions = '''На очищену поверхню було нанесено \nкраплю "червоної пробірної \nкислоти",
через кілька секунд пляма \nзабарвилась у колір червоного \nбіхромату срібла.
Висновок:
сплав на основі срібла.\n
Під мікроскопом МБС-10 були виявлені продукти корозії міді,
колір яких характерний для:
-хлорної міді
-сульфідів срібла
Висновок:
сплав має вміст міді.\n
Апробація проводилась пробірним наглядом.
Висновок:
експонат відповідає пробі срібла 875.\n\n'''
        self.silver_restoration_program = '''(СРІБЛО)\nВидалити поверхневі забруднення
Видалити стійкі забруднення
Видалити продукти корозії
Видалити залишки олов’яного припою
Провести стабілізацію
Провести консервацію\n'''
        self.silver_treatments_descriptions = '''(СРІБЛО)\nВидалення поверхневих забруднень:
Проводили м'яким щетинним пензлем.\n
Видалення стійних забруднень:
Проводили в теплій проточній воді з використанням ПАР та м'якого щетинного пензля з подальшою просушкою при t-45°.\n
Видалення осередків рецидивуючої корозії міді:
Проводили механічно під мікроскопом МБС-10 з застосуванням компресів з розчином сульфамінової кислоти,
з послідуючим ретельним промиванням в дистильованій воді та просушкою(t-45°с);
продукти корозії срібла (сульфідну плівку) видаляли за допомогою щетинного пензля та розчину на основі тіосечовини 
з подальшою промивкою та просушкою при t-45°.\n
Видалення залишків олов’яного припою:
Проводили механічно під мікроскопом, не доходячи до авторської поверхні.
Для потоншення олов’яного припою використовували компреси з водним розчином соляної кислоти,
з послідуючою нейтралізацією розчином кальцинованої соди та ретельною промивкою дистильованою водою.\n
Проведення стабілізації:
Проводили шляхом нанесення розчину бензотриазолу на всю поверхню металу за допомогою ватних тампонів.\n
Проведення консервації:
Проводили шляхом нанесення синтетичного воску Cosmoloid H80
за допомогою пензля по всій поверхні предмета.\n'''
        self.silver_treatments_chemicals = '''(СРІБЛО)\n-\n\n\nПАР\n\n\n\nH3NSO3(Cульфамінова кислота)-3%;
CH4N2S(Тіосечовина)-80г;
H3PO4(Ортофосфорна кислота)-10г;
C2H5OH(Етанол)-60г;
Емульгатор-10г;
(дист.)-1000г.\n\n\n
HCl(Соляна кислота)водний розчин-60%;
Na2CO3(Кальцинована сода)водний розчин-1%.\n\n\n\n
C6H5N3(Бензотриазол)-1%;
C2H5OH-98%(Спирт етиловий-96%).\n\n
Cosmoloid H80;
Ацетон-97%.\n\n'''
