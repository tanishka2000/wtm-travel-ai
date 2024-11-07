from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import date

class UserProfile(BaseModel):
    name: str
    dob: str
    email: EmailStr
    phone_number: str
    current_city: str
    gender: str
    disability: Optional[str] = None
    health_issues: Optional[str] = None
    marital_status: str
    emergency_contact_name: str
    emergency_contact_number: str
