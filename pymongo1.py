# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 18:17:20 2021

@author: SWARNAVA
"""

import pymongo

client=pymongo.MongoClient('mongodb://127.0.0.1:27017/')

mydb=client['employment']
information=mydb.employmentinformation

record={"firstname":"Swarnava",
        "lastname":"Mukherjee",
        "status":"single"}

information.insert_one(record)

record1=[{"firstname":"Swarnava",
        "lastname":"Mukherjee",
        "status":"single"},
         
         {"firstname":"Swarnava1",
        "lastname":"Mukherjee1",
        "status":"single1"},
        
        {"firstname":"Swarnava2",
        "lastname":"Mukherjee2",
        "status":"single2"}]

information.insert_many(record1)