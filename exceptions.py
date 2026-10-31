from fastapi.responses import JSONResponse
from fastapi import Request

class PinCodeNotFoundException(Exception):  #exception class for handling cases where the pincode is not found in the database
    def __init__(self, pincode: str):
        self.pincode = pincode  # feeding the pincode that caused the exception

class InvalidPinCodeException(Exception):   #exception class for handling cases where the pincode provided is invalid
    def __init__(self, pincode: str, reason: str): 
        self.pincode = pincode  # feeding the pincode that caused the exception
        self.reason = reason    # feeding the reason for the exception

#custom exception handler for PinCodeNotFoundException\
async def pin_code_not_found_exception_handler(request: Request, exc: PinCodeNotFoundException):
    return JSONResponse(
        status_code=404,
        content={
            "error": "Pincode Not Found",
            "message": f"Pincode {exc.pincode} not found."
            }
    )

#custom exception handler for InvalidPinCodeException
async def invalid_pin_code_exception_handler(request: Request, exc: InvalidPinCodeException):
    return JSONResponse(
        status_code=400,
        content={
            "error": "Invalid Pincode",
            "message": f"Invalid pincode {exc.pincode}: {exc.reason}"
        }
    )