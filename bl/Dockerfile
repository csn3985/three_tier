FROM node:alpine

WORKDIR /app
EXPOSE 5000

RUN apk add --update --no-cache python3
RUN python3 -m ensurepip
RUN pip3 install flask
RUN pip3 install flask-cors
RUN pip3 install mysql-connector-python

COPY . ./

CMD ["python3", "three_tier-bl.py"] 
