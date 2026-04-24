from vizualization.vizualizator_core import plot_overall_statistics
from data_processing.social_groups_analysis import get_processed_group_analysis 
from config import FILENAME

def main():
    plot_overall_statistics(FILENAME, "political_activity_dynamic", "Распределение политических взглядов")
    plot_overall_statistics(FILENAME, "technical_skills_dynamic", "Распределение технических навыков")

    subgroup_data, _ = get_processed_group_analysis(FILENAME)

if __name__ == "__main__":
    main()