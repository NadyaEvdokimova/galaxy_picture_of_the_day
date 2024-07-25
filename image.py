import requests


def get_image(url):
    response = requests.get(url=url)
    image_info = response.json()
    image_name = image_info['title']
    image_description = image_info['explanation']
    image_sum = {"Title": image_name, "Description": image_description}
    image_url = image_info['url']
    image_response = requests.get(image_url)
    with open("image.jpg", 'wb') as file:
        file.write(image_response.content)
    return image_sum

