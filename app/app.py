from flask import Flask, jsonify, request, Response, json


def create_app(config=None):
    """
    This function allows to pass different configuration.
    """
    app = Flask(__name__)

    @app.route('/api/v1/')
    def helloworld():
        """
        This function returns {{'This is ': 'Challenge two API-Endpoints with Andela'}}.
        """
        return jsonify({'This is ': 'Challenge two API-Endpoints with Andela'}), 200

    @app.route('/api/v1/parcels', methods=['GET'])
    def get_parcels():
        """
        This function returns/Fetch all parcel delivery orders.
        """
        return jsonify({'All_Parcel_Orders_Are ': parcels}), 200

    @app.route('/api/v1/parcels/<int:parcelId>', methods=['GET'])
    def get_parcel(parcelId):
        """
        This function returns/Fetch a specific parcel delivery order.
        """
        for parcel in parcels:
            if parcel['parcelId'] == parcelId:
                return jsonify({'A_Specific_Parcel_Order_By_ID ':parcel}), 200
        return jsonify({'Error':"Not found"}), 404

    @app.route('/api/v1/users/<int:userId>/parcels', methods=['GET'])
    def user_parcels(userId):
        """
        This function returns/Fetch all parcel delivery orders by a specific user.
        """
        user_parcels = []
        for parcel in parcels:
            if parcel['userId'] == userId:
                user_parcels.append(parcel)
        if len(user_parcels) != 0:
            return jsonify({'Specific_User_Parcels_Are ': user_parcels}), 200
        return jsonify({'Error':"Not_found"}), 404


    @app.route('/api/v1/parcels/<int:parcelId>/cancel', methods=['PUT'])
    def cancel_parcel(parcelId):
        """
        This function returns Cancelled the specific parcel delivery order.
        """
        for parcel in parcels:
            if parcel["parcelId"] == parcelId:
                parcel["status"] = False
                return jsonify({'Parcel_Order_Cancelled_Is': parcel['status']}), 204



    @app.route('/api/v1/parcels', methods=['POST'])
    def create_parcel():
        '''
        creates a new parcel order
        '''
        if not request.content_type == 'application/json':
            return jsonify({"failed": 'Content-type must be application/json'}), 401
        request_data = request.get_json()
        if validation(request_data):
            parcel = {
                'parcelId': len(parcels) + 1,
                'item': request_data['item'],
                'weight': request_data['weight'],
                'userId': request_data['userId'],
                'destination': request_data['destination'],
                'locationPicker': request_data['locationPicker'],
                'commentDescription': request_data['commentDescription'],
                'status': request_data['status']
                }
            data1 = {'Message': "Parcel delivery created successfully", 'OrderId': parcel.get('parcelId')}
            parcels.append(parcel)
            response = Response(response = json.dumps(data1)), 201
            return response
        data2 = {"Error": "Invalid object" }
        response = Response(json.dumps(data2),400)
        return response

    def validation(newparcel):
        """
        This function checks for parcel delivery order input if valid.
        """
        if "item" in newparcel and "weight" in newparcel and\
         "destination" in newparcel and "locationPicker" in newparcel and\
          "commentDescription" in newparcel and "status" in newparcel: 
            return True
        else:
            return False


    @app.route('/api/v1/users')
    def get_user():
        """
            This function returns all users
        """
        return jsonify({"Parcel_Delivery_Order_Customers ": users}),200


    parcels = [
        {
            "commentDescription": "Thanks",
            "destination": "Kamyokya",
            "item": "hp-laptop",
            "locationPicker": "America",
            "parcelId": 1,
            "status": True,
            "userId": 2,
            "weight": "5.7kg"
        },
        {
            "commentDescription": "Required",
            "destination": "kyengera",
            "item": "Dell-laptop",
            "locationPicker": "Dubia",
            "parcelId": 2,
            "status": True,
            "userId": 3,
            "weight": "5.8kg"
        },
        {
            "commentDescription": "See you",
            "destination": "Rubaga",
            "item": "Tablet",
            "locationPicker": "Jamaica",
            "parcelId": 3,
            "status": True,
            "userId": 2,
            "weight": "1.4kg"
        },
        {
            "commentDescription": "Thanks",
            "destination": "Wakiso",
            "item": "Router",
            "locationPicker": "London",
            "parcelId": 4,
            "status": True,
            "userId": 1,
            "weight": "3.6kg"
        }
    ]


    users = [
        {"Name": 'Chosen Emmanuel', "Card_Number": 'HD2U9DHHHOW8', "Email": 'ematembu2@gmail.com', "userId": 3, "Password": 'pass1'},
        {"Name": 'Matembu Emmanuel', "Card_Number": 'HD2U9DHHHOW8', "Email": 'ematembu@gmail.com',"userId": 1, "Password": 'pass2'},
        {"Name": 'Dominic Emmanuel', "Card_Number": '9HEH9H9OH2FKA', "Email": 'ematembu1@gmail.com',"userId": 2, "Password": 'pass3'}
    ]


    return app
    

if __name__ == '__main__':
    app = create_app()
    app.run(debug = True)
