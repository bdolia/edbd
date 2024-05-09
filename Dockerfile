FROM python:3.13.0b1-slim
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN python setup.py install
ENTRYPOINT [ "python", "./main.py" ]
EXPOSE 8080