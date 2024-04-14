import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.decomposition import PCA
import streamlit_highcharts as hct
import streamlit as st

def visualize_target_circle(options_distances, chosen_option):
    series_data = []

    closest_dist = options_distances[0][1]  # Assuming the first option is the closest.
    max_distance = max(dist for _, dist in options_distances if dist > closest_dist)

    angle_increment = 360 / (len(options_distances) - 1)

    for i, (option_label, dist) in enumerate(options_distances):
        angle = i * angle_increment
        # Adjusting angle to start from 0 degrees to avoid text overlap
        if i > 0:
            angle -= angle_increment
        scaled_dist = (dist - closest_dist) / (max_distance - closest_dist) * 100 if max_distance > closest_dist else 0

        series_data.append({
            'name': option_label,
            'x': angle,
            'y': scaled_dist,
            'z': dist,  # Storing the original cosine distance for tooltips.
            'color': 'red' if option_label == chosen_option else 'grey',
            'marker': {
                'radius': 16 if option_label == chosen_option else 14,
            },
            'dataLabels': {
                'enabled': True,
                'format': option_label,
                'style': {
                    'fontSize': '16px'
                },
                "allowOverlap": True,
                "distance": 25,  # Adjusted closer to optimize space usage
                # "backgroundColor": "white" if i == 0 else None,
                "padding": 0,
                "zIndex": 10 if i == 0 else 6,
            }
        })

    chart_config = {
        "chart": {
            "polar": True,
            "type": 'scatter',
            "backgroundColor": 'white',
            "margin": [-0, 0, -0, 0],
            # "width": 300,
            "height": 380,
        },
        "title": {
            "floating": True,
            "useHTML": True,
            "text": "<span style='background-color: white; padding: 10px; font-size: 24px'>AI's intuition</span>", 
        },
        "responsive": {
            "rules": [{
                "condition": {
                    "maxWidth": 600
                },
                "chartOptions": {
                    "chart": {
                        "margin": [-15, 0, -15, 0]
                    }
                }
            }]
        },
        "tooltip": {
            "enabled": True,
            "pointFormat": "<b>{point.name}</b><br />Distance from center: {point.y:.0f}%<br />Cosine distance: {point.z:.2f}",
            "headerFormat": None,
        },
        "pane": {
            "startAngle": 0, 
            "endAngle": 360,
            "size": '92%',
        },
        "xAxis": {
            "tickInterval": 45,
            "min": 0,
            "max": 360,
            "labels": {"enabled": False}
        },
        "yAxis": {
            "min": 0,
            "max": 100,
            "labels": {"enabled": False},
            "gridLineInterpolation": "circle",
            "lineWidth": 0,
            "gridLineColor": "#CCCCCC"
        },
        "legend": {"enabled": False},
        "series": [{"name": "Options", "data": series_data, "pointPlacement": "on"}]
    }

    hct.streamlit_highcharts(chart_config)







def visualize_target_circle_backup(options_distances, chosen_option):
    fig, ax = plt.subplots(figsize=(6, 6))

    max_distance = max(dist for _, dist in options_distances)
    min_distance = min(dist for _, dist in options_distances)

    closest_option_bound = 0.5  # Closest option to be between center and first circle
    furthest_option_bound = 4 / 5  # Furthest option to be within the outer rings

    # Scale distances
    distances_scaled = [
        (dist - min_distance) / (max_distance - min_distance) * (furthest_option_bound - closest_option_bound) + closest_option_bound 
        for _, dist in options_distances
    ]

    angle_increment = 2 * np.pi / len(options_distances)
    angles = np.linspace(0, 2 * np.pi, len(options_distances), endpoint=False)  # Uniform distribution of angles

    closest_option = options_distances[0][0]

    # Sizes and color adjustments
    dot_size = 400  # Further increased dot size
    font_size = 14  # Further increased font size
    text_offset = 0.15  # Adjusted for larger dot sizes

    for (option_label, _), distance_scaled, angle in zip(options_distances, distances_scaled, angles):
        x = distance_scaled * np.cos(angle)
        y = distance_scaled * np.sin(angle)

        # Dots
        color = 'red' if option_label == chosen_option else 'lime' if option_label == closest_option else 'grey'
        ax.scatter(x, y, color=color, s=dot_size, edgecolors='black', alpha=0.9 if option_label in [chosen_option, closest_option] else 0.5)

        # Labels
        label_color = 'black' if option_label in [chosen_option, closest_option] else 'grey'
        ax.text(x, y + text_offset, f'{option_label}', color=label_color, ha='center', va='center', fontsize=font_size, weight='bold' if option_label in [chosen_option, closest_option] else 'normal')

    # Draw concentric circles as target background
    circles = np.linspace(0, 1, num=5)
    for circle in circles:
        ax.add_patch(plt.Circle((0, 0), circle, color='black', fill=False, linewidth=0.5, alpha=0.2))

    ax.set_aspect('equal', 'box')
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.axis('off')

    plt.close()

    return fig


def visualize_embeddings(get_embedding, key_terms, options, choice, target_vector, dimensions=2):
    pca = PCA(n_components=dimensions)
    terms = key_terms + [opt for opt in options if opt != choice] + [choice, "Target"]
    embeddings = [get_embedding(term) for term in terms[:-1]]
    embeddings.append(target_vector)
    
    embeddings = np.stack(embeddings)
    reduced_embeddings = pca.fit_transform(embeddings)

    fig = plt.figure(figsize=(10, 7))
    if dimensions == 3:
        ax = fig.add_subplot(111, projection='3d')
        # Plotting and text for 3D
        for i, term in enumerate(terms):
            x, y, z = reduced_embeddings[i, :3]
            ax.scatter(x, y, z, color='blue' if term in key_terms else 'grey', alpha=0.5 if term not in key_terms else 1.0, s=100)
            ax.text(x, y, z, s=f' {term}', color='blue' if term in key_terms or term == "Target" else 'grey')
    else:
        ax = fig.add_subplot(111)
        # Plotting and text for 2D
        for i, term in enumerate(terms):
            x, y = reduced_embeddings[i, :2]
            ax.scatter(x, y, color='blue' if term in key_terms else 'grey', alpha=0.5 if term not in key_terms else 1.0, s=100)
            ax.text(x, y, s=f' {term}', color='blue' if term in key_terms or term == "Target" else 'grey')

    # Highlight the player's choice in red for both 2D and 3D
    choice_index = terms.index(choice)
    if dimensions == 3:
        x, y, z = reduced_embeddings[choice_index, :3]
        ax.scatter(x, y, z, color='red', s=100)
        ax.text(x, y, z, s=f' {choice}', color='red')
    else:
        x, y = reduced_embeddings[choice_index, :2]
        ax.scatter(x, y, color='red', s=100)
        ax.text(x, y, s=f' {choice}', color='red')

    # Draw arrows
    if dimensions == 3:
        # 3D arrows
        for start, end in [(0, 1), (2, len(terms) - 1)]:
            ax.quiver(*reduced_embeddings[start], *(reduced_embeddings[end] - reduced_embeddings[start]), length=np.linalg.norm(reduced_embeddings[end] - reduced_embeddings[start]), normalize=True)
    else:
        # 2D arrows
        for start, end in [(0, 1), (2, len(terms) - 1)]:
            ax.annotate('', xy=reduced_embeddings[end, :2], xytext=reduced_embeddings[start, :2],
                        arrowprops=dict(facecolor='black', shrink=0.05))

    # General settings for both 2D and 3D
    ax.set_xticks([])
    ax.set_yticks([])
    if dimensions == 3:
        ax.set_zticks([])

    return fig
