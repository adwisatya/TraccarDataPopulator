import requests
import json
import time

class Populator:
    def __init__(self, url,device_id,speed):
        self.url = url
        self.device_id = device_id
        self.speed = speed
    def sendData(self,url,post_data):
        print(post_data)
        content = requests.post(url,data=post_data)
        return content.status_code
    def setSpeed(self,speed):
        self.speed = speed
    def setDeviceId(self,device_id):
        self.device_id = device_id
    def populateData(self,data):
        print('Send data to:'+self.url)
        for data_to_process in data:
            current_time = time.time()
            print(current_time)
            try:
                payload = {}
                payload['id'] = self.device_id
                payload['lat'] = data_to_process[0]
                payload['lon'] = data_to_process[1]
                payload['timestamp'] = int(str(current_time).split(".")[0])
                if len(data_to_process) == 2:
                    payload['speed'] = self.speed
                if len(data_to_process) == 3:
                    payload['speed'] = data_to_process[2]
                self.sendData(self.url,payload)
            except Exception as e:
                print(e)
                pass
            time.sleep(5)
    def populateDataFromFile(self,filepath):
        data = []
        with open(filepath) as datafile:
            lines = datafile.read().split("\n")
            for line in lines:
                data.append(line.strip().split(","))
        self.populateData(data)
    def populateStraightDataBetweenTwoLocation(self,first_location,second_location):
        return True
    def populateDataBetweenTwoLocationFollowingRoad(self,first_location,second_location):
        return True