import os
import site
import re

def check_for_opengraph_tags(content):
    """Check if OpenGraph meta tags are present in the HTML content."""
    return '<meta property="og:' in content

def modify_index_html(index_html_path, custom_title, custom_meta_tags, force=False):
    """Modify the index.html file to include custom title and meta tags."""
    try:
        with open(index_html_path, 'r', encoding='utf-8') as file:
            original_content = file.read()
        print(f"Successfully read from {index_html_path}.")

        if check_for_opengraph_tags(original_content) and not force:
            print("OpenGraph tags already present, no modifications made.")
            return

        new_content = re.sub(r'<title>.*?</title>', custom_title, original_content, flags=re.DOTALL)
        head_end_pos = new_content.find('</head>')
        modified_content = new_content[:head_end_pos] + custom_meta_tags + new_content[head_end_pos:]

        with open(index_html_path, 'w', encoding='utf-8') as file:
            file.write(modified_content)
        print(f"Successfully modified {index_html_path}.")
    except Exception as e:
        print(f"Error modifying {index_html_path}: {e}")

def find_streamlit_static_path():
    """Find the streamlit static path in site-packages."""
    try:
        site_packages = next(p for p in site.getsitepackages() if 'site-packages' in p)
        streamlit_static_path = os.path.join(site_packages, 'streamlit', 'static')
        return streamlit_static_path
    except StopIteration:
        print("Could not locate 'site-packages' directory.")
        return None

def check_index_html():
    # Custom HTML content
    custom_title = "<title>Semantic Spaces - A game about language and AI</title>"
    custom_meta_tags = """
    <meta name="description" content="Compare your semantic intuition to a modern AI language model. Is 'civilization in decline' semantically closer to 'social media influencers' or 'fast food empires'?">
    
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

    <!-- Open Graph Meta Tags -->
    <meta property="og:url" content="https://semantics.fun">
    <meta property="og:type" content="website">
    <meta property="og:title" content="Semantic Spaces - A game about language and AI">
    <meta property="og:description" content="Is 'civilization in decline' semantically closer to 'social media influencers' or 'fast food empires'? Compare your intuition to a modern AI language model.">
    <meta property="og:image" content="https://github.com/OdinMB/semantic-spaces-game/blob/main/img/labyrinth.jpg?raw=true">
    <!-- Twitter Meta Tags -->
    <meta name="twitter:card" content="summary_large_image">
    <meta property="twitter:domain" content="semantics.fun">
    <meta property="twitter:url" content="https://semantics.fun">
    <meta name="twitter:title" content="Semantic Spaces - A game about language and AI">
    <meta name="twitter:description" content="Is 'civilization in decline' semantically closer to 'social media influencers' or 'fast food empires'? Compare your intuition to a modern AI language model.">
    <meta name="twitter:image" content="https://github.com/OdinMB/semantic-spaces-game/blob/main/img/labyrinth.jpg?raw=true">
    """

    streamlit_static_path = find_streamlit_static_path()
    if streamlit_static_path:
        index_html_path = os.path.join(streamlit_static_path, 'index.html')
        if os.path.exists(index_html_path):
            modify_index_html(index_html_path, custom_title, custom_meta_tags)
        else:
            print(f"The specified path does not exist: {index_html_path}")
    else:
        print("Unable to proceed without the streamlit static path.")

if __name__ == "__main__":
    check_index_html()
