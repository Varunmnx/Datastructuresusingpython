import sys
from tkinter import W
import clipboard
import json

def save_items(filepath,data): # create json
    with open(filepath,"w") as f:
     json.dump(data,f)

def load_json(filepath): # read from that json
    with open(filepath,"r") as f:
        json.load(f)


if len(sys.argv)==2:
  command = sys.argv[1]
  if command == "save":
      print("save")
  if command == "load":
      print("load")
  if command == "list":
      print("list") 
  else:
      print("unknown command")      
else:
    print("please type a command")      
      