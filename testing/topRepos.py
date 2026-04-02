import requests
from pydantic import BaseModel, ValidationError
from requests.exceptions import HTTPError

url = "https://api.github.com/search/repositories"

class RepClasser(BaseModel):
    name: str
    description: str | None
    stargazers_count: int 
    visibility: str
    
try:
    response = requests.get(url, params={
        "q": "language:python", "sort": "stars", "order": "desc"
    })
except HTTPError as httper:
    print("HTTP error occured.")
except Exception:
    print("Error occured")
else:    
    jsonResponse = response.json()
    repositories = jsonResponse["items"]
    for rep in repositories:
        try:
            repObj = RepClasser.model_validate(rep)
            print("")
            print(f"Name: {repObj.name}")
            print(f"Description: {repObj.description}")
            print(f"Stargazers: {repObj.stargazers_count}")
            print(f"Visibility: {repObj.visibility}")
        except ValidationError as validError:
            print(f"Validation error occured:{validError}")
