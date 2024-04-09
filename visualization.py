import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.decomposition import PCA

def visualize_target_circle(options_distances, chosen_option):
    fig, ax = plt.subplots(figsize=(6, 6))

    # Obtain distances from the second closest to the furthest option
    closest_dist = options_distances[0][1]
    furthest_dist = options_distances[-1][1]

    # Define visual bounds
    inner_visual_bound = 0.1  # Offset for the closest option for better visibility
    outer_visual_bound = 0.8  # Middle of the outer ring, leaving space to the bounds

    # Calculate visual distances scaling
    scale_factor = (outer_visual_bound - inner_visual_bound) / (furthest_dist - closest_dist)

    # Calculate angles for options, excluding the closest to avoid clustering at the center
    angle_increment = 2 * np.pi / (len(options_distances) - 1)
    angles = [angle_increment * i for i in range(1, len(options_distances))]  # Start from 1 to exclude closest

    # Process options for visual placement
    for i, (option_label, dist) in enumerate(options_distances):
        if i == 0:  # Closest option placed at the center
            x, y = 0, 0
        else:
            visual_dist = inner_visual_bound + (dist - closest_dist) * scale_factor
            angle = angles[i-1]  # Corrected indexing for angle
            x = visual_dist * np.cos(angle)
            y = visual_dist * np.sin(angle)

        # Distinguish the chosen option
        color = 'red' if option_label == chosen_option else 'grey'
        dot_size = 500 if option_label == chosen_option else 350
        label_offset = 0.1  # Additional space between dot and label for clarity
        font_size = 14

        ax.scatter(x, y, color=color, s=dot_size, zorder=3)  # zorder for layering
        ax.text(x, y - label_offset, option_label, color=color, ha='center', va='center', fontsize=font_size, zorder=4)

    # Draw concentric circles for reference, with spacing to the image bounds
    for r in np.linspace(0, outer_visual_bound, 5):
        ax.add_patch(plt.Circle((0, 0), r, color='black', fill=False, linewidth=0.5, alpha=0.2, zorder=2))

    ax.set_aspect('equal', 'box')
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.axis('off')

    plt.close()

    return fig



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
