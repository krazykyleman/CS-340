#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 17:22:42 2023

@author: kylewucik_snhu
"""

from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, USER, PASS):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        #USER = 'aacuser'
        #PASS = 'SNHU1234'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 32369
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]


    # Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            self.database.animals.insert_one(data)  # data should be dictionary  
            return True
          
        else:
            raise Exception("Nothing to save, because data parameter is empty")


    # Create method to implement the R in CRUD.
    def read(self, data):
        if data is not None:
            result = self.collection.find(data)
            return [item for item in result]
        else:
            raise Exception("Query parameter is empty")
            
            
    # Update method to implement the U in CRUD
    def update(self, query, new_data):
        if query is not None and new_data is not None:
            result = self.collection.update_many(query, new_data)
            return result.modified_count # Return the number of documents updated
        else:
            raise Exception("Query or new data parameter is empty")
    
    
    # Delete method to implement the D in CRUD
    def delete(self, query):
        if query is not None:
            result =  self.collection.delete_many(query)
            return result.deleted_count # Return the number of documents deleted
        else:
            raise Exception("Query parameter is empty")
    
    
    
    
    