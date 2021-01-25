import pymongo
import ast
from ipywidgets import widgets, Dropdown, interact, interact_manual, Button, Output
import json
import os

# UI Bits
collection_box=Dropdown(
    options=['team_details'],
    description='Pick Collection:',
    layout={'width': 'max-content'},
    style = {'description_width': 'initial'},
    disabled=False)

class Connect(object):
    def conn_establish():
        # Pass credentials out of credentials file.
        credentials = ast.literal_eval(open('credentials.txt','r').read())
    
        # Create client string to pass to connection open/close.
        conn_url = "mongodb+srv://" + credentials['username'] + ":" + credentials['password'] + "@maindb.r1tr0.mongodb.net/" + credentials['db_name'] + "?retryWrites=true&w=majority"
        client = pymongo.MongoClient(conn_url)
        return client

# Run connection - test and run.
def conn_start():
    try:
        status_msg = Connect.conn_establish().server_info()
        conn_time = status_msg['operationTime']
        return Connect.conn_establish()
    except:
        return "Connection failed"
    
    # Terminate connection on-demand.
def conn_close():
    try:
        Connect.conn_establish().close()
        return 'Connection closed'
    except:
        return print("No Connection Established")
    
def collection_operation():
    return

@interact_manual(collection = collection_box)
def choose_features(collection):
    if collection == 'team_details':
        
        # Find team_list file for insertion - load json.
        data_filenames = [data_file for data_file in os.listdir() 
                      if data_file.endswith('.json') and 'team_list' in data_file]
        with open(data_filenames[0]) as json_file:
            data = json.load(json_file)
            
        # Place all team details in db.    
        for x in data:
            Connect.conn_establish().collection.insert_one(x)
        
        # Note if completed.
        return "Team data updated"
    else:
        return "Nothing done"
