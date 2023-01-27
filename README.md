# GTF：Github to Feishu
通过webhook将GitHub仓库的变动推送到飞书平台
## 使用
1. 安装依赖
```
pip install -r requirements.txt
```
2. 打开main.py文件，修改第40行，将引号内的内容替换为你的飞书机器人的webhook地址
3. 运行程序
```python
python main.py
```
4. 在你的仓库的wenhook设置中，按照如下内容填写
![image](https://user-images.githubusercontent.com/53247097/215059457-56f2f8ee-9d8b-4913-a177-cff92d5a9a40.png)

5. Enjoy it :)
如果你有其他疑问，可以查阅飞书官方文档，或者提issue
如果你有一些很棒的点子，也欢迎你提issue或者pr
