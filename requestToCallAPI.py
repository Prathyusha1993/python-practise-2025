import requests

# get request
response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
data = response.json()
print(data)

# post reequest
url = "https://jsonplaceholder.typicode.com/posts"
payload = {"title":"foo", "body":"bar", "userId":1}
response = requests.post(url, json=payload)

print(response.status_code)
print(response.json())

# handling api repsonse and exceptions
# api can fail die to bad internet, invalid url, server error, etc.
# to catch them use try/ except to handle exceptions

url = 'https://jsonplaceholder.typicode.com/posts/1'
try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()

    data = response.json()
    print('title:', data['title'])

except requests.exceptions.Timeout:
    print('Request timed out')
except requests.exceptions.HTTPError as err:
    print('HTTP error occurred:', err)
except requests.exceptions.RequestException as err:
    print('Other error occurred:', err)
