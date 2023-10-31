import pyotp

def generate_personal_code():
    custom_base32_code = pyotp.random_base32()
    one_time_password = pyotp.TOTP(custom_base32_code)
    otp_code = one_time_password.now()
    print(f"The generated OTP code: {otp_code}")
    return one_time_password

def verify_custom_otp(custom_otp):
    user_input = input("Enter the OTP code you received: ")
    if custom_otp.verify(user_input):
        print("Custom OTP verification successful.")
    else:
        print("Custom OTP verification failed.")

if __name__ == "__main__":
    generated_otp = generate_personal_code()
    verify_custom_otp(generated_otp)
