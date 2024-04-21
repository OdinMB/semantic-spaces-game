def get_tag_data():
    '''
    Returns a dictionary of tag data. Each tag is a dictionary with the following keys:
    - display: the label that is displayed in the tag cloud
    - (optional) description: text that is displayed as a tooltip when hovering over the tag
    - (optional) menu: whether the tag should be displayed in the menu
    '''

    tag_data = {
        "intro": {
            "display": "Tutorial",
            "menu": False
        },
        "satirical": {
            "display": "Satire",
            "description": "We already knew that fast food empires herald civilisational decline. It's fun to have it confirmed by AI, though."
        },
        "weird": {
            "display": "Daring connections",
            "description": "Apply levels of nobility to animals and superhero relationships to concepts of happiness."
        },
        "bias": {
            "display": "AI biases",
            "description": "AI models can be biased in various ways. This theme explores these biases."
        }
    }
    return tag_data