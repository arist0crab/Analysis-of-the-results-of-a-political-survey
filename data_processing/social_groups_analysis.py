from translaters import *
from parse_primary_json_data import get_json_data, create_base_empty_dict, load_blank_to_json


choose_group_menu = """
Выберите признак группы респондентов, по которому необходимо
провести анализ:
0. Возраст
1. Место жительства
2. Род деятельности
3. Обход блокировок
4. Заблокированные сервисы
5. Динамика изменения политических взглядов
6. Динамика изменения уровня технических навыков
7. Субъективная оценка эффективности блокировок
8. Отношение к публикации своего мнения в медиа
9. Выход
"""


def get_raw_group_analysis(survey_data_filename):
    menu_option = choose_option(9, choose_group_menu)
    raw_group_analysis_json = get_data_for_special_group(menu_option, survey_data_filename)

    return raw_group_analysis_json


def get_processed_group_analysis(survey_data_filename):
    menu_option = choose_option(9, choose_group_menu)
    submenu_option = choose_subgroup_for_analysis(menu_option)

    current_subgroup_translator = get_key_translators()[menu_option]
    processed_group_analysis_json = get_statistics_for_special_group(menu_option, survey_data_filename)
    if submenu_option == len(current_subgroup_translator):
        return processed_group_analysis_json

    processed_group_analysis_json_items = list(processed_group_analysis_json.items())
    return processed_group_analysis_json_items[submenu_option]


def get_statistics_for_special_group(group_index, survey_data_filename):
    special_json_data = get_data_for_special_group(group_index, survey_data_filename)

    for current_group in special_json_data.keys():
        current_group_json = special_json_data[current_group]
        group_respondents_quantity = calculate_group_respondents(current_group_json)

        for group_characteristic in current_group_json.keys():
            current_group_characteristic_json = current_group_json[group_characteristic]

            for group_characteristic_item in current_group_characteristic_json.keys():
                current_percentage = current_group_characteristic_json[group_characteristic_item] / group_respondents_quantity * 100
                current_group_characteristic_json[group_characteristic_item] = f"{current_percentage:.2f}%"
        add_respondents_quantity_to_group(current_group_json, group_respondents_quantity)

    return special_json_data


def get_data_for_special_group(group_index, survey_data_filename):

    json_data = dict()
    survey_data = get_json_data(survey_data_filename)
    key_translators = get_key_translators()

    if group_index < 9:

        analysis_key = key_translators[group_index]
        json_data = {key: create_base_empty_dict() for key in analysis_key.keys()}

        for current_group in analysis_key.keys():
            survey_group_name = analysis_key[current_group]

            for blank in survey_data:
                for question in blank:
                    if question[1] == survey_group_name:
                        json_data[current_group] = load_blank_to_json(json_data[current_group], blank)

    return  json_data


def calculate_group_respondents(json_group_data):
    return sum(json_group_data["age"].values())


def add_respondents_quantity_to_group(json_group_data, respondents_quantity):
    json_group_data["respondents_quantity"] = respondents_quantity


def get_key_translators():
    return (
        age_translater,
        place_of_residence_translater,
        profession_translater,
        frequency_of_using_bypass_translater,
        blocked_services_using_translater,
        political_activity_dynamic_translater,
        technical_skills_dynamic_translater,
        blocks_efficiency_opinion_translater,
        publish_opinion_in_media_translater
    )


def choose_subgroup_for_analysis(group_index):
    if 0 <= group_index <= 8:
        key_translators = get_key_translators()
        current_translator = key_translators[group_index]

        submenu = "Выберите подгруппу для анализа:\n"
        submenu += "\n".join([f'{i}. {value}' for i, value in enumerate(current_translator.values())])
        submenu += f"\n{len(current_translator)}. Вывести все"

        return choose_option(len(current_translator), submenu)

    return -1


def choose_option(max_possible_option, message):
    option_was_inputted = False
    menu_option = max_possible_option

    while not option_was_inputted:
        print(message)
        try:
            menu_option = int(input("Номер опции: "))
            option_was_inputted = (0 <= menu_option <= max_possible_option)

        except ValueError:
            print("Введите только число - номер опции меню")

    return menu_option
