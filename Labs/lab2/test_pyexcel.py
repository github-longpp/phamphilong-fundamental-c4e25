import pyexcel
from collections import OrderedDict

data = [
    OrderedDict({
        "Name" : "Huy",
        "Age" : 30
    }),
    OrderedDict({
        "Name" : "Quan",
        "Age" : 25        
    })
]

pyexcel.save_as(records = data, dest_file_name = "sample.xlsx")