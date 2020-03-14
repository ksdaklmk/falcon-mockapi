import falcon
import json
import requests
import datetime
import time

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class Tools:

    def getDateTimeISO(self):
        utc_offset_sec = time.altzone if time.localtime().tm_isdst else time.timezone
        utc_offset = datetime.timedelta(seconds=-utc_offset_sec)
        return datetime.datetime.now().replace(tzinfo=datetime.timezone(offset=utc_offset)).isoformat(timespec='milliseconds')


class OrftInquiry:

    payloadHeaders = {
        'API-Key': 'l71ad26790bd0f4b9d81b215670b54fb3e',
        'X-Client-Transaction-DateTime': Tools.getDateTimeISO(self=None),
        'X-Client-Transaction-ID': 'e45dbd32-95a3-4ed3-b6fb-4ad36d1a6bcc',
        'Content-Type': 'application/json'
    }
    url = 'https://sandbox.api.krungsri.net/transfer/orft/inquiry'

    def on_post(self, req, resp):
        self.reqMessage = req.media
        self.response = requests.post(self.url, headers=self.payloadHeaders, json=self.reqMessage, verify=False)
        resp.body = self.response.json()
        resp.status = str(self.response.status_code)


class OrftConfirm:

    tryCount = 0
    responseMessage1 = {
        "error": {
            "code": "55",
            "message": "This is response code 55",
            "messageTH": "-",
            "serverDateTime": Tools.getDateTimeISO(self=None),
            "clientTransactionID": "a01fa0ae-190a-49d5-9cc1-465f9f9ab0dc",
            "serverTransactionID": "47865470-7a51-444f-b676-679c83000302"
        }
    }
    responseMessage2 = {
        "error": {
            "code": "98",
            "message": "This is response code 98",
            "messageTH": "-",
            "serverDateTime": Tools.getDateTimeISO(self=None),
            "clientTransactionID": "a01fa0ae-190a-49d5-9cc1-465f9f9ab0dc",
            "serverTransactionID": "47865470-7a51-444f-b676-679c83000302"
        }
    }

    def on_post(self, req, resp):
        if self.tryCount % 3 == 0:
            resp.body = json.dumps(self.responseMessage1)
        else:
            resp.body = json.dumps(self.responseMessage2)
        resp.status = falcon.HTTP_400
        self.tryCount += 1


class Dopa:
    
    responseMessage = {
        "code": "0",
        "description": "สถานะปกติ"
    }

    def on_post(self, req, resp):
        resp.body = json.dumps(self.responseMessage)
        resp.status = falcon.HTTP_200


class Ndid:

    payloadHeaders = {
        'Content-Type': 'application/json'
    }
    payload = {
        "result": {
            "reference_number": None,
            "diis_status": "timeout",
            "ndid_status": "pending"
        },
        "success": True,
        "errorcode": "0000"
    }
    url = 'https://miraimob-uat.krungsri.net/mirai_tbs/ndid_request_callback.tml'
    responseMessage = {
        "error": {
            "code": "-200",
            "message": "Cannot contact backend",
            "messageTH": "-",
            "serverDateTime": Tools.getDateTimeISO(self=None),
            "clientTransactionID": "a01fa0ae-190a-49d5-9cc1-465f9f9ab0dc",
            "serverTransactionID": "47865470-7a51-444f-b676-679c83000302"
        }
    }

    def on_get(self, req, resp):
        self.payload['result']['reference_number'] = req.get_param('rp')
        # resp.body = json.dumps(self.payload)
        # resp.status = falcon.HTTP_200
        self.response = requests.post(self.url, headers=self.payloadHeaders, json=self.payload, verify=False)
        resp.body = self.response.json()
        resp.status = str(self.response.status_code)

    def on_post(self, req, resp):
        resp.body = json.dumps(self.responseMessage)
        resp.status = falcon.HTTP_400


# Initiates the instance
api = falcon.API()
orft_inquiry = OrftInquiry()
orft_confirm = OrftConfirm()
ndid = Ndid()
dopa = Dopa()

# Adds API routes
# api.add_route('/transfer/orft/inquiry', orft_inquiry)
# api.add_route('/transfer/orft/confirm', orft_confirm)
api.add_route('/native/ndid/utility/idp', ndid)
api.add_route('/native/ndid/rp/request', ndid)
api.add_route('/ndid/callback/', ndid)
# api.add_route('/external/dopa/idcard/chip', dopa)
# api.add_route('/external/dopa/idcard/laser', dopa)
