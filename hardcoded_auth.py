import requests
from requests.auth import HTTPBasicAuth

# the following line should be flagged for passing a plaintext password
auth = HTTPBasicAuth("user", "pass")

