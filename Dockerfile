FROM python:3.11
# 拉取一个基础镜像，基于python3.11
MAINTAINER 千石
# 维护者信息
RUN cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo 'Asia/Shanghai' >/etc/timezone
# 设置容器时间，有的容器时区与我们的时区不同，可能会带来麻烦
ENV LANG C.UTF-8
# 设置语言为utf-8
COPY requirements.txt /tmp/requirements.txt
COPY ./app/main.py /app/main.py
RUN ["pip3", "install", "-r", "/tmp/requirements.txt"]
# 根据requirement.txt下载好依赖包
EXPOSE 5000
# EXPOSE 指令是声明运行时容器提供服务端口，这只是一个声明，在运行时并不会因为这个声明应用就会开启这个端口的服务。
# 此处填写5000，是因为我们上面的app.py提供的web服务就需要使用5000端口
ENTRYPOINT ["python3","/app/main.py"]