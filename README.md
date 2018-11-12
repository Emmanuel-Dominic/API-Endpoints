# API-Endpoints

A set of API endpoints defined to use data structures
to store data in memory (without use a database).

## Getting Started Requirements
<<<<<<< HEAD

###You Need to install:
```
 >*Server side Framework:*(Insert tool .eg vscode, pycharm)
 >*Linting Library:* (Insert tool .eg pylint)
 >*Style Guide:* (Insert tool .eg How python is writen)
 >*Testing Framework:* (insert tool .eg pytest)
 ```

```
>https://itsfoss.com/install-pycharm-ubuntu/
>https://docs.pylint.org/en/1.6.0/installation.html
>https://www.pythonforbeginners.com/style-guide/
>https://docs.pytest.org/en/latest/fixture.html
```

```
###1.On Pivotal Tracker, create user stories to set up and test API endpoints
that do the following using data structures
```
```
 >Create a parcel delivery order
 >Get all parcel delivery orders
 >Get a specific parcel delivery order
 >Cancel a parcel delivery order
```
```
###2.On Pivotal Tracker create stories to capture any other tasks not captured above.
The tasks can be feature, bug or chore for this challenge.
```
```
###3.Setup the server side of the application using the specified framework © Andela Confidential4.
Setup linting library and ensure that your work follows the specified style guide requirements
```
```
###5.Setup the test framework
```
```
###6.Version your API using URL versioning starting, with the letter “v”. 
A simple ordinal number would be appropriate and avoid dot notation such as 2.5. 
An example of this will be: https://somewebapp.com/api/v1/users
```
```
###7.Using separate branches for each feature, create version 1 (v1) of your 
RESTful API to power front-end pages
```
```
###8.At the minimum, you should have the following API endpoints working: EndPoint Functionality
```
```
>GET /parcels Fetch all parcel delivery orders
>GET /parcels/<parcelId> Fetch a specific parcel delivery order
>GET /users/<userId>/parcels Fetch all parcel delivery orders by a specific user
>PUT /parcels/<parcelId>/cancel Cancel the specific parcel delivery order
>POST /parcels Create a parcel delivery order
```
```
###9.Write tests for the API endpoints
```
```
###10.Ensure to test all endpoints and see that they work using Postman.
 ```
```
###11.Integrate TravisCI for Continuous Integration in your repository (with ReadMe badge).
```
```
###12.Integrate test coverage reporting (e.g. Coveralls) with a badge in the ReadMe.
```
 ```
###13.Obtain CI badges (e.g. from Code Climate and Coveralls) and add to ReadMe .
 ```
```
###14.Ensure the app gets hosted on Heroku.
=======
```
 https://www.pivotaltracker.com/n/projects/2215959
```
[![Build Status](https://travis-ci.com/ManuelDominic/API-Endpoints.svg?branch=develop)](https://travis-ci.com/ManuelDominic/API-Endpoints) [![Coverage Status](https://coveralls.io/repos/github/ManuelDominic/API-Endpoints/badge.svg?branch=develop)](https://coveralls.io/github/ManuelDominic/API-Endpoints?branch=develop)
[![Test Coverage](https://api.codeclimate.com/v1/badges/a99a88d28ad37a79dbf6/test_coverage)](https://codeclimate.com/github/codeclimate/codeclimate/test_coverage)

```
 https://dashboard.heroku.com/apps/sendit-api-endpoint
>>>>>>> 37f39ede0e30d7e8a6a3bc2c0d50d23708ad2b57
```  

## Deployment

This project is hosted on Heroku.

## Built With

* [Flask](http://flask.pocoo.org/) - The web framework used
* [Code Climate](https://maven.apache.org/) - Used to generate CI Badges
* [Coveralls](https://coveralls.io/) - Used to generate converage reporting Badge
* [Travis CI](https://travis-ci.org/) - Used to generate Travis CI Badge


## Written by:

* **Matembu Emmanuel Dominic**-*Workflow* @-ematembu2@gmail.com

## License

This project is licensed under [@Andela](https://andela.com/fellowship/) challenge-2 Bootcamp-14

## Acknowledgments
* Inspiration
* Andela-Uganda
* Bootcamp-14Challenge-Team@Open-Andela

