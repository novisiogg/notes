import requests
import os # to read the token
url = "https://api.github.com/users/octocat"

# 1. the 'introvert' (HEAD)
res_head = requests.head(url)
print("head vs get")
print(f"HEAD Text: '{res_head.text}'") # will be empty!
print(f"HEAD Size: {res_head.headers.get('Content-Length')}")

# 2. the 'talker' (GET)
res_get = requests.get(url)
print(f"GET Text: '{res_get.text[:20]}...'") # will show the actual JSON
print(f"GET Size: {res_get.headers.get("content-length")}")

link = "https://httpbin.org/post"

response = requests.post(link, json={
    "student":"novisiogg"
})

jsonResp = response.json()

# side a: what i sent to the server (reflected back by httpbin)
print(f"")
print("what i actually sent to the server")
print(f"i sent this data: {jsonResp["data"]}")
print(f"i sent this format: {jsonResp["headers"]["Content-Type"]}")

# side b: What the server sent back to me (The real python object)
print(f"the server is running: {response.headers['Server']}")

# inspect the prepared request / you can see the request before actually sending it
print(f"")
print("inspecting the prepared request")
print(f"i'm sending this request to the server: {response.request}")
print(f"i'm sending this type of data to the server: {response.request.headers["Content-Type"]}")
print(f"i'm sending this data to the server {response.request.body}")

# authentication (api)
print(f"")
print("authentication")
anotherLink = "https://api.github.com/user"
token = os.getenv("TOKEN")

headers = {
    "Authorization": f"token {token}",
    "Accept": "application/vnd.github+json"
}

resp = requests.get(anotherLink, headers=headers)
respJson = resp.json()
if resp.ok:
    print(f"logged in as : {respJson["login"]}")
else:
    print(f"status code: {resp.status_code}")

