import requests, time

temperature=0

for x in range(5):
    temperature = temperature+1
    print("The temperature is %s celsius" % temperature)
    time.sleep(3)

    payload = {'key1': temperature}
    r = requests.get('http://localhost:3000/hello',params=payload)
    print(r.text)

