from vizualization.vizualizator_core import plot_overall_statistics, plot_partial_subgroups_analysis
from config import FILENAME

def main():
    plot_overall_statistics(FILENAME, "political_activity_dynamic", "Распределение политических взглядов")
    plot_overall_statistics(FILENAME, "technical_skills_dynamic", "Распределение технических навыков")
    plot_partial_subgroups_analysis(FILENAME)

if __name__ == "__main__":
    main()