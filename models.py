from pydantic import BaseModel, field_validator

class PincodeRequest(BaseModel):
    pincode: str

    #pincode must be exactly 6 digits
    @field_validator("pincode")
    @classmethod                 #Used to define a class method that can be called on the class itself, rather than on an instance of the class. This is useful for validation methods that need to access class-level data or perform operations that are not specific to a single instance.
    def validate_pincode(cls, value):  #validate_pincode is a class method that validates the pincode field of the PincodeRequest model. It checks if the provided pincode is exactly 6 digits long and consists only of digits. If the validation fails, it raises a ValueError with an appropriate message. If the validation passes, it returns the validated value.
        if len(value) != 6 or not value.isdigit():
            raise ValueError("Pincode must be exactly 6 digit")
        return value
    
class LocationResponse(BaseModel):
    pincode: str
    city: str
    state: str
    district: str


class BulkRequest(BaseModel):
    pincodes: list[str]

    @field_validator("pincodes")
    @classmethod
    def validate_pincodes(cls, values):
        if len(values) == 0:
            raise ValueError("At least one pincode is required")
        if len(values) > 20:
            raise ValueError("Maximum 20 pincodes allowed per request")
        
        for code in values:
            if len(code) != 6 or not code.isdigit():
                raise ValueError("Each Pincode must be exactly 6 digit")
        return values


class BulkResponse(BaseModel):
    status: str = "success"
    found: int
    not_found: int
    results: list[LocationResponse]
    missing: list[str]