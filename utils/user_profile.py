from auth.firebase_auth import db
from models.user_profile import UserProfile


class UserProfileCRUD:
    @staticmethod
    def create_user_profile(data: dict):
        # Validate data using the Pydantic model
        user_profile = UserProfile(**data)
        user_profiles_ref = db.collection("user-profile")
        new_doc_ref = user_profiles_ref.add(user_profile.dict())
        print(f"User profile created with ID: {new_doc_ref[1].id}")
        return new_doc_ref[1].id

    @staticmethod
    def get_all_user_profiles():
        user_profiles_ref = db.collection("user-profile")
        docs = user_profiles_ref.stream()
        profiles = [{doc.id: doc.to_dict()} for doc in docs]
        return profiles

    @staticmethod
    def get_user_profile(doc_id: str):
        user_profiles_ref = db.collection("user-profile")
        doc_ref = user_profiles_ref.document(doc_id)
        doc = doc_ref.get()
        if doc.exists:
            return doc.to_dict()
        else:
            print("No such document!")
            return None

    @staticmethod
    def update_user_profile(doc_id: str, data: dict):
        # Validate data with Pydantic model before updating
        user_profile = UserProfile(**data)
        user_profiles_ref = db.collection("user-profile")
        doc_ref = user_profiles_ref.document(doc_id)
        doc_ref.update(user_profile.dict())
        print(f"User profile with ID: {doc_id} updated.")

    @staticmethod
    def delete_user_profile(doc_id: str):
        user_profiles_ref = db.collection("user-profile")
        doc_ref = user_profiles_ref.document(doc_id)
        doc_ref.delete()
        print(f"User profile with ID: {doc_id} deleted.")