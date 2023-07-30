FROM python:3.11
WORKDIR /Emerging-Technologies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "emergingfront.py"]
