from social_groups_analysis import get_data_for_special_group
from parse_primary_json_data import create_base_empty_dict, print_json_data_to_terminal, read_base_dict_from_json
from translaters import TRANSLATOR

def print_all_partial_subgroups_analysis(survey_data_filename):
   print('analyze_technical_skill_growth_clusters_by_politics')
   print_json_data_to_terminal(analyze_technical_skill_growth_clusters_by_politics(survey_data_filename))

   print('analyze_humanities_people_clusters_by_technical_skills')
   print_json_data_to_terminal(analyze_humanities_people_clusters_by_technical_skills(survey_data_filename))

   print('analyze_techies_people_clusters_by_technical_skills')
   print_json_data_to_terminal(analyze_techies_people_clusters_by_technical_skills(survey_data_filename))

   print('analyze_opposite_politics_views_by_age')
   print_json_data_to_terminal(analyze_opposite_politics_views_by_age(survey_data_filename))


def analyze_technical_skill_growth_clusters_by_politics(survey_data_filename):
    return get_relative_percents_by_two_signs_clusters(survey_data_filename, 6,5, ("increased significantly", "increased a little bit"))


def analyze_humanities_people_clusters_by_technical_skills(survey_data_filename):
    return get_relative_percents_by_two_signs_clusters(survey_data_filename, 2, 6, ("humanities student", ))


def analyze_techies_people_clusters_by_technical_skills(survey_data_filename):
    return get_relative_percents_by_two_signs_clusters(survey_data_filename, 2, 6, ("technical student", "IT-sector worker"))


def analyze_opposite_politics_views_by_age(survey_data_filename):
    return get_relative_percents_by_two_signs_clusters(survey_data_filename, 5, 0, ("became more opposite cuz of blocks", ))


def get_relative_percents_by_two_signs_clusters(survey_data_filename, major_analysis_sign_index, minor_analysis_sign_index, major_sign_combined_features):
    subgroup_data_json = get_special_clusters_by_two_signs_clusters(survey_data_filename, major_analysis_sign_index, minor_analysis_sign_index, major_sign_combined_features)
    all_data_json = read_base_dict_from_json(survey_data_filename)
    minor_analysis_sign_key = list(TRANSLATOR.keys())[minor_analysis_sign_index]
    for subsubgroup in subgroup_data_json.keys():
        subgroup_data_json[subsubgroup] /= all_data_json[minor_analysis_sign_key][subsubgroup]

    return subgroup_data_json


def get_special_clusters_by_two_signs_clusters(survey_data_filename, major_analysis_sign_index, minor_analysis_sign_index, major_sign_combined_features):
    main_sign_analysis_json = get_data_for_special_group(major_analysis_sign_index, survey_data_filename)
    result_json = create_base_empty_dict()
    for feature in major_sign_combined_features:
        current_group_json = main_sign_analysis_json[feature]
        for subgroup in current_group_json.keys():
            for subsubgroup in current_group_json[subgroup].keys():
                result_json[subgroup][subsubgroup] += main_sign_analysis_json[feature][subgroup][subsubgroup]

    return  result_json[list(result_json.keys())[minor_analysis_sign_index]]
