'''
    1. 인가코드 받기
    https://kauth.kakao.com/oauth/authorize
    
    - client_id         : REST API KEY
    - redirect_uri      : https://localhost.com
    - response_type     : code


    응답결과 : code (인가코드)
'''
a = 'de52792f84e5e05dbe770a85dfee64eb'
b = 'https://localhost.com'
c = 'code'

req_url = 'https://kauth.kakao.com/oauth/authorize?client_id={}&redirect_uri={}&response_type={}'.format(a,b,c)
print(req_url)


# 인가코드 요청 URL
# https://kauth.kakao.com/oauth/authorize?client_id=636004344b306ca0cc7283d41ffc4f1b&redirect_uri=https://localhost.com&response_type=code


# 인가코드
auth_code = 'Ctymdk8LvrwG5kRQ5G_gbeilLm-pOrenPTeL-eWqI00_lbPbLV2UJh3JsSc-fszg8vG0XQopyNgAAAGI4f0_Dw'

# 액세스 토큰 받기
url = 'https://kauth.kakao.com/oauth/token'

# 요청 정보
data = {
    'grant_type'   : 'authorization_code',
    'client_id'    : a,                 # REST API KEY
    'redirect_url' : b,
    'code'         : auth_code          # 인가코드
}

import requests

# POST 방식으로 URL 요청
response = requests.post(url, data=data)


# 요청 실패
if response.status_code != 200:
    print('요청 실패!', response.json())
# 요청 성공
else:
    result = response.json()
    token = result['access_token']
    print(result)
    print(token)

# access_token
# RE36ArgIeE2F1VY1l-ucdp0qS7hN9CgR5xe37teACj102gAAAYjiAWUb


