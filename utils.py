import os
import json

# Environmental Variable handling for ease of testing. 

def get_env_vars() -> (list, int, str):
    if os.environ.get("SERVER_ID") is None:
        print("Missing SERVER_ID environment variable, this can be obtained by Server Settings -> Widget -> Server ID")
        exit(1)
    if os.environ.get("LUMENAUT_ROLE_ID") is None:
        print("Missing LUMENAUT_ROLE_ID environment variable, this can be obtained by Server Settings -> Roles -> Right Click Desired Role -> Copy ID")
        exit(1)
    if os.environ.get("BOT_TOKEN") is None:
        print("Missing BOT_TOKEN environment variable")
        exit(1)
        
    try:
        server_id = json.loads(os.environ.get("SERVER_ID"))
        if isinstance(server_id, int):
            server_id = [server_id]

    except Exception as e:
        print("There was an error parsing the SERVER_ID variable, please validate that is set to either an int or an array of ints formatted as \"[1234,1235]\"")
        exit(1)

    try:
        role_id = int(os.environ.get("LUMENAUT_ROLE_ID"))
        bot_token = os.environ.get("BOT_TOKEN")
        return server_id, role_id, bot_token
    except ValueError as e:
        print("Please validate that LUMENAUT_ROLE_ID is currently set to an integer")
        exit(1)

    except Exception as e:
        print("An unexpected error occured, Exception Details: " + str(e))
        exit(1)
