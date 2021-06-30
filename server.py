import http.client
import urllib
import time


apikey = "S8347UB5QUFMPF9D" 

def publishdata(temp):
    while True:
        params = urllib.parse.urlencode({'field1': temp, 'key':apikey }) 
        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = http.client.HTTPConnection("api.thingspeak.com:80")
        conn.request("POST", "/update", params, headers)
        response = conn.getresponse()
        #print(temp)
        #print(response.status, response.reason)
        data = response.read()
        conn.close()

        break

