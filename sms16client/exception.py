# coding: utf-8

ERRORS = {
        "000": u"Service is unavailable",
        "1": u"Signature is missing",
        "2": u"Login is missing",
        "3": u"Text is missing",
        "4": u"Unknown phone number",
        "5": u"Unknown sender",
        "6": u"Invalid signature",
        "7": u"Invalid login",
        "8": u"Invalid sender's name",
        "9": u"Unknown name of the sender",
        "10": u"Sender's name is not approved",
        "11": u"The text contains forbidden words",
        "12": u"Error sending sms",
        "13": u"Phone number located in the stop list. Sending to this number \
                is blocked",
        "14": u"There are of more than 50 phone numbers in the request",
        "15": u"Database is not specified",
        "16": u"Invalid phone number",
        "17": u"SMS ID are not specified",
        "18": u"Status is not received",
        "19": u"Empty response",
        "20": u"Phone number already exists",
        "21": u"No name",
        "22": u"Template already exists",
        "23": u"Unknown month (format: YYYY-MM)",
        "24": u"Timestamp is not specified",
        "25": u"Error accessing database",
        "26": u"Database is empty",
        "27": u"There are no valid phone numbers",
        "28": u"Initial date is not specified",
        "29": u"Final date is not specified",
        "30": u"Date not specified (format: YYYY-MM-DD)",
}


class SMS16Exception(Exception):
    pass

class ApiException(SMS16Exception):
    """
    An exception is thrown if an error occurs in the work with api.
    """

    def __init__(self, code):
        default_message = u"Error code `{}` is not found"
        if code.isdigit():
            message = ERRORS.get(str(code), default_message.format(code))
        else:
            message = default_message.format(code)
        self.code = code
        self.json = {"code": code, "message": message}

        super(ApiException, self).__init__(message)
