import requests
import random
import time

url = 'http://34.74.158.214:9091/metrics/job/sensor-data'

while True:
    temperature = random.randint(10, 30)
    humidity = random.randint(4, 100)
    data = f"""
    # TYPE temperature gauge
    temperature{{sensor_id="12345"}} {temperature}
    # TYPE humidity gauge
    humidity{{sensor_id="12345"}} {humidity}
    """
    response = requests.post(url, data=data)

    if response.status_code == 200:
        print('Data posted successfully')
    else:
        print(f'Failed to post data. Status code: {response.status_code}')
    
    time.sleep(10)