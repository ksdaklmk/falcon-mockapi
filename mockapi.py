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
        resp.body = self.response.text
        resp.status = str(self.response.status_code)


class OrftConfirm:

    tryCount = 1
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


class NdidList:

    idp_headers = {
        'API-Key': 'l726df48afe64548c9acb2430af3484009',
        'X-Client-Transaction-DateTime': Tools.getDateTimeISO(self=None),
        'X-Client-Transaction-ID': 'e45dbd32-95a3-4ed3-b6fb-4ad36d1a6bcc',
        'Content-Type': 'application/json'
    }
    error_response = {
        "error": {
            "code": "-200",
            "message": "Cannot contact backend",
            "messageTH": "-",
            "serverDateTime": Tools.getDateTimeISO(self=None),
            "clientTransactionID": "a01fa0ae-190a-49d5-9cc1-465f9f9ab0dc",
            "serverTransactionID": "47865470-7a51-444f-b676-679c83000302"
        }
    }
    list_idp_url = 'https://sit.api.krungsri.net/native/ndid/utility/idp'

    def on_post(self, req, resp):
        call_api = False # False: returns error, True: forward request to actual API GW
        if call_api:
            self.req_message = req.media
            self.response = requests.post(self.list_idp_url, headers=self.idp_headers, json=self.req_message, verify=False)
            resp.body = self.response.text
            resp.status = str(self.response.status_code)
        else:
            resp.body = json.dumps(self.error_response)
            resp.status = falcon.HTTP_400


class NdidRequest:

    idp_headers = {
        'API-Key': 'l726df48afe64548c9acb2430af3484009',
        'X-Client-Transaction-DateTime': Tools.getDateTimeISO(self=None),
        'X-Client-Transaction-ID': 'e45dbd32-95a3-4ed3-b6fb-4ad36d1a6bcc',
        'Content-Type': 'application/json'
    }
    error_response = {
        "error": {
            "code": "-200",
            "message": "Cannot contact backend",
            "messageTH": "-",
            "serverDateTime": Tools.getDateTimeISO(self=None),
            "clientTransactionID": "a01fa0ae-190a-49d5-9cc1-465f9f9ab0dc",
            "serverTransactionID": "47865470-7a51-444f-b676-679c83000302"
        }
    }
    request_idp_url = 'https://sit.api.krungsri.net/native/ndid/rp/request'

    def on_post(self, req, resp):
        call_api = True # False: returns error, True: forward request to actual API GW
        if call_api:
            self.req_message = req.media
            self.response = requests.post(self.request_idp_url, headers=self.idp_headers, json=self.req_message, verify=False)
            resp.body = self.response.text
            resp.status = str(self.response.status_code)
        else:
            resp.body = json.dumps(self.error_response)
            resp.status = falcon.HTTP_400


class NdidGetData:

    error_response = {
        "error": {
            "code": "-200",
            "message": "Cannot contact backend",
            "messageTH": "-",
            "serverDateTime": Tools.getDateTimeISO(self=None),
            "clientTransactionID": "a01fa0ae-190a-49d5-9cc1-465f9f9ab0dc",
            "serverTransactionID": "47865470-7a51-444f-b676-679c83000302"
        }
    }
    idp_headers = {
        'API-Key': 'l726df48afe64548c9acb2430af3484009',
        'X-Client-Transaction-DateTime': Tools.getDateTimeISO(self=None),
        'X-Client-Transaction-ID': 'e45dbd32-95a3-4ed3-b6fb-4ad36d1a6bcc',
        'Content-Type': 'application/json'
    }
    get_data_url = 'https://sit.api.krungsri.net/native/ndid/rp/data'

    def on_post(self, req, resp):
        call_api = True # False: returns error, True: forward request to actual API GW
        if call_api:
            self.req_message = req.media
            self.response = requests.post(self.get_data_url, headers=self.idp_headers, json=self.req_message, verify=False)
            resp.body = self.response.text
            resp.status = str(self.response.status_code)
        else:
            resp.body = json.dumps(self.error_response)
            resp.status = falcon.HTTP_400


# Initiates the instance
api = falcon.API()
orft_inquiry = OrftInquiry()
orft_confirm = OrftConfirm()
ndid_list = NdidList()
ndid_request = NdidRequest()
dopa = Dopa()
as_data = NdidGetData()

# Adds API routes
# api.add_route('/transfer/orft/inquiry', orft_inquiry)
# api.add_route('/transfer/orft/confirm', orft_confirm)
api.add_route('/native/ndid/utility/idp', ndid_list)
api.add_route('/native/ndid/rp/request', ndid_request)
api.add_route('/native/ndid/rp/data', as_data)
# api.add_route('/external/dopa/idcard/chip', dopa)
# api.add_route('/external/dopa/idcard/laser', dopa)
