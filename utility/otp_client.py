import pyotp
class OTPGenerator:

    def ganerate(self):
        # Generate OTP
        totp = pyotp.TOTP('base32secret3232', interval=300)
        return totp.now()
    def verify(self,otp : str):
        try :
            # Get Otp from Redis based on user id
            
            # Verify the otp
            totp = pyotp.TOTP('base32secret3232', interval=300)
            return totp.verify(otp=otp)
            # Delete Otp From redis
        except Exception as e:
            return e.args[0]

        
