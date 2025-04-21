import requests
import json
import time
import webbrowser
from auth_util import gen_sign_headers

# 配置信息
APP_ID = '2025802261'
APP_KEY = 'MtJDOAqjvfQiwmFW'
DOMAIN = 'api-ai.vivo.com.cn'

def generate_image(prompt):
    # 提交绘图任务
    submit_uri = '/api/v1/task_submit'
    submit_params = {}
    submit_data = {
        'height': 1024,
        'width': 768,
        'prompt': prompt,
        'styleConfig': '7a0079b5571d5087825e52e26fc3518b',
        'userAccount': 'thisistestuseraccount'
    }

    submit_headers = gen_sign_headers(APP_ID, APP_KEY, 'POST', submit_uri, submit_params)
    submit_headers['Content-Type'] = 'application/json'

    submit_url = f'http://{DOMAIN}{submit_uri}'
    submit_response = requests.post(submit_url, data=json.dumps(submit_data), headers=submit_headers)
    
    if submit_response.status_code != 200:
        print(f"提交任务失败: {submit_response.status_code} {submit_response.text}")
        return None

    submit_result = submit_response.json()
    if submit_result['code'] != 200:
        print(f"提交任务失败: {submit_result['msg']}")
        return None

    task_id = submit_result['result']['task_id']
    print(f"任务已提交，task_id: {task_id}")

    # 查询任务进度
    progress_uri = '/api/v1/task_progress'
    progress_params = {'task_id': task_id}
    progress_headers = gen_sign_headers(APP_ID, APP_KEY, 'GET', progress_uri, progress_params)

    uri_params = '&'.join([f"{k}={v}" for k, v in progress_params.items()])
    progress_url = f'http://{DOMAIN}{progress_uri}?{uri_params}'
    
    while True:
        progress_response = requests.get(progress_url, headers=progress_headers)
        if progress_response.status_code != 200:
            print(f"查询进度失败: {progress_response.status_code} {progress_response.text}")
            return None

        progress_result = progress_response.json()
        if progress_result['code'] != 200:
            print(f"查询进度失败: {progress_result['msg']}")
            return None

        if progress_result['result']['finished']:
            image_url = progress_result['result']['images_url'][0]
            print(f"图片生成完成！URL: {image_url}")
            webbrowser.open(image_url)
            return image_url

        print("图片正在生成中，请稍候...")
        time.sleep(2)  # 每2秒查询一次进度

def main():
    prompt = input("请输入图片描述（例如：一只梵高画的猫）: ")
    if not prompt:
        print("描述不能为空！")
        return
    
    print("开始生成图片...")
    image_url = generate_image(prompt)
    if image_url:
        print("图片生成成功！")
    else:
        print("图片生成失败！")

if __name__ == '__main__':
    main() 