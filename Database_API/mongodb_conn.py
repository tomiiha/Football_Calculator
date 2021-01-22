import pymongo
import ast

def conn_establish():
    # Pass credentials out of credentials file.
    credentials = ast.literal_eval(open('credentials.txt','r').read())
    conn_url = "mongodb+srv://" + credentials['username'] + ":" + credentials['password'] + "@maindb.r1tr0.mongodb.net/" + credentials['db_name'] + "?retryWrites=true&w=majority"
    client = pymongo.MongoClient(conn_url)
    return client

# Run connection - test and run, otherwise close connection straight.
def conn_start():
    try:
        status_msg = conn_establish().server_info()
        conn_time = status_msg['operationTime']
        return conn_time
    except:
        return "Connection failed"

# Terminate connection on-demand.
def conn_close():
    try:
        conn_establish().close()
        return 'Connection closed'
    except:
        return print("No Connection Established")
