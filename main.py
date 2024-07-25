import requests
import os

API_KEY = os.environ.get("API_KEY")
URL = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}"

response = requests.get(url=URL)
image_info = response.json()
image_name = image_info['title']
image_description = image_info['explanation']
image_url = image_info['url']

image_response = requests.get(image_url)
with open("image.jpg", 'wb') as file:
    file.write(image_response.content)
