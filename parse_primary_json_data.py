import json


def read_base_dict_from_json(survey_data_filename):

    survey_data = get_json_data(survey_data_filename)
    json_data = create_base_empty_dict()

    for blank in survey_data:

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

    return  json_data


def print_json_data_to_terminal(json_data):
    print(json.dumps(json_data, indent=4))

def create_base_empty_dict():
    ages = ("less 18", "18-25", "26-40", "41-60", "60 and elder")
    place_of_residence = ("Moscow", "Moscow area", "Saint-Petersburg", "another million citizens town", "another less than million citizens town", "settlement or village")
    profession = ("schoolboy", "technical student", "humanities student", "IT-sector worker", "not IT-sector worker", "entrepreneur", "budgetary sphere", "pensioner", "another")
    frequency_of_using_bypass = ("yes regularly", "yes but rarely", "no but i know", "no and i dont know")
    blocked_services_using = ("youtube", "telegram", "instagram", "facebook", "tik-tok", "twitter/x", "discord", "foreign-news", "foreign-music", "another", "i dont use")
    political_activity_dynamic = ("became more opposite cuz of blocks", "became more opposite independence of blocks", "became more loyal cuz of blocks", "became more loyal independence of blocks", "have not changed", "difficult to answer")
    technical_skills_dynamic = ("increased significantly", "increased a little bit", "has not changed: they were good", "has not changed: they were bad", "i dont use blocked resources")
    blocks_efficiency_opinion = ("effectively", "partially effectively", "not effectively")
    publish_opinion_in_media = ("became carefully", "write all i want", "never say opinion in media")

    analys_data = dict()
    analys_data["age"] = dict.fromkeys(ages, 0)
    analys_data["place_of_residence"] = dict.fromkeys(place_of_residence, 0)
    analys_data["profession"] = dict.fromkeys(profession, 0)
    analys_data["frequency_of_using_bypass"] = dict.fromkeys(frequency_of_using_bypass, 0)
    analys_data["blocked_services_using"] = dict.fromkeys(blocked_services_using, 0)
    analys_data["political_activity_dynamic"] = dict.fromkeys(political_activity_dynamic, 0)
    analys_data["technical_skills_dynamic"] = dict.fromkeys(technical_skills_dynamic, 0)
    analys_data["blocks_efficiency_opinion"] = dict.fromkeys(blocks_efficiency_opinion, 0)
    analys_data["publish_opinion_in_media"] = dict.fromkeys(publish_opinion_in_media, 0)

    return  analys_data


def get_json_data(json_filename):
    with open(json_filename, "r") as data_file:
        json_data = json.load(data_file)

    return json_data


def load_age(json_data, age_str):
    json_data["age"]["less 18"] += age_str == "Младше 18 лет"
    json_data["age"]["18-25"] += age_str == "18-25 лет"
    json_data["age"]["26-40"] += age_str == "26-40 лет"
    json_data["age"]["41-60"] += age_str == "41-60 лет"
    json_data["age"]["60 and elder"] += age_str == "Старше 60 лет"


def load_place_of_residence(json_data, place_str):
    json_data["place_of_residence"]["Moscow"] += place_str == "Москва"
    json_data["place_of_residence"]["Moscow area"] += place_str == "Московская область"
    json_data["place_of_residence"]["Saint-Petersburg"] += place_str == "Санкт-Петербург"
    json_data["place_of_residence"]["another million citizens town"] +=  place_str == "Другой город-миллионник"
    json_data["place_of_residence"]["another less than million citizens town"] += place_str == "Другой город до 1млн жителей"
    json_data["place_of_residence"]["settlement or village"] += place_str == "Поселок или село"


def load_profession(json_data, profession_str):
    json_data["profession"]["schoolboy"] += profession_str == "Школьник"
    json_data["profession"]["technical student"] += profession_str == "Студент технической специальности"
    json_data["profession"]["humanities student"] += profession_str == "Студент гуманитарной / естественнонаучной / творческой специальности"
    json_data["profession"]["IT-sector worker"] += profession_str == "Работник IT-сферы / инженерии"
    json_data["profession"]["not IT-sector worker"] += profession_str == "Работник в сфере, не относящийся к IT / инженерии"
    json_data["profession"]["entrepreneur"] += profession_str == "Предприниматель"
    json_data["profession"]["budgetary sphere"] += profession_str == "Бюджетная сфера"
    json_data["profession"]["pensioner"] += profession_str == "Пенсионер"
    json_data["profession"]["another"] += profession_str == "Другое"


def load_frequency_of_using_bypass(json_data, frequency_str):
    json_data["frequency_of_using_bypass"]["yes regularly"] += frequency_str == "Да, регулярно"
    json_data["frequency_of_using_bypass"]["yes but rarely"] += frequency_str == "Да, но редко"
    json_data["frequency_of_using_bypass"]["no but i know"] += frequency_str == "Нет, но знаю, что это такое "
    json_data["frequency_of_using_bypass"]["no and i dont know"] += frequency_str == "Нет и не знаю, что это такое"


def load_blocked_services_using(json_data, service_str):
    json_data["blocked_services_using"]["youtube"] += service_str == "YouTube"
    json_data["blocked_services_using"]["telegram"] += service_str == "Telegram"
    json_data["blocked_services_using"]["instagram"] += service_str == "Instagram (запрещен на территории РФ)"
    json_data["blocked_services_using"]["facebook"] += service_str == "Facebook (запрещен на территории РФ)"
    json_data["blocked_services_using"]["tik-tok"] += service_str == "TikTok"
    json_data["blocked_services_using"]["twitter/x"] += service_str == "Twitter / X"
    json_data["blocked_services_using"]["discord"] += service_str == "Discord"
    json_data["blocked_services_using"]["foreign-news"] += service_str == "Зарубежные новостные сайты"
    json_data["blocked_services_using"]["foreign-music"] += service_str == "Зарубежные музыкальные сервисы"
    json_data["blocked_services_using"]["another"] += service_str == "Другое"
    json_data["blocked_services_using"]["i dont use"] += service_str == "Не пользуюсь такими"


def load_political_activity_dynamic(json_data, political_activity_str):
    json_data["political_activity_dynamic"]["became more opposite cuz of blocks"] += political_activity_str == "Да, стали более оппозиционными - в том числе из-за того, что блокировку интернет-ресурсов я воспринимаю как давление на свободу информации"
    json_data["political_activity_dynamic"]["became more opposite independence of blocks"] += political_activity_str == "Да, стали более оппозиционными. Причины не связаны с интернет-блокировками"
    json_data["political_activity_dynamic"]["became more loyal cuz of blocks"] += political_activity_str == "Да, стали более лояльными к власти: я считаю блокировки оправданной мерой для безопасности"
    json_data["political_activity_dynamic"]["became more loyal independence of blocks"] += political_activity_str == "Да, стали более лояльными к власти. Причины не связаны с интернет-блокировками"
    json_data["political_activity_dynamic"]["have not changed"] += political_activity_str == "Нет, мои взгляды не изменились"
    json_data["political_activity_dynamic"]["difficult to answer"] += political_activity_str == "Затрудняюсь ответить"


def load_technical_skills_dynamic(json_data, skill_str):
    json_data["technical_skills_dynamic"]["increased significantly"] += skill_str == "Существенно вырос - до блокировок я почти ничего не умел, теперь разбираюсь хорошо"
    json_data["technical_skills_dynamic"]["increased a little bit"] += skill_str == "Немного вырос - раньше не сталкивался, теперь научился базовым вещам"
    json_data["technical_skills_dynamic"]["has not changed: they were good"] += skill_str == "Не изменился - я хорошо разбирался в этом еще до блокировок"
    json_data["technical_skills_dynamic"]["has not changed: they were bad"] += skill_str == "Не изменился - я до сих пор в этом ничего не понимаю"
    json_data["technical_skills_dynamic"]["i dont use blocked resources"] += skill_str == "Блокировки меня не коснулись, так как я не пользуюсь заблокированными ресурсами"


def load_blocks_efficiency_opinion(json_data, block_str):
    json_data["blocks_efficiency_opinion"]["effectively"] += block_str == "Эффективны - люди перестают пользоваться заблокированными сервисами"
    json_data["blocks_efficiency_opinion"]["partially effectively"] += block_str == "Частично эффективны - некоторые люди перестают пользоваться привычными сервисами, другие находят пути обхода"
    json_data["blocks_efficiency_opinion"]["not effectively"] += block_str == "Неэффективны - люди массово обходят блокировки и продолжают пользоваться запрещенными ресурсами"


def load_publish_opinion_in_media(json_data, publish_opinion_str):
    json_data["publish_opinion_in_media"]["became carefully"] += publish_opinion_str == "Да, я стал осторожнее"
    json_data["publish_opinion_in_media"]["write all i want"] += publish_opinion_str == "Нет, пишу все, что считаю нужным"
    json_data["publish_opinion_in_media"]["never say opinion in media"] += publish_opinion_str == "Я никогда не выражал мнение публично в соцсетях"
