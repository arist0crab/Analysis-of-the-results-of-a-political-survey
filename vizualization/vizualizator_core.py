import os
import textwrap
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
from typing import Any
from config import *
from errors import *
from data_processing.translaters import TRANSLATOR
from data_processing.parse_primary_json_data import read_base_dict_from_json
from data_processing.partial_subgroups_analysis import *

def build_pie_chart(data: dict, target_group: str) -> tuple[list[str], list[float]]:
    translator = TRANSLATOR.get(target_group)
    labels = []
    sizes = []
    for key, value in data.items():
        if value > 0:
            labels.append(translator.get(key))
            sizes.append(value)
    return labels, sizes

def ensure_plots_directory() -> None:
    if not os.path.exists(PLOTS_DIR):
        os.makedirs(PLOTS_DIR)

def prepare_labels(labels: list[str], sizes: list[float]) -> tuple[list[str], list[str], list[str]]:
    pie_labels = [str(i + 1) for i in range(len(sizes))]
    legend_labels = [textwrap.fill(f"{i + 1}. {label}", width=45) for i, label in enumerate(labels)]
    colors = CHART_COLORS[:len(sizes)]
    return pie_labels, legend_labels, colors

def add_callout_annotations(ax: Axes, wedges: list[Any], sizes: list[float], pie_labels: list[str]) -> None:
    bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
    kw = dict(arrowprops=dict(arrowstyle="-"), bbox=bbox_props, zorder=0, va="center", fontsize=16)

    for i, p in enumerate(wedges):
        angle = (p.theta2 - p.theta1) / 2. + p.theta1
        y = np.sin(np.deg2rad(angle))
        x = np.cos(np.deg2rad(angle))
        
        horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
        connectionstyle = f"angle,angleA=0,angleB={angle}"
        kw["arrowprops"].update({"connectionstyle": connectionstyle})
        
        percentage = sizes[i] / sum(sizes) * 100
        label_text = f"{pie_labels[i]} ({percentage:.1f}%)"

        ax.annotate(label_text, xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y),
                    horizontalalignment=horizontalalignment, **kw)

def setup_legend(ax: Axes, wedges: list[Any], legend_labels: list[str]) -> Any:
    leg = ax.legend(
        wedges, 
        legend_labels,
        title="Расшифровка вариантов",
        loc="center left",
        bbox_to_anchor=(1.2, 0.5), 
        fontsize=10
    )
    leg.remove() 
    return leg

def save_legend_separately(legend, title: str) -> None:
    fig_leg = plt.figure(figsize=(6, len(legend.get_texts()) * 0.5))
    new_leg = fig_leg.legend(
        legend.legend_handles, 
        [t.get_text() for t in legend.get_texts()],
        title="Расшифровка вариантов",
        loc='center',
        fontsize=10
    )
    
    path = os.path.join(PLOTS_DIR, f"{title}_legend.png")
    fig_leg.savefig(path, dpi=300, bbox_inches='tight')
    plt.close(fig_leg) 

def save_and_show_chart(fig: Figure, title: str, legend: Any) -> None:
    fig.subplots_adjust(right=0.9) 

    path = os.path.join(PLOTS_DIR, f"{title}.png")
    plt.savefig(path, bbox_inches='tight', dpi=300)
    
    save_legend_separately(legend, title)

def draw_pie_chart(data: dict, target_group: str, title: str = "") -> None:
    labels, sizes = build_pie_chart(data, target_group)
    if not sizes:
        return

    ensure_plots_directory()
    pie_labels, legend_labels, colors = prepare_labels(labels, sizes)

    fig, ax = plt.subplots(figsize=(12, 7))
    
    wedges, _ = ax.pie(sizes, wedgeprops=dict(width=0.5), startangle=-40, colors=colors)
    ax.axis('equal')

    add_callout_annotations(ax, wedges, sizes, pie_labels)
    legend = setup_legend(ax, wedges, legend_labels)
    save_and_show_chart(fig, title, legend)

def plot_overall_statistics(filename: str, target_group: str, title: str = "") -> None:
    data = read_base_dict_from_json(filename)
    if target_group not in data.keys():
        print(NO_SUCH_GROUP_ERROR_TEXT)
        return
    draw_pie_chart(data[target_group], target_group, title)

def build_histogram(data: dict, subgroup: str) -> tuple[list[str], list[float]]:
    labels = []
    sizes = []
    for key, value in data.items():
        raw_label = TRANSLATOR[subgroup][key]
        wrapped_label = textwrap.fill(raw_label, width=15)
        labels.append(wrapped_label)
        sizes.append(value)
    return labels, sizes

def draw_histogram(data: dict, subgroup: str, title: str, xlabel: str) -> None:
    labels, sizes = build_histogram(data, subgroup)
    ensure_plots_directory()

    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(labels, sizes, color=CHART_COLORS[:len(labels)])
    
    ax.set_xlabel(xlabel)
    ax.set_ylabel("Процент респондентов")
    
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height:.2f}%', 
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points", 
                    ha='center', 
                    va='bottom',
                    fontsize=10)
        
    path = os.path.join(PLOTS_DIR, f"{title}.png")
    plt.savefig(path, bbox_inches='tight', dpi=300)
    plt.close(fig)

def plot_partial_subgroups_analysis(filename: str) -> None:
    technical_skill_growth_data_by_politics = analyze_technical_skill_growth_clusters_by_politics(filename)
    humanities_people_data_by_technical_skills = analyze_humanities_people_clusters_by_technical_skills(filename)
    techies_people_data_by_technical_skills = analyze_techies_people_clusters_by_technical_skills(filename)
    opposite_politics_views_data_by_age = analyze_opposite_politics_views_by_age(filename)

    draw_histogram(technical_skill_growth_data_by_politics, "political_activity_dynamic", "technical_skill_growth_by_politics", "Рост технических навыков в зависимости от политических взглядов")
    draw_histogram(humanities_people_data_by_technical_skills, "technical_skills_dynamic", "humanities_people_by_technical_skills", "Распределение гуманитариев по техническим навыкам")
    draw_histogram(techies_people_data_by_technical_skills, "technical_skills_dynamic", "techies_people_by_technical_skills", "Распределение технарей по техническим навыкам")
    draw_histogram(opposite_politics_views_data_by_age, "age", "opposite_politics_views_by_age", "Распределение противоположных политических взглядов по возрасту")