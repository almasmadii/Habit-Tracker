import requests
from datetime import datetime
pythonfrom dotenv import load_dotenv
import os

load_dotenv()

GRAPH_ID=os.getenv("GRAPH_ID")
USERNAME=os.getenv("USERNAME")
TOKEN=os.getenv("TOKEN")
pixela_endpoint=os.getenv("pixela_endpoint")

user_params={
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}

# response=requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)

graph_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config={
    "id":GRAPH_ID,
    "name":"Coding Graph",
    "unit":"hours",
    "type":"float",
    "color":"ajisai"
}

headers={
    "X-USER-TOKEN":TOKEN
}

# response=requests.post(url=graph_endpoint,json=graph_config,headers=headers)
# print(response.text)
pixel_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today=datetime(year=2025,month=11,day=14)



add_pixel={
    "date":today.strftime("%Y%m%d"),
    "quantity":input("How many hours did you code today?")
}

pixel_header={
    "X-USER-TOKEN":TOKEN
}

# response=requests.post(url=pixel_endpoint,json=add_pixel,headers=pixel_header)
# print(response.text)
update_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{'20251115'}"

update_header={"X-USER-TOKEN":TOKEN}

update_body={
    "quantity":"8"
}

# response=requests.put(url=update_endpoint,json=update_body,headers=update_header)
# print(response.text)

delete_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{'20251116'}"
delete_header={
    "X-USER-TOKEN":TOKEN
}
response=requests.delete(url=delete_endpoint,headers=delete_header)
print(response.text)
