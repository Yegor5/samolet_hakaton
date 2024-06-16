FROM python:3.12-slim

COPY ./requirements.txt /root/server/requirements.txt

RUN chown -R root:root /root/server

WORKDIR /root/server
RUN pip3 install --no-cache-dir -r requirements.txt

COPY ./ ./
RUN chown -R root:root ./

RUN chmod +x main.py
CMD ["python3", "main.py"]
