# UpGrad Chatbot for restaurant search from the team of
#     Arup Mondal, Kiran C Kumar, Kousik Das & Viswajit Iyer

### Introduction

This bot searches for restaurants provides the outout as a list.

Some examples are as follows:
```
User: Hola
Bot: Hi there! How may I help you?
User: I’m hungry. Looking out for some good restaurants
Bot: In what location?
User: bengaluru
Bot: What kind of cuisine would you like to have?
1. Chinese
2. Mexican
3. Italian
4. American
5. Thai
6. North Indian
User: I’ll prefer thai
Bot: What's the average budget for two people?
1. Lesser than Rs. 300
2. Rs. 300 to 700
3. More than 700
User: 300-700 range
Bot: Showing you top rated restaurants:
1. Restaurant 1 in Area 1. And the average price for two people here is: XXX
Rs
2. Restaurant 1 in Area 1. And the average price for two people here is: XXX
Rs
3. .
4. .
5. .
Bot: Should I send you details of all the restaurants on email?
User: yes. Please send it to ahbcdj@dkj.com
Bot: Sent
```


### Installation

Create a virtual environment for python 3.6.5
```sh
$ conda create -n <name of virtual env> python=3.6.5
```

Activate the virtual environment created above 
```sh
$ conda activate <name of virtual env> 
```

Download this repo and cd into the folder

Install the dependencies
```sh
$ pip install -r requirements.txt
```
Install the spacy en library
```sh
$ python -m spacy download en
```

### Training the RASA 

In order to train the interpreter, run the following command

```sh
$ python -m rasa_nlu.train -c nlu_config.yml --data data/data.json -o models --fixed_model_name nlu --project current --verbose
```

In order to train RASA CORE, run the following command

```sh
$ python -m rasa_core.train -d domain.yml -s data/stories.md -o models/current/dialogue -c policies.yml
```

### Running the RASA on commandline

In order to run rasa action server, execute
```sh
$ python -m rasa_core_sdk.endpoint --actions actions
```


In order to run rasa at commandline, execute
```sh
$ python -m rasa_core.run -d models/current/dialogue -u models/current/nlu --endpoints endpoints.yml
```
