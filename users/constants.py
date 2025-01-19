class REGEX:
    IBAN_RULE = r'^[A-Za-z0-9]+$'
    PHONE_NUMBER_RULE = r'^\+?\d+$'
    NAME_RULE = r'^[a-zA-ZČŠĆŽĐčćšđž\s]+$'


def min_birth_age():
    return 567648000  # 18 years in seconds
