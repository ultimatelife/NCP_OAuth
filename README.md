# NCP OAuth

## 1. NCP_OAuth
1. Construct
    - base_url: str
    - oauth_consumer_key: str
    - secret_key: str
    - params: dict
        - 위의 것들 이외의 추가 parameter 가 있을 경우 추가한다.
2. get_encoded_parmas(self, info: dict, http_method: str = "GET")
    - info: dict
        - API 요청시 필요한 parameter 들을 넣는다.
    - http_method: str
        - 사용한 HTTP Method 를 입력한다.
        - Default 는 GET 이다.   
    
## 2. Example :
1. NCP_OAuth 만 사용
```
from NCP_OAuth.OAuth import OAuth

oauth = OAuth(base_url="https://api.ncloud.com/geolocation/"
                  , oauth_consumer_key="oauth_consumer_key"
                  , secret_key="secret_key"
                  , params=None)

encoded_parmas = oauth.get_encoded_parmas(info={
    "action": "getLocation"
    , "ip": "209.209.212.112"
    , "responseFormatType": "json"
})

print(requests.get("https://api.ncloud.com/geolocation/", params=encoded_parmas).json())
```

2. NCP_OAuth Module 을 사용하여 NCP API 개발
```
class GeolocationAPI(object):
    base_url: str = "https://beta-api.ncloud.com/geolocation/"

    def __init__(self, oauth_consumer_key: str, secret_key: str, params: dict = None):
        self.oauth = OAuth(base_url=GeolocationAPI.base_url
                           , oauth_consumer_key=oauth_consumer_key
                           , secret_key=secret_key
                           , params=params)

    def get_geolocation_info(self, info: dict, http_method: str = "GET"):
        encoded_parmas = self.oauth.get_encoded_parmas(info=info, http_method=http_method)
        return requests.get(GeolocationAPI.base_url, encoded_parmas).json()
```