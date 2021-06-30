import sys
import os
import csv
import random
from time import sleep
import threading
import server

#Program to send buffered data every 5 seconds

def bufferdata():
    threading.Timer(5.0,bufferdata).start()
    file_path = 'buffer.txt'
    # check if file is empty
    if os.stat(file_path).st_size == 0:
        return None
    else:
        with open('buffer.txt') as f:
            value = f.readline()
            while value:
                value = f.readline()
                print("Publising Buffered data on server...",end=" ")
                print(value)
                server.publishdata(value)
        f.close()
        file = open("buffer.txt","r+")
        file.truncate(0)
        file.close()

class sensordata(threading.Thread):
    def run(self):
        pcount = 0
        bcount = 0
        with open('dataset.csv','r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                sleep(5) #delay for reading sensor data
                x = random.randint(0,5)  #simple program to give random success or failure 
                if(x<3):    
                    print("\nPublishing data on server...",end=" ")
                    print(line[1])
                    print(line[0])
                    server.publishdata(line[1])
                    pcount = pcount + 1
                    print("Succesfully published",pcount,"new temperature readings")
                else:
                    print("\nConnection Error! Data Stored locally")
                    bcount = bcount + 1
                    print("Data Buffered for",bcount,"time/s")
                    fhand = open('buffer.txt','a')
                    fhand.write(line[1])
                    fhand.write("\n")
                    fhand.close()
                        


if __name__ == '__main__':
    print("\n==========Temperature Sensor Data Logging=========\n")
    while(True):
        publishsensor = sensordata()
        bufferdata()
        publishsensor.run()