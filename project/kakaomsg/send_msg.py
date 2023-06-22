import json
import requests

access_token = 'RE36ArgIeE2F1VY1l-ucdp0qS7hN9CgR5xe37teACj102gAAAYjiAWUb'   # 김도연
# access_token = 'xoc41BoospqMEB1kH9Bb83U4FVvLSSqbRWqiq8J5CiolDQAAAYjiJC57' # 강찬욱
# access_token = '2U9e1tZAKSRe3ZtNa_x64bNccYRtGVoL6YWszISTCj1z7AAAAYjh_qUD' # 선생님

url = 'https://kapi.kakao.com/v2/api/talk/memo/default/send'

# header 정보
headers = {
    'Authorization' : 'Bearer ' + access_token
}

# 요청 정보
temp = {
            # "object_type": "text",
            # "link": {
            #     "web_url": "https://www.youtube.com",
            #     "mobile_web_url": "https://www.youtube.com"
            # "button_title": "바로 확인"
            # },
            "object_type": "feed",
            "content" : {
                "title" : input("제목 : "),
                "description" : input("내용 : "),
                "image_url": input("img url : "),
                "image_width": 640,
                "image_height": 640,
                'link' : { 
                    "web_url" : 'https://youtube.com',          # PC 카톡의 URL
                    "mobile_web_url" : 'https://youtube.com'    # 모바일 URL
                }
            },
            "buttons" : [
            {
                    "title" : "바로 가기",
                    'link' : { 
                        "web_url" : 'https://youtube.com',          # PC 카톡의 URL
                        "mobile_web_url" : 'https://youtube.com'    # 모바일 URL
                    }
                }
            ]
        }

data = {
    'template_object' : json.dumps( temp )      # 파이썬 객체를 JSON 문자열로 직렬화하는 함수
}

# 나에게 카카오 메시지 보내기
response = requests.post(url, headers=headers, data=data)
print(response.status_code)
