FROM python:3.10

WORKDIR /app

COPY . .

RUN chmod +x ./wait-for-it.sh

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "script.py"]
