import sys 
import clipboard
import json

# from clipboardauto import SAVED_DATA
# from clipboardauto import load_data

SAVED_DATA='clipboard66.json'


def save_data(filepath, data):
    with open(filepath, "w") as f:
         json.dump(data, f)

def load_data(filepath):
    try: 
        with open(filepath,"r") as f:
            data = json.load(f)
            return data
    except: 
        return print("cannot open")   

if len(sys.argv) == 2:
    command=sys.argv[1]
    data = load_data(SAVED_DATA)

    if command == 'save': 
        key = input("enter key: ")
        data[key] = clipboard.paste()     
        save_data(SAVED_DATA,data)
       