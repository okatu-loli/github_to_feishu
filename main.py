import json
from flask import Flask, request
import requests

app = Flask(__name__)


@app.route('/', methods=['POST'])
def handle_github_webhook():
    # 获取github webhook发送的json数据
    github_json = request.get_json()
    repo = github_json.get("repository", {}).get("name", "未获取到仓库名")
    commit_msg = github_json.get("head_commit", {}).get("message", "未获取到commit的内容，可能为非commit操作，点击下方的commit地址可在浏览器查看具体错误")
    commit_url = github_json.get("head_commit", {}).get("url", "未获取到commit的链接，可能为非commit操作")
    repo_url = github_json.get("repository", {}).get("html_url", "未获取到仓库链接")
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
                                "text": f"请点击查看仓库\n",
                                "href": repo_url
                            },
                            {
                                "tag": "a",
                                "text": f"请点击查看commit地址\n",
                                "href": commit_url
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
    print(jsons)
    response = requests.post(url, jsons, headers=headers)
    if response.status_code != 200:
        print(response.text)
    return '', 200


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)