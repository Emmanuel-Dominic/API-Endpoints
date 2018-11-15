from flask import Flask, jsonify, request, Response, json


def create_app(config=None):
    """
    This function allows to pass different configuration.
    """
    app = Flask(__name__)

    @app.route('/api/v1/')
    def helloworld():
        """
        This function returns {{'EMMANUEL ': 'API-Endpoints'}}.
        """
        return jsonify({'EMMANUEL ': 'API-Endpoints'}), 200

    @app.route('/api/v1/parcels', methods=['GET'])
    def get_parcels():
        """
        This function returns/Fetch all parcel delivery orders.
        """
        return jsonify({'ALL_PARCEL_ORDERS ': parcels}), 200

    @app.route('/api/v1/parcels/<int:parcelId>', methods=['GET'])
    def get_parcel(parcelId):
        """
        This function returns/Fetch a specific parcel delivery order.
        """
        for parcel in parcels:
            if parcel['parcelId'] == parcelId:
                return jsonify({'SPECIFIC_PARCEL ':parcel}), 200
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
            return jsonify({'PARCELS': user_parcels}), 200
        return jsonify({'Error':"Not found"}), 404


    @app.route('/api/v1/parcels/<int:parcelId>/cancel', methods=['PUT'])
    def cancel_parcel(parcelId):
        """
        This function returns Cancelled the specific parcel delivery order.
        """
        for parcel in parcels:
            if parcel["parcelId"] == parcelId:
                parcel["status"] = False
                return jsonify({'Cancelled': parcels}), 204


    @app.route('/api/v1/parcels', methods=['POST'])
    def create_parcel():
        '''
        creates a new parcel order
        '''
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
            data1 = {'Message': "Parcel delivery created successfully",\
             'OrderId': parcel.get('parcelId')}
            parcels.append(parcel)
            response = Response(response = json.dumps(data1)), 201
            return response
        data2 = {"error": "Invalid object" }
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


    parcels = [
        {'parcelId': 1, 'item': 'laptop', 'weight': '3.9kg', 'userId': 2,\
        'commentDescription':'thanks', 'locationPicker': 'america',\
        'destination': 'kyengera', 'status': True },
        {'parcelId': 2, 'item': 'laptop', 'weight': '3.9kg', 'userId': 3,\
        'commentDescription':'thanks', 'locationPicker': 'america',\
         'destination': 'kyengera', 'status': True },
        {'parcelId': 3, 'item': 'laptop4', 'weight': '3.9kg', 'userId': 2,\
        'commentDescription':'thanks', 'locationPicker': 'america',\
         'destination': 'kyengera', 'status': True },
        {'parcelId': 4, 'item': 'laptop', 'weight': '3.9kg', 'userId': 1,\
        'commentDescription':'thanks', 'locationPicker': 'america',\
         'destination': 'kyengera', 'status': True }
        ]

    users = [
        {'name': 'joseph', 'userId': 1, 'email': 'joseph@gmail.com',\
         'password': 'pass1'},
        {'name': 'emmanuel', 'userId': 2, 'email': 'emmanuel@gmail.com',\
         'password': 'pass2'},
        {'name': 'annmary', 'userId': 3, 'email': 'annmary@gmail.com',\
         'password': 'pass3'}
        ]


    return app
    

if __name__ == '__main__':
    app = create_app()
    app.run(debug = True)
