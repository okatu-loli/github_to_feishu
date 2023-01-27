import json
from flask import Flask, request
import requests

app = Flask(__name__)


@app.route('/', methods=['POST'])
def handle_github_webhook():
    # 获取github webhook发送的json数据
    github_json = request.get_json()
    repo = github_json["repository"]["name"]
    commit_msg = github_json["head_commit"]["message"]
    commit_url = github_json["head_commit"]
    repo_url = github_json["repository"]["html_url"]
    # 解析github webhook发送的json数据，生成飞书API支持的json数据
    feishu_json = {
        "msg_type": "post",
        "content": {
            "post": {
                "zh_cn": {
                    "title": "项目更新通知",
                    "content": [
                        [{
                            "tag": "text",
                            "text": f"项目 {repo} 有更新：\n提交内容：\n{commit_msg}\n"
                        },
                            {
                                "tag": "a",
                                "text": f"请点击查看仓库",
                                "href": repo_url
                            }
                        ]
                    ]
                }
            }
        }
    }
    # 飞书机器人的webhook地址
    url = '修改这里'
    headers = {'Content-Type': 'application/json'}
    # 将飞书API支持的json数据转换为字符串并发送给飞书机器人
    jsons = json.dumps(feishu_json)
    response = requests.post(url, jsons, headers=headers)
    if response.status_code != 200:
        print(response.text)
    return '', 200


if __name__ == '__main__':
    app.run()