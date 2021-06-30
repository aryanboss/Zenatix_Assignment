# Temprature Sensor Data Logger
**IoT based temperature data logger on cloud over MQTT protocol**

**Steps:**<br />
1)Creat a Channel on Thingspeak.<br />
2)Enter the name of Channel name and Filed 1 as "Temperature".<br />
3)Keep the Writing API key safe.<br />
4)We are using MQTT Protocol to publish data to cloud, via MQTT API Key.<br />
5)sever.py script is used for connection.<br />
6)edge.py scipt contains program that reads each points every-60 sec delay and publish to the cloud.<br />
7)for random Connection Success/failure, a simple program is used. A random int is generated between 0 to 5, if the int is less than 3, the data will be published to cloud otherwise it will be stored in  local text file.<br />
8)A threaded program bufferdata() that runs every 5 seconds to check if there is any data stored in buffer.txt file,if so it will publish that data and cleans the buffer.<br />

**==> A Sample Video of project is Uploaded that reads data every 5 seconds (for realization)**<br />

**Flowchart of Program**![Blank diagram](https://user-images.githubusercontent.com/58064647/123987080-84e05f80-d9e4-11eb-9f79-b0115b0c8481.jpeg)
