# Sms16Client

Sms16Client is a module that provides an interface for sms16.ru API.

## Usage

```python
from sms16client import Sms16Client

sms16 = Sms16Client()
sms16.api_key = 'your_api_key'
sms16.login = 'your_sms16_login'

sms16.balance()
sms16.send("author", ["12345678900"], "hello world")
sms16.status(["111"])
```

## Changelog

0.1.0 - Release module
