import os
import json
import datetime as dt
import pytz
from dotenv import load_dotenv
from api.cline import Cline
from api import keys
from api.utils import *


def read(id):
    load_dotenv()
    cli = Cline()

    name_account = os.environ["inery_account"]
    pkey = os.environ["private_key"]
    key = keys.INRKey(pkey)
    content1 = {"id": id, "user": name_account, "data": "data {id}"}
    content2 = {"id": id}
    content3 = {"id": id, "data": "data {id}"}
    content4 = {"id": id}

##Read_Transaction
    action_read =  {"account": name_account, "name": "read","authorization":
                   [{"actor":name_account, "permission":"active"}],
    "data": cli.abi.json.to.bin(name_account, "read", content2)["binargs"]}
    transaction_read = {"actions": [action_read],"expiration": str((dt.datetime.utcnow() + dt.timedelta(seconds=60)).replace(tzinfo=pytz.UTC))}

    tx_read = cli.push.transaction(transactioan_read, key, broadcast=True)
    print("Read")
    print(json.dumps(tx_read, indent=4))

    if __name__ == "__main__":
     read(333)