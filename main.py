# Sample data based on the document schema
from utils.user_profile import UserProfileCRUD

new_user_data = {
    "name": "Alice",
    "phone_number": "7890123456",
    "disability": None,
    "emergency_contact_number": "2314845334",
    "marital_status": "Married",
    "emergency_contact_name": "",
    "current_city": "Vancouver",
    "health_issues": None,
    "email": "alice@gmail.com",
    "gender": "Female",
    "dob": "06/10/2005"
}

# Create a new user profile
new_user_id = UserProfileCRUD.create_user_profile(new_user_data)

# Get all user profiles
print("All User Profiles:")
all_profiles = UserProfileCRUD.get_all_user_profiles()
for profile in all_profiles:
    print(profile)

# Get a specific user profile by ID
print("User Profile by ID:")
user_profile = UserProfileCRUD.get_user_profile(new_user_id)
print(user_profile)

# Update the user profile
updated_data = {
    "name": "Tanishka Gupta",
    "phone_number": "0987654321",
    "disability": None,
    "emergency_contact_number": "1234567890",
    "marital_status": "Single",
    "emergency_contact_name": "John Doe",
    "current_city": "Toronto",
    "health_issues": "None",
    "email": "tanishka6920@gmail.com",
    "gender": "Female",
    "dob": "06/09/2000"
}
UserProfileCRUD.update_user_profile(new_user_id, updated_data)
print("User Profile by ID Updated:")
user_profile = UserProfileCRUD.get_user_profile(new_user_id)
print(user_profile)

# Delete the user profile
UserProfileCRUD.delete_user_profile(new_user_id)