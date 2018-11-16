# API-Endpoints

A set of API endpoints defined to use data structures
to store data in memory (without use a database).

## Getting Started Requirements

```
 https://www.pivotaltracker.com/n/projects/2215959
```
```
 https://dashboard.heroku.com/apps/sendit-api-endpoint

``` 

[![Build Status](https://travis-ci.com/ManuelDominic/API-Endpoints.svg?branch=develop)](https://travis-ci.com/ManuelDominic/API-Endpoints) 
[![Coverage Status](https://coveralls.io/repos/github/ManuelDominic/API-Endpoints/badge.svg?branch=develop)](https://coveralls.io/github/ManuelDominic/API-Endpoints?branch=develop)
 

## Postman Requests
```
* POST request for create Parcel Delivery Order(JSON).
 - (/api/v1/parcels)
```
### Set Up Postman
* First thing’s first: You need to download Postman. It’s free, it’s fun and it works on Mac, Windows and Linux machines.

### automated api testing - postman
* Make sure you have the API documentation for your application handy.

### run APP
* Commandline run:
```
	& export FLASK_APP=app.py

	& export FLASK_ENV=development

	& flask run
```

### automated api testing - post
* Using Test Manager, go ahead and structure json format requirements;
```
	{
      "commentDescription": "Newyear", 
      "destination": "Newkampala", 
      "item": "Newlaptop", 
      "locationPicker": "Newyork", 
      "status": true, 
      "userId": 1, 
      "weight": "3.9kg"
      
	}
```
* Once you structure your tests pass, status = 201 with;
```	
	{
    "Message": "Parcel delivery created successfully",
    "OrderId": 6
	}
```

## Other Tested Requests.

* GET request for get all parcel Delivery Orders(JSON).
```
 - (/api/v1/parcels/)

	{
	    "ALL_PARCEL_ORDERS ": [
	        {
	            "commentDescription": "Thanks",
	            "destination": "Kamyokya",
	            "item": "hp-laptop",
	            "locationPicker": "America",
	            "parcelId": 1,
	            "status": true,
	            "userId": 2,
	            "weight": "5.7kg"
	        },
	        {
	            "commentDescription": "Required",
	            "destination": "kyengera",
	            "item": "Dell-laptop",
	            "locationPicker": "Dubia",
	            "parcelId": 2,
	            "status": true,
	            "userId": 3,
	            "weight": "5.8kg"
	        },
	        {
	            "commentDescription": "See you",
	            "destination": "Rubaga",
	            "item": "Tablet",
	            "locationPicker": "Jamaica",
	            "parcelId": 3,
	            "status": true,
	            "userId": 2,
	            "weight": "1.4kg"
	        },
	        {
	            "commentDescription": "Thanks",
	            "destination": "Wakiso",
	            "item": "Router",
	            "locationPicker": "London",
	            "parcelId": 4,
	            "status": true,
	            "userId": 1,
	            "weight": "3.6kg"
	        }
	    ]
	}

```
* GET request to get a specific parcel(JSON).
```
  - (/api/v1/parcels/'parcelId=1'/)

	{

    "SPECIFIC_PARCEL ": {
        "commentDescription": "Thanks",
        "destination": "Kamyokya",
        "item": "hp-laptop",
        "locationPicker": "America",
        "parcelId": 1,
        "status": true,
        "userId": 2,
        "weight": "5.7kg"
    	}
	}

```
* GET request to get parcel Delivery Orders for specific User(JSON).
```
 - (/api/v1/users/'userId=2'/parcels)

    {
    "PARCELS": [
        {
            "commentDescription": "Thanks",
            "destination": "Kamyokya",
            "item": "hp-laptop",
            "locationPicker": "America",
            "parcelId": 1,
            "status": true,
            "userId": 2,
            "weight": "5.7kg"
        },
        {
            "commentDescription": "See you",
            "destination": "Rubaga",
            "item": "Tablet",
            "locationPicker": "Jamaica",
            "parcelId": 3,
            "status": true,
            "userId": 2,
            "weight": "1.4kg"
	        }
	    ]
	}

```
* PUT request for Cancel parcel Delivery Order(204-NO CONTENT).
```
 - (/api/v1/parcels/'parcelId=1'/cancel)-@(200 JSON)

 	{
    "Parcel Cancelled": false
	}
```
* GET request for Helloworld Testing(JSON).
```
 - (/api/v1/)

 	{
    "EMMANUEL ": "API-Endpoints"
	}

```
## Acknowledgments
* Inspiration
* Andela-Uganda
* Andela-LFA
* Bootcamp-14Challenge-Team@Open-Andela

