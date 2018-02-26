import base64
import hashlib
import hmac
import operator
import random
import time
import urllib.parse
from datetime import datetime


class OAuth:
    def __init__(self, base_url: str, oauth_consumer_key: str, secret_key: str, params: dict = None):
        self.oauth_consumer_key = oauth_consumer_key
        self.secret_key = secret_key
        self.oauth_nonce = str(random.randrange(-98385302039483772298912, 98385302039483772298912))
        self.base_url = base_url
        self.params = {
            "oauth_consumer_key": self.oauth_consumer_key,
            "oauth_nonce": 10,
            "oauth_signature_method": "HMAC-SHA1",
            "oauth_version": "1.0",
        }
        if params is not None:
            self.params.update(params)

    def get_encoded_parmas(self, info: dict, http_method: str = "GET"):
        signature: str = self.get_signature(info=info, http_method=http_method)
        self.params["oauth_signature"] = signature
        return self.params

    # def get_signature(self, http_method: str, response_format_type: str = "json"):
    def get_signature(self, info: dict, http_method: str = "GET") -> str:
        self.params["oauth_timestamp"] = str(time.mktime(datetime.today().timetuple())).replace(".0", "")
        # self.params["responseFormatType"] = info["response_format_type"]
        self.params.update(info)

        params_str = ""
        for key, item in sorted(self.params.items(), key=operator.itemgetter(0)):
            params_str = "&".join([params_str, f"{key}={item}"])
        params_str = params_str[1:]

        encoded_base_url = urllib.parse.quote_plus(self.base_url)
        encoded_params_str = urllib.parse.quote_plus(params_str)
        merged_params = "&".join([http_method, encoded_base_url, encoded_params_str])

        signature = self.transform_digest(merged_params, self.secret_key)
        return signature

    def transform_digest(self, message, key):
        key = bytes(key + "&", 'UTF-8')
        message = bytes(message, 'UTF-8')
        digester = hmac.new(key, message, hashlib.sha1)
        signature = base64.urlsafe_b64encode(digester.digest())
        return str(signature, 'UTF-8').replace("_", "/").replace("-", "+")
