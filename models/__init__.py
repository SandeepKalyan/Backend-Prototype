from pymongo import MongoClient

user_schema = {
        'cartID': int,
        'username': str,
        'password': str,
        'email': str,
        'pincode': int,
        'firstname': str,
        'lastname': str,
        'phone-no': int
    }

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

orders_schema = {
        'orderID': int,
        'userID': int,
        'cartID': int,
        'products': [products_schema],

    }

category_schema = {
        'categoryID': int,
        'products': [products_schema],
    }

def initiate_mongo():
    client = MongoClient('mongodb://localhost:27017')

    db = client['backend-database']

    user_collection = db['users']

    products_collection = db['products']

    category_collection = db['category']

    orders_collection = db['orders']

    client.close()
