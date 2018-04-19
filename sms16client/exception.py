ERRORS = {
        0: "Service is unavailable",
        1: "Signature is missing",
        2: "Login is missing",
        3: "Text is missing",
        4: "Unknown phone number",
        5: "Unknown sender",
        6: "Invalid signature",
        7: "Invalid login",
        8: "Invalid sender's name",
        9: "Unknown name of the sender",
        10: "Sender's name is not approved",
        11: "The text contains forbidden words",
        12: "Error sending sms",
        13: "Phone number located in the stop list. Sending to this number \
                is blocked",
        14: "There are of more than 50 phone numbers in the request",
        15: "Database is not specified",
        16: "Invalid phone number",
        17: "SMS ID are not specified",
        18: "Status is not received",
        19: "Empty response",
        20: "Phone number already exists",
        21: "No name",
        22: "Template already exists",
        23: "Unknown month (format: YYYY-MM)",
        24: "Timestamp is not specified",
        25: "Error accessing database",
        26: "Database is empty",
        27: "There are no valid phone numbers",
        28: "Initial date is not specified",
        29: "Final date is not specified",
        30: "Date not specified (format: YYYY-MM-DD)",
}


class SMS16Exception(Exception):
    pass

class ApiException(SMS16Exception):
    """
    An exception is thrown if an error occurs in the work with api.
    """

    def __init__(self, code):
        default_message = "Error code `{}` is not found"
        if isinstance(code, int):
            message = ERRORS.get(code, default_message.format(code))
        else:
            message = default_message.format(code)
        self.code = code
        self.json = {"code": code, "message": message}

        super(ApiException, self).__init__(message)
