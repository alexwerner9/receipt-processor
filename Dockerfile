FROM python:3.12.5-bookworm

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT ["gunicorn"]
CMD ["-b", "0.0.0.0:8000", "-w", "4", "app:create_app()"]
