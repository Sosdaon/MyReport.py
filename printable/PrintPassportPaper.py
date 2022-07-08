from docx import Document
from docx.shared import Inches
from docx.shared import Pt
from docx.enum.style import WD_STYLE_TYPE
import re
from heritageLogic.PassportPaperBlank import PassportPaperTitles


class Paperwork:
    def __init__(self, titles=PassportPaperTitles(), photos_amount='3', map_schemes_amount='',
                 additional_researches_amount='', other_related_materials_amount=''):
        self.passport_number_title = titles.passport_number
        self.inventory_number_title = titles.inventory_number
        self.acceptance_number_title = titles.acceptance_number
        self.ministry_title = titles.ministry
        self.passport_type_title = titles.passport_type
        self.institution_title = titles.institution
        self.department_title = titles.department
        self.typological_title = titles.typological
        self.definition_title = titles.definition
        self.fine_art_title = titles.fine_art
        self.applied_art_title = titles.applied_art
        self.archeological_title = titles.archeological
        self.documentary_title = titles.documentary
        self.other_object_title = titles.other_object
        self.object_owner_title = titles.object_owner
        self.attribution_data_from_acceptance_report_title = titles.attribution_data_from_acceptance_report
        self.clarification_title = titles.clarification
        self.author_title = titles.author
        self.object_name_title = titles.object_name
        self.time_of_creation_title = titles.time_of_creation
        self.material_title = titles.material
        self.technique_title = titles.technique
        self.object_size_title = titles.object_size
        self.weight_title = titles.weight
        self.reason_title = titles.reason
        self.dates_title = titles.dates
        self.restorers_title = titles.restorers
        self.object_input_date_title = titles.object_input_date
        self.execute_restorer_title = titles.execute_restorer
        self.object_output_date_title = titles.object_output_date
        self.responsible_restorer_title = titles.responsible_restorer
        self.origin_description_title = titles.origin_description
        self.condition_before_restoration_title = titles.condition_before_restoration
        self.appearance_description_title = titles.appearance_description
        self.damages_description_title = titles.damages_description
        self.signs_description_title = titles.signs_description
        self.size_description_title = titles.size_description
        self.researches_title = titles.researches
        self.purposes_researches_title = titles.purposes_researches
        self.methods_researches_title = titles.methods_researches
        self.executor_date_researches_title = titles.executor_date_researches
        self.results_researches_title = titles.results_researches
        self.restoration_program_title = titles.restoration_program
        self.sequence_of_treatments_title = titles.sequence_of_treatments
        self.program_approved_meeting_title = titles.program_approved_meeting
        self.approved_meeting_protocol_number_title = titles.approved_meeting_protocol_number
        self.appointed_responsible_restorer_title = titles.appointed_responsible_restorer
        self.meeting_secretary_title = titles.meeting_secretary
        self.reapproved_restoration_program_title = titles.reapproved_restoration_program
        self.reapproved_program_meeting_place_title = titles.reapproved_program_meeting_place
        self.reapproved_meeting_protocol_number_title = titles.reapproved_meeting_protocol_number
        self.treatments_title = titles.treatments
        self.treatments_descriptions_title = titles.treatments_descriptions
        self.treatments_chemicals_title = titles.treatments_chemicals
        self.treatments_executor_date_title = titles.treatments_executor_date
        self.treatments_results_title = titles.treatments_results
        self.responsible_restorer_signature_title = titles.responsible_restorer_signature
        self.signature_place = '_______________________________________'
        self.execute_restorer_signature_title = titles.execute_restorer_signature
        self.meeting_conclusion_title = titles.meeting_conclusion
        self.meeting_place_title = titles.meeting_place
        self.after_restoration_meeting_protocol_number_title = titles.after_restoration_meeting_protocol_number
        self.recommendations_title = titles.recommendations
        self.illustrative_material_title = titles.illustrative_material
        self.before_restoration_image_description_title = titles.before_restoration_image_description
        self.process_restoration_image_description_title = titles.process_restoration_image_description
        self.after_restoration_image_description_title = titles.after_restoration_image_description
        self.appendix_title = titles.appendix
        self.related_materials_title = titles.related_materials
        self.photos_title = titles.photos
        self.photos_amount = photos_amount
        self.units_title = "од."
        self.map_schemes_title = titles.map_schemes
        self.map_schemes_amount = map_schemes_amount
        self.additional_researches_results_title = titles.additional_researches_results
        self.additional_researches_amount = additional_researches_amount
        self.other_related_materials_title = titles.other_related_materials
        self.other_related_materials_amount = other_related_materials_amount
        self.attachment_illustrative_material_place_title = titles.attachment_illustrative_material_place
        self.object_transferred_place_title = titles.object_transferred_place
        self.responsible_treasurer_and_storage_place_title = titles.responsible_treasurer_and_storage_place
        self.give_back_report_title = titles.give_back_report
        self.passport_copies_transferred_place_title = titles.passport_copies_transferred_place
        self.head_of_institution_title = titles.head_of_institution
        self.head_of_the_department_title = titles.head_of_the_department
        self.head_of_restoration_title = titles.head_of_restoration
        self.executor_of_restoration_title = titles.executor_of_restoration
        self.restorers_and_other_executors_title = titles.restorers_and_other_executors
        self.empty_row_place = "___________________________________________________________________________"
        self.other_executors_signature_title = titles.other_executors_signature
        self.condition_check_date_title = titles.condition_check_date
        self.condition_description_title = titles.condition_description
        self.storage_condition_title = titles.storage_condition
        self.checking_person_signature_title = titles.checking_person_signature
        self.indent = '\n\n\n\n\n\n\n\n\n\n'

    def build_passport(self, passport_number, inventory_number, acceptance_number, institution_name, department_name,
                       definition, typological, object_owner, author, clarified_author, object_name,
                       clarified_object_name, time_of_creation, clarified_time_of_creation, material,
                       clarified_material, technique, clarified_technique, object_size, clarified_size, weight,
                       clarified_weight, reason,
                       object_input_date, execute_restorer, object_output_date, responsible_restorer,
                       origin_description, appearance_description, damages_description, signs_description,
                       size_description, purposes_researches, methods_researches, executor_date_researches,
                       results_researches, restoration_program, treatments_descriptions, treatments_chemicals,
                       treatments_executor_date, treatments_results, before_restoration_image_description,
                       process_restoration_image_description, after_restoration_image_description):

        document = Document()

        passport_identity_table = document.add_table(rows=1, cols=3)
        passport_identity_table.autofit = False
        passport_identity_table.allow_autofit = False
        passport_identity_table.columns[0].width = Inches(1.6)
        passport_identity_table.columns[1].width = Inches(1.4)
        passport_identity_table.columns[2].width = Inches(1.3)
        passport_identity_table.style = 'TableGrid'
        passport_identity_table.alignment = 2

        passport_identity_parameter = passport_identity_table.rows[0].cells
        passport_identity_parameter[0].text = f"{self.passport_number_title}{passport_number}"
        passport_identity_parameter[1].text = f"{self.inventory_number_title}{inventory_number}"
        passport_identity_parameter[2].text = f"{self.acceptance_number_title}{acceptance_number}"

        font_styles = document.styles
        font_charstyle = font_styles.add_style('CommentsStyle', WD_STYLE_TYPE.CHARACTER)
        font_object = font_charstyle.font
        font_object.name = 'Times New Roman'
        font_object.size = Pt(10)

        ministry_paragraph = document.add_paragraph()
        ministry_paragraph.add_run(f"{self.ministry_title}", style='CommentsStyle').bold = True
        ministry_paragraph.alignment = 1

        passport_type_paragraph = document.add_paragraph()
        passport_type_paragraph.add_run(f"{self.passport_type_title}", style='CommentsStyle').bold = True
        passport_type_paragraph.alignment = 1

        institution_paragraph = document.add_paragraph()
        institution_paragraph.add_run(f'{institution_name}', style='CommentsStyle').bold = True
        institution_paragraph.alignment = 1

        institution_parameter = document.add_paragraph()
        institution_parameter.add_run(f"{self.institution_title}")
        institution_parameter.alignment = 1

        department_paragraph = document.add_paragraph()
        department_paragraph.add_run(f'{department_name}', style='CommentsStyle').bold = True
        department_paragraph.alignment = 1

        department_parameter = document.add_paragraph()
        department_parameter.add_run(f'{self.department_title}')
        department_parameter.alignment = 1

        typological_paragraph = document.add_paragraph()
        typological_paragraph.add_run(f'{self.typological_title}').bold = True
        typological_paragraph.alignment = 0

        typological_table = document.add_table(rows=2, cols=6)
        typological_table.style = 'TableGrid'
        typological_table.alignment = 1

        typological_parameter = typological_table.rows[0].cells
        typological_parameter[0].text = f'{self.definition_title}'
        typological_parameter[1].text = f'{self.fine_art_title}'
        typological_parameter[2].text = f'{self.applied_art_title}'
        typological_parameter[3].text = f'{self.archeological_title}'
        typological_parameter[4].text = f'{self.documentary_title}'
        typological_parameter[5].text = f'{self.other_object_title}'

        typological_input = typological_table.rows[1].cells
        typological_input[0].text = f'{definition}'
        if typological == '(1)':
            typological_input[1].text = f'{typological}'
        elif typological == '(2)':
            typological_input[2].text = f'{typological}'
        elif typological == '(3)':
            typological_input[3].text = f'{typological}'
        elif typological == '(4)':
            typological_input[4].text = f'{typological}'
        elif typological == '(5)':
            typological_input[5].text = f'{typological}'
        else:
            typological_input[5].text = ''

        object_owner_paragraph = document.add_paragraph()
        object_owner_paragraph.add_run(f'{self.object_owner_title}').bold = True
        object_owner_paragraph.alignment = 1

        object_owner_input = document.add_paragraph()
        object_owner_input.add_run(f'{object_owner}')
        object_owner_input.alignment = 1

        attribution_data_table = document.add_table(rows=8, cols=2)
        attribution_data_table.style = 'TableGrid'
        attribution_data_table.alignment = 1

        attribution_data_parameter = attribution_data_table.rows[0].cells
        attribution_data_parameter[0].text = f'{self.attribution_data_from_acceptance_report_title}'
        attribution_data_parameter[1].text = f'{self.clarification_title}'

        author_parameter = attribution_data_table.rows[1].cells
        author_parameter[0].text = f'{self.author_title}{author}'
        author_parameter[1].text = f'{clarified_author}'

        object_name_parameter = attribution_data_table.rows[2].cells
        object_name_parameter[0].text = f'{self.object_name_title}{object_name}'
        object_name_parameter[1].text = f'{clarified_object_name}'

        time_of_creation_parameter = attribution_data_table.rows[3].cells
        time_of_creation_parameter[0].text = f'{self.time_of_creation_title}{time_of_creation}'
        time_of_creation_parameter[1].text = f'{clarified_time_of_creation}'

        material_parameter = attribution_data_table.rows[4].cells
        material_parameter[0].text = f'{self.material_title}{material}'
        material_parameter[1].text = f'{clarified_material}'

        technique_parameter = attribution_data_table.rows[5].cells
        technique_parameter[0].text = f'{self.technique_title}{technique}'
        technique_parameter[1].text = f'{clarified_technique}'

        object_size_parameter = attribution_data_table.rows[6].cells
        object_size_parameter[0].text = f'{self.object_size_title}{object_size}'
        object_size_parameter[1].text = f'{clarified_size}'

        weight_parameter = attribution_data_table.rows[7].cells
        weight_parameter[0].text = f'{self.weight_title }{weight}'
        weight_parameter[1].text = f'{clarified_weight}'

        reason_paragraph = document.add_paragraph()
        reason_paragraph.add_run(f'{self.reason_title}').bold = True
        reason_paragraph.alignment = 1

        reason_input = document.add_paragraph()
        reason = re.sub(r'<br>', '\n', reason)
        reason_input.add_run(f'{reason}')
        reason_input.paragraph_format.first_line_indent = Pt(18)
        reason_input.alignment = 0

        dates_and_restorers_table = document.add_table(rows=3, cols=2)
        dates_and_restorers_table.style = 'TableGrid'
        dates_and_restorers_table.alignment = 1

        dates_and_restorers_parameter = dates_and_restorers_table.rows[0].cells
        dates_and_restorers_parameter[0].text = f'{self.dates_title}'
        dates_and_restorers_parameter[1].text = f'{self.restorers_title}'

        dates_and_restorers_parameter = dates_and_restorers_table.rows[1].cells
        dates_and_restorers_parameter[0].text = f'{self.object_input_date_title}{object_input_date}'
        dates_and_restorers_parameter[1].text = f'{self.execute_restorer_title}{execute_restorer}'

        dates_and_restorers_parameter = dates_and_restorers_table.rows[2].cells
        dates_and_restorers_parameter[0].text = f'{self.object_output_date_title}{object_output_date}'
        dates_and_restorers_parameter[1].text = f'{self.responsible_restorer_title}{responsible_restorer}'

        document.add_page_break()

        origin_description_parameter = document.add_paragraph()
        origin_description_parameter.add_run(f'{self.origin_description_title}').bold = True
        origin_description_parameter.alignment = 0

        origin_description_input = document.add_paragraph()
        origin_description = re.sub(r'<br>', '\n', origin_description)
        origin_description_input.add_run(f'{origin_description}')
        origin_description_input.paragraph_format.first_line_indent = Pt(18)
        origin_description_input.alignment = 0

        appearance_description_paragraph = document.add_paragraph()
        appearance_description_paragraph.add_run(f'{self.condition_before_restoration_title}').bold = True
        appearance_description_paragraph.alignment = 0
        visual_observation_title = document.add_paragraph()
        visual_observation_title.add_run(f'{self.appearance_description_title}', 'Emphasis')
        visual_observation_title.alignment = 0
        appearance_description_input = document.add_paragraph()
        appearance_description = re.sub(r'<br>', '\n', appearance_description)
        appearance_description_input.add_run(f'{appearance_description}')
        appearance_description_input.paragraph_format.first_line_indent = Pt(18)
        appearance_description_input.alignment = 0

        damages_description_paragraph = document.add_paragraph()
        damages_description_paragraph.add_run(f'{self.damages_description_title}', 'Emphasis')
        damages_description_paragraph.alignment = 0

        damages_description_input = document.add_paragraph()
        damages_description = re.sub(r'<br>', '\n', damages_description)
        damages_description_input.add_run(f'{damages_description}')
        damages_description_input.paragraph_format.first_line_indent = Pt(18)
        damages_description_input.alignment = 0

        signs_description_paragraph = document.add_paragraph()
        signs_description_paragraph.add_run(f'{self.signs_description_title}', 'Emphasis')
        signs_description_paragraph.alignment = 0

        signs_description_input = document.add_paragraph()
        signs_description = re.sub(r'<br>', '\n', signs_description)
        signs_description_input.add_run(f'{signs_description}')
        signs_description_input.paragraph_format.first_line_indent = Pt(18)
        signs_description_input.alignment = 0

        size_description_paragraph = document.add_paragraph()
        size_description_paragraph.add_run(f'{self.size_description_title}', 'Emphasis')
        size_description_paragraph.alignment = 0

        size_description_input = document.add_paragraph()
        size_description = re.sub(r'<br>', '\n', size_description)
        size_description_input.add_run(f'{size_description}')
        size_description_input.paragraph_format.left_indent = Inches(0.25)
        size_description_input.alignment = 0

        document.add_page_break()

        researches_paragraph = document.add_paragraph()
        researches_paragraph.add_run(f'{self.researches_title}').bold = True
        researches_paragraph.alignment = 0

        researches_table = document.add_table(rows=2, cols=3)
        researches_table.autofit = False
        researches_table.allow_autofit = False
        researches_table.columns[0].width = Inches(2.0)
        researches_table.columns[1].width = Inches(3.0)
        researches_table.columns[2].width = Inches(1.0)
        researches_table.style = 'TableGrid'
        researches_table.alignment = 1

        researches_parameter = researches_table.rows[0].cells
        researches_parameter[0].text = f'{self.purposes_researches_title}'
        researches_parameter[1].text = f'{self.methods_researches_title}'
        researches_parameter[2].text = f'{self.executor_date_researches_title}'

        researches_parameter = researches_table.rows[1].cells
        purposes_researches = re.sub(r'<br>', '\n', purposes_researches)
        researches_parameter[0].text = f'{purposes_researches}'
        methods_researches = re.sub(r'<br>', '\n', methods_researches)
        researches_parameter[1].text = f'{methods_researches}'
        executor_date_researches = re.sub(r'<br>', '\n', executor_date_researches)
        researches_parameter[2].text = f'{executor_date_researches}'

        results_researches_paragraph = document.add_paragraph()
        results_researches_paragraph.add_run(f'{self.results_researches_title}').bold = True
        results_researches_paragraph.alignment = 0

        results_researches_input = document.add_paragraph()
        results_researches = re.sub(r'<br>', '\n', results_researches)
        results_researches_input.add_run(f'{results_researches}')
        results_researches_input.paragraph_format.first_line_indent = Pt(18)
        results_researches_input.alignment = 0

        document.add_page_break()

        restoration_program_paragraph = document.add_paragraph()
        restoration_program_paragraph.add_run(f'{self.restoration_program_title}').bold = True
        restoration_program_paragraph.alignment = 0
        treatments_order_program_paragraph = document.add_paragraph()
        treatments_order_program_paragraph.add_run(f'{self.sequence_of_treatments_title}', 'Emphasis')
        treatments_order_program_paragraph.alignment = 0
        restoration_program_input = document.add_paragraph()
        restoration_program = re.sub(r'<br>', '\n', restoration_program)
        restoration_program_input.add_run(f'{restoration_program}')
        restoration_program_input.alignment = 0

        program_approved_meeting_table = document.add_table(rows=2, cols=1)
        program_approved_meeting_table.style = 'TableGrid'
        program_approved_meeting_table.alignment = 1

        program_approved_meeting_parameter = program_approved_meeting_table.rows[0].cells
        program_approved_meeting_parameter[0].text = f'{self.program_approved_meeting_title}'

        program_approved_meeting_parameter = program_approved_meeting_table.rows[1].cells
        program_approved_meeting_parameter[0].text = f'{self.approved_meeting_protocol_number_title}'

        appointed_responsible_restorer_paragraph = document.add_paragraph()
        appointed_responsible_restorer_paragraph.add_run(f'{self.appointed_responsible_restorer_title}')
        appointed_responsible_restorer_paragraph.alignment = 0

        meeting_secretary_paragraph = document.add_paragraph()
        meeting_secretary_paragraph.add_run(f'{self.meeting_secretary_title}')
        meeting_secretary_paragraph.alignment = 0

        reapproved_restoration_program_paragraph = document.add_paragraph()
        reapproved_restoration_program_paragraph.add_run(f'{self.reapproved_restoration_program_title}').bold = True
        reapproved_restoration_program_paragraph.alignment = 0

        reapproved_program_meeting_table = document.add_table(rows=2, cols=1)
        reapproved_program_meeting_table.style = 'TableGrid'
        reapproved_program_meeting_table.alignment = 1

        reapproved_program_meeting_parameter = reapproved_program_meeting_table.rows[0].cells
        reapproved_program_meeting_parameter[0].text = f'{self.reapproved_program_meeting_place_title}'

        reapproved_program_meeting_parameter = reapproved_program_meeting_table.rows[1].cells
        reapproved_program_meeting_parameter[0].text = f'{self.reapproved_meeting_protocol_number_title}'

        reapproved_meeting_secretary_paragraph = document.add_paragraph()
        reapproved_meeting_secretary_paragraph.add_run(f'{self.meeting_secretary_title}')
        reapproved_meeting_secretary_paragraph.alignment = 0

        document.add_page_break()

        treatments_paragraph = document.add_paragraph()
        treatments_paragraph.add_run(f'{self.treatments_title}').bold = True
        treatments_paragraph.alignment = 0

        treatments_table = document.add_table(rows=2, cols=3)
        treatments_table.autofit = False
        treatments_table.allow_autofit = False
        treatments_table.columns[0].width = Inches(3.0)
        treatments_table.columns[1].width = Inches(1.6)
        treatments_table.columns[2].width = Inches(1.0)
        treatments_table.style = 'TableGrid'
        treatments_table.alignment = 1

        treatments_parameter = treatments_table.rows[0].cells
        treatments_parameter[0].text = f'{self.treatments_descriptions_title}'
        treatments_parameter[1].text = f'{self.treatments_chemicals_title}'
        treatments_parameter[2].text = f'{self.treatments_executor_date_title}'

        treatments_parameter = treatments_table.rows[1].cells
        treatments_descriptions = re.sub(r'<br>', '\n', treatments_descriptions)
        treatments_parameter[0].text = f'{treatments_descriptions}'
        treatments_chemicals = re.sub(r'<br>', '\n', treatments_chemicals)
        treatments_parameter[1].text = f'{treatments_chemicals}'
        treatments_executor_date = re.sub(r'<br>', '\n', treatments_executor_date)
        treatments_parameter[2].text = f'{treatments_executor_date}'

        document.add_page_break()

        treatments_paragraph = document.add_paragraph()
        treatments_paragraph.add_run(f'{self.treatments_results_title}').bold = True
        treatments_paragraph.alignment = 0

        treatments_results_input = document.add_paragraph()
        treatments_results = re.sub(r'<br>', '\n', treatments_results)
        treatments_results_input.add_run(f'{treatments_results}')
        treatments_results_input.paragraph_format.first_line_indent = Pt(18)
        treatments_results_input.alignment = 0

        result_responsible_restorer_paragraph = document.add_paragraph()
        result_responsible_restorer_paragraph.add_run(f'{self.responsible_restorer_signature_title}{responsible_restorer}{self.signature_place}')
        result_responsible_restorer_paragraph.alignment = 2

        result_execute_restorer_paragraph = document.add_paragraph()
        result_execute_restorer_paragraph.add_run(f'{self.execute_restorer_signature_title}{execute_restorer}{self.signature_place}')
        result_execute_restorer_paragraph.alignment = 2

        result_object_output_date_paragraph = document.add_paragraph()
        result_object_output_date_paragraph.add_run(f'{object_output_date}')
        result_object_output_date_paragraph.alignment = 2

        meeting_conclusion_paragraph = document.add_paragraph()
        meeting_conclusion_paragraph.add_run(f'{self.meeting_conclusion_title}').bold = True
        meeting_conclusion_paragraph.alignment = 0

        meeting_conclusion_table = document.add_table(rows=2, cols=1)
        meeting_conclusion_table.style = 'TableGrid'
        meeting_conclusion_table.alignment = 1

        meeting_conclusion_parameter = meeting_conclusion_table.rows[0].cells
        meeting_conclusion_parameter[0].text = f'{self.meeting_place_title}'

        meeting_conclusion_parameter = meeting_conclusion_table.rows[1].cells
        meeting_conclusion_parameter[0].text = f'{self.after_restoration_meeting_protocol_number_title}'

        conclusion_meeting_secretary_paragraph = document.add_paragraph()
        conclusion_meeting_secretary_paragraph.add_run(f'{self.meeting_secretary_title}')
        conclusion_meeting_secretary_paragraph.alignment = 0

        recommendations_paragraph = document.add_paragraph()
        recommendations_paragraph.add_run(self.recommendations_title).bold = True
        recommendations_paragraph.alignment = 0

        recommendations_table = document.add_table(rows=5, cols=1)
        recommendations_table.style = 'TableGrid'
        recommendations_table.alignment = 1

        recommendations_execute_restorer_paragraph = document.add_paragraph()
        recommendations_execute_restorer_paragraph.add_run(f'{self.execute_restorer_signature_title}{execute_restorer}{self.signature_place}')
        recommendations_execute_restorer_paragraph.alignment = 2

        recommendations_output_date_paragraph = document.add_paragraph()
        recommendations_output_date_paragraph.add_run(f'{object_output_date}')
        recommendations_output_date_paragraph.alignment = 2

        document.add_page_break()

        illustrative_material_paragraph = document.add_paragraph()
        illustrative_material_paragraph.add_run(f'{self.illustrative_material_title}').bold = True
        illustrative_material_paragraph.alignment = 0

        beforeRestorationPhotoPath = 'static/Intelligible_illustrations/' + before_restoration_image_description
        document.add_picture(beforeRestorationPhotoPath, width=Inches(1.25))

        before_restoration_image_description_paragraph = document.add_paragraph()
        before_restoration_image_description_paragraph.add_run(f'{self.before_restoration_image_description_title}{before_restoration_image_description}')
        before_restoration_image_description_paragraph.alignment = 0

        processRestorationPhotoPath = 'static/Intelligible_illustrations/' + process_restoration_image_description
        document.add_picture(processRestorationPhotoPath, width=Inches(1.25))

        process_restoration_image_description_paragraph = document.add_paragraph()
        process_restoration_image_description_paragraph.add_run(f'{self.process_restoration_image_description_title}{process_restoration_image_description}')
        process_restoration_image_description_paragraph.alignment = 0

        afterRestorationPhotoPath = 'static/Intelligible_illustrations/' + after_restoration_image_description
        document.add_picture(afterRestorationPhotoPath, width=Inches(1.25))

        after_restoration_image_description_paragraph = document.add_paragraph()
        after_restoration_image_description_paragraph.add_run(f'{self.after_restoration_image_description_title}{after_restoration_image_description}')
        after_restoration_image_description_paragraph.alignment = 0

        document.add_page_break()

        counted_illustrative_material_paragraph = document.add_paragraph()
        counted_illustrative_material_paragraph.add_run(f'{self.appendix_title}').bold = True
        counted_illustrative_material_paragraph.add_run(f'{self.related_materials_title}')
        counted_illustrative_material_paragraph.alignment = 0

        counted_illustrative_material_table = document.add_table(rows=4, cols=3)
        counted_illustrative_material_table.autofit = False
        counted_illustrative_material_table.allow_autofit = False
        counted_illustrative_material_table.columns[0].width = Inches(1.5)
        counted_illustrative_material_table.columns[1].width = Inches(1.0)
        counted_illustrative_material_table.columns[2].width = Inches(0.5)
        counted_illustrative_material_table.style = 'TableGrid'
        counted_illustrative_material_table.alignment = 0

        counted_illustrative_material_parameter = counted_illustrative_material_table.rows[0].cells
        counted_illustrative_material_parameter[0].text = f'{self.photos_title}'
        counted_illustrative_material_parameter[1].text = f'{self.photos_amount}'
        counted_illustrative_material_parameter[2].text = f'{self.units_title}'

        counted_illustrative_material_parameter = counted_illustrative_material_table.rows[1].cells
        counted_illustrative_material_parameter[0].text = f'{self.map_schemes_title}'
        counted_illustrative_material_parameter[1].text = f'{self.map_schemes_amount}'
        counted_illustrative_material_parameter[2].text = f'{self.units_title}'

        counted_illustrative_material_parameter = counted_illustrative_material_table.rows[2].cells
        counted_illustrative_material_parameter[0].text = f'{self.additional_researches_results_title}'
        counted_illustrative_material_parameter[1].text = f'{self.additional_researches_amount}'
        counted_illustrative_material_parameter[2].text = f'{self.units_title}'

        counted_illustrative_material_parameter = counted_illustrative_material_table.rows[3].cells
        counted_illustrative_material_parameter[0].text = f'{self.other_related_materials_title}'
        counted_illustrative_material_parameter[1].text = f'{self.other_related_materials_amount}'
        counted_illustrative_material_parameter[2].text = f'{self.units_title}'

        attachment_illustrative_material_place_paragraph = document.add_paragraph()
        attachment_illustrative_material_place_paragraph.add_run(f'{self.attachment_illustrative_material_place_title}')
        attachment_illustrative_material_place_paragraph.alignment = 2

        document.add_page_break()

        object_transferred_table = document.add_table(rows=4, cols=1)
        object_transferred_table.style = 'TableGrid'
        object_transferred_table.alignment = 1

        object_transferred_parameter = object_transferred_table.rows[0].cells
        object_transferred_parameter[0].text = f'{self.object_transferred_place_title}'

        object_transferred_parameter = object_transferred_table.rows[1].cells
        object_transferred_parameter[0].text = f'{self.responsible_treasurer_and_storage_place_title}'

        object_transferred_parameter = object_transferred_table.rows[2].cells
        object_transferred_parameter[0].text = f'{self.give_back_report_title}'

        object_transferred_parameter = object_transferred_table.rows[3].cells
        object_transferred_parameter[0].text = f'{self.passport_copies_transferred_place_title}'

        first_divider_paragraph = document.add_paragraph()
        first_divider_paragraph.add_run('\n')
        first_divider_paragraph.alignment = 1

        related_employees_table = document.add_table(rows=5, cols=2)
        related_employees_table.autofit = False
        related_employees_table.allow_autofit = False
        related_employees_table.columns[0].width = Inches(1.7)
        related_employees_table.columns[1].width = Inches(4.4)
        related_employees_table.style = 'TableGrid'
        related_employees_table.alignment = 1

        related_employees_parameter = related_employees_table.rows[0].cells
        related_employees_parameter[0].text = f'{self.head_of_institution_title}'

        related_employees_parameter = related_employees_table.rows[1].cells
        related_employees_parameter[0].text = f'{self.head_of_the_department_title}'

        related_employees_parameter = related_employees_table.rows[2].cells
        related_employees_parameter[0].text = f'{self.head_of_restoration_title}'
        related_employees_parameter[1].text = f'{responsible_restorer}'

        related_employees_parameter = related_employees_table.rows[3].cells
        related_employees_parameter[0].text = f'{self.executor_of_restoration_title}'
        related_employees_parameter[1].text = f'{execute_restorer}'

        related_employees_parameter = related_employees_table.rows[4].cells
        related_employees_parameter[0].text = f'{self.restorers_and_other_executors_title}'
        related_employees_parameter[1].text = f'{self.empty_row_place}'

        second_divider_paragraph = document.add_paragraph()
        second_divider_paragraph.add_run('\n')
        second_divider_paragraph.alignment = 1

        other_executors_table = document.add_table(rows=1, cols=1)
        other_executors_table.style = 'TableGrid'
        other_executors_table.alignment = 1

        other_executors_parameter = other_executors_table.rows[0].cells
        other_executors_parameter[0].text = f'{self.other_executors_signature_title}'

        third_divider_paragraph = document.add_paragraph()
        third_divider_paragraph.add_run('\n')
        third_divider_paragraph.alignment = 1

        condition_observation_table = document.add_table(rows=2, cols=4)
        condition_observation_table.style = 'TableGrid'
        condition_observation_table.alignment = 1

        condition_observation_parameter = condition_observation_table.rows[0].cells
        condition_observation_parameter[0].text = f'{self.condition_check_date_title}'
        condition_observation_parameter[1].text = f'{self.condition_description_title}'
        condition_observation_parameter[2].text = f'{self.storage_condition_title}'
        condition_observation_parameter[3].text = f'{self.checking_person_signature_title}'

        condition_observation_parameter = condition_observation_table.rows[1].cells
        condition_observation_parameter[0].text = f'{self.indent}'

        document.add_page_break()

        document.save('filled_passport.docx')
