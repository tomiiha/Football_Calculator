import pymongo
import ast

def conn_establish():
    # Pass credentials out of credentials file.
    credentials = ast.literal_eval(open('credentials.txt','r').read())
    conn_url = "mongodb+srv://" + credentials['username'] + ":" + credentials['password'] + "@sandbox.r1tr0.mongodb.net/" + credentials['db_name'] + "?retryWrites=true&w=majority"
    client = pymongo.MongoClient(conn_url)
    return conn_test(client)

# Run connection - test and run, otherwise close connection straight.
def conn_test(client):
    try:
        client.server_info()
        return print("Connection Established")
    except:
        print("Connection failed")
        close_conn(client)

# Terminate connection.
def close_conn(client):
    try:
        client.close()
        return
    except:
        return print("No Connection Established")
