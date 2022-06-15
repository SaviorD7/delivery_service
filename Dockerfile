FROM python:3.9

COPY . /app
WORKDIR /app

# install requirements
RUN apt-get update
#RUN apt-get install telnet
#RUN apt-get install net-tools
RUN pip install -r requirements.txt


# expose the app port
EXPOSE 8020

# dev command
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8020"]

# run the app server in production
#CMD ["uvicorn", "adapter:flower", "--host", "0.0.0.0", "--port", "8020"]

