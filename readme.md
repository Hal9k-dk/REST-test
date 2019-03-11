# REST-test

This is a very simple flask app, used for testing the [ESP8266-restclient](https://github.com/Hal9k-dk/esp8266-restclient) library
It responds 200 "OK" to successful requests, and appends the value of json variable "test" and test headers.

```
 OK[test][h1][h2]
``` 

it returns 400 if the headers are supplied but aren't "one" and "two" respectively.

### Dependencies
* flask
* flask-restful
* python 2.6 - 3.6 (not 3.7)

The requirements.txt is a pip freeze and known to work with python3.6

### Usage
In order to run this, set up a virtualenv and install the requirements:

```bash
git clone https://github.com/Hal9k-dk/REST-test.git
cd REST-test
python3.6 -m venv RESTtest
source RESTtest/bin/activate
pip install -r requirements.txt
python app.py
```

This should run the api on localhost:5000