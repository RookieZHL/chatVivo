from flask import Flask, render_template, request, jsonify
import uuid
import time
import requests
from auth_util import gen_sign_headers

app = Flask(__name__)

# 配置信息
APP_ID = '2025802261'
APP_KEY = 'MtJDOAqjvfQiwmFW'
URI = '/vivogpt/completions'
DOMAIN = 'api-ai.vivo.com.cn'
METHOD = 'POST'

def get_vivo_response(prompt):
    params = {
        'requestId': str(uuid.uuid4())
    }
    print(f"Request ID: {params['requestId']}")

    data = {
        'prompt': prompt,
        'model': 'vivo-BlueLM-TB-Pro',
        'sessionId': str(uuid.uuid4()),
        'extra': {
            'temperature': 0.9
        }
    }
    
    headers = gen_sign_headers(APP_ID, APP_KEY, METHOD, URI, params)
    headers['Content-Type'] = 'application/json'

    url = f'https://{DOMAIN}{URI}'
    print(f"Request URL: {url}")
    print(f"Request Headers: {headers}")
    print(f"Request Data: {data}")

    try:
        response = requests.post(url, json=data, headers=headers, params=params)
        print(f"Response Status Code: {response.status_code}")
        print(f"Response Text: {response.text}")

        if response.status_code == 200:
            res_obj = response.json()
            print(f"Response JSON: {res_obj}")
            if res_obj['code'] == 0 and res_obj.get('data'):
                return res_obj['data']['content']
            else:
                return f"API返回错误: {res_obj.get('message', '未知错误')}"
        else:
            return f"请求失败，状态码: {response.status_code}"
    except Exception as e:
        print(f"发生错误: {str(e)}")
        return f"发生错误: {str(e)}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '')
    if not user_message:
        return jsonify({'error': '消息不能为空'})
    
    response = get_vivo_response(user_message)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True) 