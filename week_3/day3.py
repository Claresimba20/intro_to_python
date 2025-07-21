import requests
api_key="8f07cdcfe855ebc0dfdef7fc9371c22c"

url=f"http://api.weatherstack.com/current?access_key={api_key}"

parameters={"query":"Nairobi","units":"f"}
response=requests.get(url,params=parameters)
#print(response.json())

result=response.json()
parameters=result['request']

for key,value in parameters.items():
    #print(f"{key}:{value}")

air=result["current"]["air_quality"]
print(air)