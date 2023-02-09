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


### On Django/DRF

#### General
- To get a random object from a django model, you can do `ModelName.objects.all().order_by("?").first()`. Really cool!

#### Serializers
- Model serializers in DRF work very similar to how ModelForms work in Django in addition to making model fields JSON serializeable.
- You can serialize a model's methods and properties by calling their names in Meta.fields just like regular field names
- You can have multiple serializers for the exact same model based on the shape/format you want to view model data
- Also similar to Django forms, serializers can injest send data to the backend
- Other thing that serializer does is verify data that has been sent in from a POST request (checks if request data matches the format set for the model data fields) before saving data to database. Similar to `form.is_valid()`
- When you add an extra non-read-only field to a model serializer to collect data that will not be saved to the model, you can override the serializers create method or the `CreateView`'s `perform_create` method to perform custom actions with that field without saving it to the model.
- Same logic for validating form fields in django work for validating serializer fields in DRF.

#### Generics
- Django and DRF generics (generic views) abstract away commonly used views and can be used in place of writing basic views such as list and detail views. These are class based views and can be extended to add on or update their default methods/properties
- There are some generics that combine views together: e.g. `ListCreateView`. Pretty cool. Makes sense when those views use the same endpoint

### Authenticaton
From DRF docs:
- >Authentication is the mechanism of associating an incoming request with a set of identifying credentials, such as the user the request came from, or the token that it was signed with. The permission and throttling policies can then use those credentials to determine if the request should be permitted.
- > `TokenAuthentication` is appropriate for client-server setups, such as native desktop and mobile clients.
- > `SessionAuthentication` is appropriate for AJAX clients that are running in the same session context as your website.
- Implemented a `TokenAuthentication` to give py_client access to the backend since it's not an AJAX client
- *Why do we pass tokens to request headers?* 
    - to authenticaticate the user making a particular request, we need to send a token(that proves the credibility of the user?) as part of the request to the server. 
    - Tokens are created at the server side and stored in a database temporarily.
    - When making a request, token passed in the request should match what's stored with the server to authenticate the user
    - Tokens can be passed to the other parts of a request like the body. However different request types (GET, POST, etc.) could have different body formats, making things unnecessarily complicated on the client side. 
    - Headers are therefore perfect to hold such data as they are independent of request type.([source](https://stackoverflow.com/questions/40902970/why-do-we-prefer-authorization-header-to-send-bearer-token-to-server-over-other))
- when a token is deleted, the user's authentication is invalidated and they'd need to log back in to get a new token created.
- by default, the `Token` model from `django_restframework.authtoken.models` does not enforce a key expiration.
- to manage that, you can extend the model to add an expiration date, or you can use third party packages(available in DRF) to manage token expiration and deletion
- the expiration time for a token depends on what it is being used for. If a token being used for a GET request for example, it's not necessary to change it very often.
- instead of repeating particular authentication and permisison classes in each view, you can set default permissions and authentication classes for the entire project by including them in the `REST_FRAMEWORK` namespace in your django project settings

#### Permissions
- User/group-based permissions on a model can be enforced in a client by including `permissions.DjangoModelPermission` in the `permisson_classes` list in a generic api view. However permissions are only activated for `POST`, `PUT` and `DELETE` requests by default.
- To support `GET` requests or support other custom behaviours, you can create a custom model permissions by overriding the django model permissions. You can override the `perms_map` defined in the `DjangoModelPermission` class to give "view" permissions or provide custom permission codes
- You can use mixins to hold various permissions classes that will be repeated in parts of your project and not the entire project. You then add the mixin to the view class that you want the permission classes to apply to.
- *Mixins are a great way to avoid writing repeatable code*


#### ViewSets
- Instead of creating different views for various request actions on a particular model (GET, PUT, POST, etc.), you can use `ModelViewSet` from  `rest_framework.viewsets` on the model to automatically create views for all those request types. 
- Viewset can be used with a `DefaultRouter` from `rest_framework.routers` to create default routers for all the views from the viewset.



## Challenges/Surprises
- **localhost:\*/api and localhost:\*/api/ are not the same!**: I could not echo back the request body from the django backend when I sent GET a request from py_client with the endpoint localhost:\*/api. Request body was blank, even though the request was sent with json data. Later realised the url in the django backend had been configured as localhost:\*/api/. Difference is the trailing forward slash. As a result, the django backend could not get the request body from the api endpoint I made the GET request from. *Somehow there was no problem with getting a response from the django backend to the py_client??* Seems that distinction is not made when info flow is from backend to frontend.