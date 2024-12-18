import json
import requests

def collect_data(sensor_url):
    response = requests.get(sensor_url)
    data = response.json()
    return data

def save_data_to_db(data, db_session):
    # Process and save to database
    pass
