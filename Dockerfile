FROM python:3.12.5-bookworm

COPY . .

ENTRYPOINT ["python3"]
CMD ["app/api.py"]
