import os

def get_file_name():
    # Check if the riddles_wip.txt file exists
    # If it exists and is not empty, use it
    if os.path.exists("riddles_wip.txt"):
        if os.stat("riddles_wip.txt").st_size != 0:
            return "riddles_wip"
    return "riddles"