import requests

# get_email = "enj17hz5@yzm.de"
# print(type(get_email))


def login(get_email):
    url = "https://api.distribute.ai/internal/auth/login"
    headers = {'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
               'Content-Type': 'application/json',
               'Accept': '*/*',
               'Host': 'api.distribute.ai',
               'Connection': 'keep-alive'
               }
    payload = {
        "email": get_email,
        "password": "admin123",
        "rememberSession": True
    }
    print("请求参数:", payload)
    try:
        response = requests.post(url=url, json=payload, headers=headers)
        response.raise_for_status()  # 如果响应错误，抛出异常
        if response.status_code == 200:
            token = response.json().get("token")
            print("获取到的token:", token)
            return token
        else:
            print("错误响应:", response.status_code, response.text)
            return None
    except requests.exceptions.RequestException as e:
        print("请求发生错误:", e)
        return None


# if __name__ == '__main__':
#     login(get_email)