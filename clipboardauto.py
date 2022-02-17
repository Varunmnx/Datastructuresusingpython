import sys
import clipboard
import json


if len(sys.argv)==2:
  command = sys.argv[1]
  if command == "save":
      print("save")
  if command == "load":
      print("load")
  if command == "list":
      print("list")    
      