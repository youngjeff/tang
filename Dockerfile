FROM docker.io/frolvlad/alpine-python3
ENV PATH /usr/local/bin:$PATH
ENV PATH /home:$PATH
ADD . /home
WORKDIR /home
RUN pip install -i https://mirrors.aliyun.com/pypi/simple -r requirements.txt
