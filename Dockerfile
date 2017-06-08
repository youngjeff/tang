FROM docker.io/torz/django
ENV PATH /usr/local/bin:$PATH
ENV PATH /home:$PATH
ADD . /home
WORKDIR /home
RUN pip install -i https://mirrors.aliyun.com/pypi/simple -r requirements.txt
EXPOSE 8000
RUN python manage.py migrate
CMD python manage.py runserver
