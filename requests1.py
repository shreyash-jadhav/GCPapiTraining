import requests

response = requests.post(url='http://127.0.0.1:5001/addage', json={"age":50,"randomno":30})


print("Sum of ages: ",response.json())

response1 = requests.post(url='http://127.0.0.1:5002/sumby2', json={"sum":response.json()})

print("Divided by 2 ",response1.json())