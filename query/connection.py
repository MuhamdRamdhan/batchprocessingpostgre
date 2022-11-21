import os
import json
import psycopg2

from sqlalchemy import create_engine

def config(): 
    path = os.getcwd()
    with open(path+'/'+'config.json') as file :
        print(json.load(file)['marketplace_prod'])

config()