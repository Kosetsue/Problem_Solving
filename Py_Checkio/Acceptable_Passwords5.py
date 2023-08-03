def is_acceptable_password(password: str) -> bool:
    p_len = len(password)
    condition_1 = p_len > 6
    condition_2 = p_len > 9
    condition_3 = any(password.isdigit() for password in password)
    condition_4 = any(password.isalpha() for password in password)
    condition_5 = "password" not in password.lower()

    if (
        condition_2
        and condition_5
        or condition_1
        and condition_3
        and condition_4
        and condition_5
    ):
        print(True)
        return True
    else:
        print(False)
        return False


is_acceptable_password("password12345")
