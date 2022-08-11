CREATE TABLE IF NOT EXISTS main_menu (
id INTEGER PRIMARY KEY AUTOINCREMENT,
menu_element TEXT NOT NULL,
url TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS passports (
id INTEGER PRIMARY KEY AUTOINCREMENT,
passport_number TEXT NOT NULL,
inventory_number TEXT NOT NULL,
acceptance_number TEXT NOT NULL,
institution_name TEXT NOT NULL,
department_name TEXT NOT NULL,
definition TEXT NOT NULL,
typological TEXT NOT NULL,
object_owner TEXT NOT NULL,
author TEXT NOT NULL,
clarified_author TEXT NOT NULL,
object_name TEXT NOT NULL,
clarified_object_name TEXT NOT NULL,
time_of_creation TEXT NOT NULL,
clarified_time_of_creation TEXT NOT NULL,
material TEXT NOT NULL,
clarified_material TEXT NOT NULL,
technique TEXT NOT NULL,
clarified_technique TEXT NOT NULL,
object_size TEXT NOT NULL,
clarified_size TEXT NOT NULL,
weight TEXT NOT NULL,
clarified_weight TEXT NOT NULL,
reason TEXT NOT NULL,
object_input_date TEXT NOT NULL,
execute_restorer TEXT NOT NULL,
object_output_date TEXT NOT NULL,
responsible_restorer TEXT NOT NULL,
origin_description TEXT NOT NULL,
appearance_description TEXT NOT NULL,
damages_description TEXT NOT NULL,
signs_description TEXT NOT NULL,
size_description TEXT NOT NULL,
purposes_researches TEXT NOT NULL,
methods_researches TEXT NOT NULL,
executor_date_researches TEXT NOT NULL,
results_researches TEXT NOT NULL,
restoration_program TEXT NOT NULL,
treatments_descriptions TEXT NOT NULL,
treatments_chemicals TEXT NOT NULL,
treatments_executor_date TEXT NOT NULL,
treatments_results TEXT NOT NULL,
author_of_passport_id TEXT NOT NULL,
TIME INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS restorers (
id INTEGER PRIMARY KEY AUTOINCREMENT,
restorer_name TEXT NOT NULL,
restorer_email TEXT NOT NULL,
hashed_restorer_password TEXT NOT NULL,
TIME INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS experience (
id INTEGER PRIMARY KEY AUTOINCREMENT,
experienced_material TEXT NOT NULL,
experienced_description TEXT NOT NULL,
experienced_damages_description TEXT NOT NULL,
experienced_research_title TEXT NOT NULL,
experienced_research_description TEXT NOT NULL,
experienced_restoration_program TEXT NOT NULL,
experienced_treatments_descriptions TEXT NOT NULL,
experienced_treatments_chemicals TEXT NOT NULL,
author_of_experience_id TEXT NOT NULL,
TIME INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS experience_2 (
id INTEGER PRIMARY KEY AUTOINCREMENT,
experienced_material_2 TEXT NOT NULL,
experienced_description_2 TEXT NOT NULL,
experienced_damages_description_2 TEXT NOT NULL,
experienced_research_title_2 TEXT NOT NULL,
experienced_research_description_2 TEXT NOT NULL,
experienced_restoration_program_2 TEXT NOT NULL,
experienced_treatments_descriptions_2 TEXT NOT NULL,
experienced_treatments_chemicals_2 TEXT NOT NULL,
author_of_experience_id TEXT NOT NULL,
TIME INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS experience_3 (
id INTEGER PRIMARY KEY AUTOINCREMENT,
experienced_material_3 TEXT NOT NULL,
experienced_description_3 TEXT NOT NULL,
experienced_damages_description_3 TEXT NOT NULL,
experienced_research_title_3 TEXT NOT NULL,
experienced_research_description_3 TEXT NOT NULL,
experienced_restoration_program_3 TEXT NOT NULL,
experienced_treatments_descriptions_3 TEXT NOT NULL,
experienced_treatments_chemicals_3 TEXT NOT NULL,
author_of_experience_id TEXT NOT NULL,
TIME INTEGER NOT NULL
);