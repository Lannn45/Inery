import os
import json
import datetime as dt
import pytz
from dotenv import load_dotenv
from api.cline import Cline
from api import keys
from api.utils import *


def transact(id):
    load_dotenv()
    cli = Cline()

    name_account = os.environ["inery_account"]
    pkey = os.environ["private_key"]
    key = keys.INRKey(pkey)
    content1 = {"id": id, "user": name_account, "data": "data {id}"}
    content2 = {"id": id}
    content3 = {"id": id, "data": "data {id}"}
    content4 = {"id": id}



 action_create = {"account": name_account,"name": "create","authorization": 
                    [{"actor": name_account,"permission": "active"}],
    "data": cli.abi_json_to_bin(name_account, "create", content1)["binargs"]}
    transaction_create = {"actions": [action_create],"expiration": str((dt.datetime.utcnow() + dt.timedelta(seconds=60)).replace(tzinfo=pytz.UTC))}

    tx_create = cli.push_transaction(transaction_create, key, broadcast=True)
    print("Create")
    print(json.dumps(tx_create, indent=4))

    
if __name__ == "__main__":
     transact(332)
