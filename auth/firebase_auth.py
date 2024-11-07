import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase Admin SDK (if not already initialized)
try:
    firebase_admin.get_app()
except ValueError:
    cred = credentials.Certificate("./ServiceAccountKey.json")
    firebase_admin.initialize_app(cred)


db = firestore.client()