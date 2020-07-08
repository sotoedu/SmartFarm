import requests, time, json

temperature=0

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

for x in range(5):
    temperature = temperature+1
    print("The temperature is %s celsius" % temperature)
    time.sleep(3)

    payload = {'id': str("sensor1"), 'key1': str(temperature) }

    r = requests.post('http://localhost:3000/messages', data=json.dumps(payload), headers=headers)

    print(r.text)
