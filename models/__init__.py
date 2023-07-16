from pymongo import MongoClient


def initiate_mongo():
    client = MongoClient('mongodb://localhost:27017')

    db = client['backend-database']

    user_collection = db['users']
    user_schema = {
        'userID': int,
        'cartID': int,
        'username': str,
        'password': str,
        'email': str,
        'pincode': int,
        'firstname': str,
        'lastname': str,
        'phone-no': int
    }

    products_collection = db['products']
    products_schema = {
        'productID': int,
        'categoryID': int,
        'productName': str,
        'productPrice': int,
        'productRating': int,
        'productHypermedia': {
            'productImage': str,
            'productDocument': str
        }
    }

    category_collection = db['category']
    category_schema = {
        'categoryID': int,
        'products': [products_schema],
    }

    orders_collection = db['orders']
    orders_schema = {
        'orderID': int,
        'userID': int,
        'cartID': int,
        'products': [products_schema],

    }

    client.close()
