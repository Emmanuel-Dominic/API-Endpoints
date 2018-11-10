from flask import Flask, jsonify, request, Response, json


def create_app(config=None):
    app = Flask(__name__)

    @app.route('/')
    def helloworld():
        return jsonify({'EMMANUEL ': 'API-Endpoints'}),200

    @app.route('/parcels', methods=['GET'])
    def get_parcels():
        return jsonify({'ALL_PARCEL_ORDERS ': parcels}), 200

    @app.route('/parcels/<int:parcelId>', methods=['GET'])
    def get_parcel(parcelId):
        for parcel in parcels:
            if parcel['parcelId'] == parcelId:
                return jsonify({'SPECIFIC_PARCEL ':parcel}), 200
        return jsonify({'Error':"Not found"}), 404

    @app.route('/users/<int:userId>/parcels', methods=['GET'])
    def user_parcels(userId):
        user_parcels = []
        for parcel in parcels:
            if parcel['userId'] == userId:
                user_parcels.append(parcel)
        if len(user_parcels) != 0:
            return jsonify({'PARCELS': user_parcels}), 200
        return jsonify({'Error':"Not found"}), 404


    @app.route('/parcels/<int:parcelId>/cancel', methods=['PUT'])
    def cancel_parcel(parcelId):
        for parcel in parcels:
            if parcel["parcelId"] == parcelId:
                parcel["status"]= False
                return jsonify({'Cancelled': parcels}), 200

    @app.route('/parcels', methods=['POST'])
    def create_parcel():
        request_data = request.get_json()
        if is_valid_request(request_data):
            parcel = {'parcelId': len(parcels) + 1,'item': request_data['item'],\
                'weight': request_data['weight'],'userId': request_data['userId'],\
                'destination': request_data['destination'],'locationPicker': request_data['locationPicker'],\
                'commentDescription': request_data['commentDescription'],'userId': request_data['userId'],\
                'status': request_data['status']}
            parcels.append(parcel)
            response = Response("", 201, mimetype="application/json")
            response.headers['Location'] = "parcels/" + str(parcel['id'])
            return jsonify({'msg': 'parcel delivery requests created'},parcel)
        
        bad_object = {
            "error": "Invalid Parcel delivery order object"
        }
        response = Response(json.dumps(bad_object), status=400,\
         mimetype="appliation/json")
        return response


    def is_valid_request(newparcel):
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
    app.run(port=5000)
