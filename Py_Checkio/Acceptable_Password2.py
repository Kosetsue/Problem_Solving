def is_acceptable_password(password: str) -> bool:
    condition_1 = len(password) > 6
    condition_2 = any(password.isdigit() for password in password)

    if condition_1 and condition_2:
        print(True)
        return True
    else:
        print(False)
        return False


is_acceptable_password("short")
is_acceptable_password("muchlonger")
is_acceptable_password("ashort")
is_acceptable_password("muchlonger5")
is_acceptable_password("sh5")
