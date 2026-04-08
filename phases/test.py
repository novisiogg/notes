import requests
from requests.exceptions import RequestException

url = "http://localhost:8000/"

payload = {
    "role": "user",
    "content": "hey there"
}
try:
    response = requests.post(
        url,
        json=payload,
        timeout=2
    )
except RequestException:
    print("There was an error posting to " + url)