CREATE TABLE IF NOT EXISTS main_menu (
id integer PRIMARY KEY AUTOINCREMENT,
menu_element TEXT NOT NULL,
url TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS passports (
id integer PRIMARY KEY AUTOINCREMENT,
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
object_title TEXT NOT NULL,
clarified_object_title TEXT NOT NULL,
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
before_restoration_image_description TEXT NOT NULL,
before_restoration_image_of_object BLOB NOT NULL,
process_restoration_image_description TEXT NOT NULL,
process_restoration_image_of_object BLOB NOT NULL,
after_restoration_image_description TEXT NOT NULL,
after_restoration_image_of_object BLOB NOT NULL,
time integer NOT NULL
);