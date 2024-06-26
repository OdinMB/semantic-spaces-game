def get_group_data():
    '''
    Returns a dictionary of group data. Each group is a dictionary with the following keys:
    - label: the label that is displayed above the riddle
    - riddles: a list of riddle ids
    - sequence: how many riddles are shown in sequence before the group is considered complete
    - (optional) note: a note that is displayed with the results of riddles in this group
    '''

    group_data = {
        "gender_jobs": {
            "label": "Gender - Jobs",
            "riddles": [9, 10],
            "sequence": 2,
            "note": ""
        },
        "race": {
            "label": "Race",
            "riddles": [19, 20, 21],
            "sequence": 3,
            "note": ""
        },
        "religion": {
            "label": "Religion",
            "riddles": [23, 24, 25],
            "sequence": 3,
            "note": ""
        }
    }
    return group_data