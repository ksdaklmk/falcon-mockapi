import json
import requests
import datetime
import time
import uvicorn

from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, Json
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class Tools:

    def getDateTimeISO(self):
        utc_offset_sec = time.altzone if time.localtime().tm_isdst else time.timezone
        utc_offset = datetime.timedelta(seconds=-utc_offset_sec)
        return datetime.datetime.now().replace(tzinfo=datetime.timezone(offset=utc_offset)).isoformat(timespec='milliseconds')


class SenderTxnModel(BaseModel):
    account_no: str = Field(..., alias='accountNo')
    account_name: str = Field(..., alias='accountName')
    account_type: str = Field(..., alias='accountType')
    sender_tax: str = Field(..., alias='senderTax')
    

class ReceiverTxnModel(BaseModel):
    account_no: str = Field(..., alias='accountNo')
    account_type: str = Field(..., alias='accountType')
    bank_code: str = Field(..., alias='bankCode')


class OrftInquiry(BaseModel):
    sender: SenderTxnModel
    receiver: ReceiverTxnModel
    amount: float
    qr_flag: str = Field(..., alias='qrFlag')


class OrftConfirm(BaseModel):
    pass


class ChannelIdModel(BaseModel):
    channel_id: str


class NdidPayloadModel(BaseModel):
    namespace: str
    identifier: str
    min_ial: float
    min_aal: float
    product_id: str


class ListIdpModel(BaseModel):
    header: ChannelIdModel
    payload: NdidPayloadModel


api = FastAPI(title="Mirai Mock APIs", description="List of mock APIs for Mirai interface tesing", version="1.0", debug=True)
try_count = 1

@api.post("/ndid", name="NDID interface", description="")
async def idp_list():
    response_message = {
        "error": {
            "code": "-200",
            "message": "Cannot contact backend",
            "messageTH": "-",
            "serverDateTime": Tools.getDateTimeISO(self=None),
            "clientTransactionID": "a01fa0ae-190a-49d5-9cc1-465f9f9ab0dc",
            "serverTransactionID": "47865470-7a51-444f-b676-679c83000302"
        }
    }

    return JSONResponse(status_code=400, content=response_message)


@api.post("/transfer/orft/inquiry", name="Actual account fund transfer inquiry transaction", description="")
async def orft_inquiry(res: OrftInquiry):
    payload_headers = {
        'API-Key': 'l71ad26790bd0f4b9d81b215670b54fb3e',
        'X-Client-Transaction-DateTime': Tools.getDateTimeISO(self=None),
        'X-Client-Transaction-ID': 'e45dbd32-95a3-4ed3-b6fb-4ad36d1a6bcc',
        'Content-Type': 'application/json'
    }
    url = 'https://sandbox.api.krungsri.net/transfer/orft/inquiry'
    payload = {
	    "sender": {
		    "accountNo": "3007035315",
		    "accountName": "PANUWAT BOVORNCHAICHARN",
		    "accountType": "15",
		    "senderTax": "3129900009286"
	    },
	    "receiver": {
		    "accountNo": "1112000099",
		    "accountType": "99",
		    "bankCode": "014"
	    },
	    "amount": 10.00,
	    "qrFlag": "N"
    }
    response = requests.post(url, headers=payload_headers, json=payload, verify=False)
    return response.json()


@api.post("/transfer/orft/confirm", name="Actual account fund transfer confirm transaction", description="")
async def orft_confirm(res: OrftConfirm):
    global try_count
    response_98 = {
        "error": {
            "code": "98",
            "message": "This is response code 98",
            "messageTH": "-",
            "serverDateTime": Tools.getDateTimeISO(self=None),
            "clientTransactionID": "a01fa0ae-190a-49d5-9cc1-465f9f9ab0dc",
            "serverTransactionID": "47865470-7a51-444f-b676-679c83000302"
        }
    }
    response_55 = {
        "error": {
            "code": "55",
            "message": "This is response code 55",
            "messageTH": "-",
            "serverDateTime": Tools.getDateTimeISO(self=None),
            "clientTransactionID": "a01fa0ae-190a-49d5-9cc1-465f9f9ab0dc",
            "serverTransactionID": "47865470-7a51-444f-b676-679c83000302"
        }
    }

    if try_count % 3 == 0:
        response = JSONResponse(status_code=400, content=response_55)
    else:
        response = JSONResponse(status_code=400, content=response_98)
    try_count += 1
    
    return response

