# apis-with-django

Code from tutorial on building APIs with python and django.

Source: [Coding for Entrepreneurs on Youtube](https://www.youtube.com/watch?v=c708Nf0cHrs)

## Project Structure
- */backend*: contains the django backend, including the django rest framework
    - */cfehome*:
    - *.manage.py*: created by django for project administrative tasks
- */py_client*: consumes the django backend


## Stuff I Learnt

### Setting up project environment
- recommended to use LTS version of Django(and other libraries) for long-term projects as they're more secure, stable and reliable.


### On APIs
- not all APIs are web-based, e.g. library apis, apis on devices, etc. 
- REST APIs are specific web-based APIs(use HTTP requests)
- A normal http request will respond with an html page(or image or video), but a rest api http request usually responds with data in a JSON format. Sometimes response is in XML or other formats.
- A normal http request renders a response for human comsumption but REST APIs are designed mostly for one software to communicate with another software
- REST APIs can be consumed on all kinds of different clients regardless of technology
- You can send data (params, json) with a GET request and can then be used at the server side.


## Challenges/Surprises
- **localhost:\*/api and localhost:\*/api/ are not the same!**: I could not echo back the request body from the django backend when I sent GET a request from py_client with the endpoint localhost:\*/api. Request body was blank, even though the request was sent with json data. Later realised the url in the django backend had been configured as localhost:\*/api/. Difference is the trailing forward slash. As a result, the django backend could not get the request body from the api endpoint I made the GET request from. *Somehow there was no problem with getting a response from the django backend to the py_client??* Seems that distinction is not made when info flow is from backend to frontend.