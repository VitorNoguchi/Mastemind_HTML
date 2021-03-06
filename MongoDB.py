#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pymongo import MongoClient

class DB:
    def __init__(self):
        self.cliente = ''
        self.banco = ''
        self.album = ''

    def start_conn(self, base, collection):
        self.cliente = MongoClient('mongodb://localhost:27017/')
        self.banco = self.cliente[base]
        self.album = self.banco[collection]

    def insertion_mongo(self, collection, sample):
        collection.insert_one(sample)

    def find_mongo(self, collection, name, email):
        data = collection.find({'Name': name, 'Email': email})
        for a in data:
            if a['Result'] != 'GAME OVER' and a['Result'] != 'VOCE VENCEU!':
                return a

    def findall(self, collection):
        data = collection.find()
        return data

    def update(self, collection, name, email, target_number, attempt, result, attempt_list):
        data = DB().find_mongo(collection, name, email)
        collection.update(data, {'Name': name, 'Email': email,
                        'Target': target_number,'Count': attempt,'Result': result, 'past_attempt': attempt_list})

if __name__ == "__main__":
    conn = DB()
    conn.start_conn('Name', 'Target')
    print(DB().find_mongo(conn.album, 'Vitor', 'vshojifn@gmail.com'))
    #for a in DB().find_mongo(conn.album, 'Vitor', 'vshojifn@gmail.com'):
    #    print(a)