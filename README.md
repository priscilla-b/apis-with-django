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