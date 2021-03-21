FROM python:3.8-slim-buster
EXPOSE 8501
RUN apt-get update && \
     apt-get -y --no-install-recommends install \
     libgomp1
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["streamlit","run"]
CMD ["app.py"]