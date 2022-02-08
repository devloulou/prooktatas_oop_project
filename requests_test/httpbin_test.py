import requests


payload = {"username": "Ricsi", "password": "test_pass"}

post_end_point = "https://httpbin.org/post"
r = requests.put(post_end_point, data=payload)

print(r)

# my_image = "https://img-9gag-fun.9cache.com/photo/aNPp4WG_700b.jpg"

# r = requests.get(my_image)

# with open("test_image.jpg", "wb") as data:
#     data.write(r.content)
