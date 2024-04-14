import os

def get_file_name():
    # Check if the riddles_wip.json file exists
    # If it exists and is not empty, use it
    if os.path.exists("riddles_wip.json"):
        # if riddles_wip.json is smaller than 150 bytes, it's empty
        if os.stat("riddles_wip.json").st_size > 160:
            return "riddles_wip"
    return "riddles"