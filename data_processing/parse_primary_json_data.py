import json
from translaters import *


def read_base_dict_from_json(survey_data_filename):

    survey_data = get_json_data(survey_data_filename)
    json_data = create_base_empty_dict()

    for blank in survey_data:
        load_blank_to_json(json_data, blank)

    return  json_data


def load_blank_to_json(json_data, blank):
    load_age(json_data, blank[0][1])
    load_place_of_residence(json_data, blank[1][1])
    load_profession(json_data, blank[2][1])
    load_frequency_of_using_bypass(json_data, blank[3][1])
    load_political_activity_dynamic(json_data, blank[15][1])
    load_technical_skills_dynamic(json_data, blank[16][1])
    load_blocks_efficiency_opinion(json_data, blank[17][1])
    load_publish_opinion_in_media(json_data, blank[18][1])

    for i in range(4, 15):
        load_blocked_services_using(json_data, blank[i][1])

    return json_data


def print_json_data_to_terminal(json_data):
    print(json.dumps(json_data, indent=4))

def create_base_empty_dict():
    analys_data = dict()
    analys_data["age"] = dict.fromkeys(age_translater.keys(), 0)
    analys_data["place_of_residence"] = dict.fromkeys(place_of_residence_translater.keys(), 0)
    analys_data["profession"] = dict.fromkeys(profession_translater.keys(), 0)
    analys_data["frequency_of_using_bypass"] = dict.fromkeys(frequency_of_using_bypass_translater.keys(), 0)
    analys_data["blocked_services_using"] = dict.fromkeys(blocked_services_using_translater.keys(), 0)
    analys_data["political_activity_dynamic"] = dict.fromkeys(political_activity_dynamic_translater.keys(), 0)
    analys_data["technical_skills_dynamic"] = dict.fromkeys(technical_skills_dynamic_translater.keys(), 0)
    analys_data["blocks_efficiency_opinion"] = dict.fromkeys(blocks_efficiency_opinion_translater.keys(), 0)
    analys_data["publish_opinion_in_media"] = dict.fromkeys(publish_opinion_in_media_translater.keys(), 0)

    return  analys_data


def get_json_data(json_filename):
    with open(json_filename, "r") as data_file:
        json_data = json.load(data_file)

    return json_data

def load_age(json_data, age_str):
    for key, value in age_translater.items():
        json_data["age"][key] += (age_str == value)


def load_place_of_residence(json_data, place_str):
    for key, value in place_of_residence_translater.items():
        json_data["place_of_residence"][key] += (place_str == value)


def load_profession(json_data, profession_str):
    for key, value in profession_translater.items():
        json_data["profession"][key] += (profession_str == value)


def load_frequency_of_using_bypass(json_data, frequency_str):
    for key, value in frequency_of_using_bypass_translater.items():
        json_data["frequency_of_using_bypass"][key] += (frequency_str == value)


def load_blocked_services_using(json_data, service_str):
    for key, value in blocked_services_using_translater.items():
        json_data["blocked_services_using"][key] += (service_str == value)


def load_political_activity_dynamic(json_data, political_activity_str):
    for key, value in political_activity_dynamic_translater.items():
        json_data["political_activity_dynamic"][key] += (political_activity_str == value)


def load_technical_skills_dynamic(json_data, skill_str):
    for key, value in technical_skills_dynamic_translater.items():
        json_data["technical_skills_dynamic"][key] += (skill_str == value)


def load_blocks_efficiency_opinion(json_data, block_str):
    for key, value in blocks_efficiency_opinion_translater.items():
        json_data["blocks_efficiency_opinion"][key] += (block_str == value)


def load_publish_opinion_in_media(json_data, publish_opinion_str):
    for key, value in publish_opinion_in_media_translater.items():
        json_data["publish_opinion_in_media"][key] += (publish_opinion_str == value)