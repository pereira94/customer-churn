FROM python:3.8-slim-buster
EXPOSE 8501
RUN apt-get update && \
     apt-get -y --no-install-recommends install -y\
     libgomp1\
     git
RUN git clone https://github.com/pereira94/customer-churn.git 
WORKDIR /customer-churn
RUN pip install -r requirements.txt
ENTRYPOINT ["streamlit","run"]
CMD ["app.py"]