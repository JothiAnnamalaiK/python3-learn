import requests
import json
import os

# Path to save file inside project folder
working_folder = os.path.dirname(__file__)  # current folder of the script

response = requests.get("https://api.github.com/events")
# print(r.text)
if response.status_code == 200:
    data = response.json()  # Parse the JSON response
    # print(data)  # Access data from the JSON

    # Pretty-print JSON to terminal
    # print(json.dumps(data, indent=4))

    file_path = os.path.join(working_folder, "get_request_data.txt")

    # Write JSON to file
    with open(file_path, "a") as f:
        f.write(json.dumps(data, indent=4))
        f.write("\n\n")  # Optional: separate each request
else:
    print(f"Error: {response.status_code}")


"""
Other Examples:

r = requests.post('https://httpbin.org/post', data={'key': 'value'})
r = requests.put('https://httpbin.org/put', data={'key': 'value'})
r = requests.delete('https://httpbin.org/delete')
r = requests.head('https://httpbin.org/get')
r = requests.options('https://httpbin.org/get')


Passing Parameters In URLs:

payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('https://httpbin.org/get', params=payload)

You can see that the URL has been correctly encoded by printing the URL:

print(r.url)  #output: https://httpbin.org/get?key2=value2&key1=value1



Custom Headers:
url = 'https://api.github.com/some/endpoint'
headers = {'user-agent': 'my-app/0.0.1'}
r = requests.get(url, headers=headers)
"""
