FROM python:3.9

WORKDIR /app
COPY server.py /app/
COPY cert.pem /app/
COPY key.pem /app/

RUN pip install flask

EXPOSE 443

CMD ["python", "server.py"]
