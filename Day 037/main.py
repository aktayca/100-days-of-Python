import requests
from datetime import datetime as dt
import os
from dotenv import load_dotenv

load_dotenv()

USERNAME = os.getenv("USERNAME")
TOKEN = os.getenv("TOKEN")

date_to_edit_or_delete = dt(year=2025, month=10, day=29)
DATE_STRING = date_to_edit_or_delete.strftime("%Y%m%d")

pixela_endpoint = "https://pixe.la/v1/users"
pixela_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
add_pixel = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"
edit_or_delete_pixel = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{DATE_STRING}"


user_params= {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor": "yes"
}

graph_config = {
    "id":"graph1",
    "name":"Coding Graph",
    "unit":"Hours",
    "type":"float",
    "color":"momiji"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

today = dt.now()
# todays_date = today.strftime("%Y%m%d")

pixel_add_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours did you code today?")
}

pixel_edit_data = {
    "quantity": "2.5"
}

response = requests.post(add_pixel,json=pixel_add_data ,headers=headers)

