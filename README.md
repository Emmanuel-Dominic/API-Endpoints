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
    "All_Parcel_Orders_Are ": [
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
    "A_Specific_Parcel_Order_By_ID ": {
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
    "Specific_User_Parcels_Are ": [
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
    "Parcel_Order_Cancelled_Is": false
	}
```
* GET request for Helloworld Testing(JSON).
```
 - (/api/v1/)

 	{
    "This is ": "Challenge two API-Endpoints with Andela"
	}

```
* GET request for Users(JSON).
```
 - (/api/v1/users)

 	{
    "Parcel_Delivery_Order_Customers ": [
        {
            "Card_Number": "HD2U9DHHHOW8",
            "Email": "ematembu2@gmail.com",
            "Name": "Chosen Emmanuel",
            "Password": "pass1",
            "userId": 3
        },
        {
            "Card_Number": "HD2U9DHHHOW8",
            "Email": "ematembu@gmail.com",
            "Name": "Matembu Emmanuel",
            "Password": "pass2",
            "userId": 1
        },
        {
            "Card_Number": "9HEH9H9OH2FKA",
            "Email": "ematembu1@gmail.com",
            "Name": "Dominic Emmanuel",
            "Password": "pass3",
            "userId": 2
			}
		]
	}

```
## Acknowledgments
* Inspiration
* Andela-Uganda
* Andela-LFA (Harriet and Jude)
* Bootcamp-14Challenge-Team@Open-Andela

