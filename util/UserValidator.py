MSG_USERNAME_INVALID = ("Username must start with lower or upper english alphabet " +
                        "and should contain only alphabets or digits or underscore")
MSG_PASSWORD_INVALID = ("Password should be at least 8 characters and contains any of "
                        "the following characters : upper or lower case alphabet or "
                        "digits or @#$%^&+=")
MSG_PASSWORD_NO_MATCH = "Password and Confirm password must be same"
MSG_EMAIL_INVALID = ("Email should contain '@' symbol, and should have group of " +
                     "characters on either side of the symbol")
MSG_USERDATA_VALID = "VALID"

RE_USERNAME = r"^[A-Za-z][A-Za-z0-9_]+$"
RE_PASSWORD = r"[A-Za-z0-9@#$%^&+=.]{8,}"
