# Traccar Data Populator
Generating real data for development is troublesome, thats why better to create data populator for that purpose, this library. This library help us to populate data for device trip.

## How to Use

### Installation
Installation
```sh
pip install TraccarDataPopulator
```
### Usage
To use this library you just need to provide traccar url for osmand and device_id
```Python
from TraccarDataPopulator.Populator import Populator
populator = Populator('http://demo.traccar.org:5055','testid2',5)
populator.populateData([[-8.2257,113.2190],[-8.2258,113.2190],[-8.1260,113.2190,10]])
populator.populateDataBetweenTwoLocationFollowingRoad(112.78532737805308,-7.38007105,105.4596077,-7.0249592)

```

### Available Function
#### Populator(traccar_url,device_id,speed)
This function instantiate populator for specific traccar url, device id, and speed    
#### setSpeed(speed)    
This function set speed that sent to traccar server    
#### setDeviceId(device_id)    
This function set device_id that sent to traccar server    
#### populateData([[lat,lon],[lat,lon,speed]])    
This function send data to traccar by given input format lat,lon with speed as mentioned in setSpeed. Other format is lat,lon,speed which send data with custom speed    
#### populateDataBetweenTwoLocationFollowingRoad(origin_lon,origin_lat,destination_lon,destination_lat)
This function send data to traccar by following routes    
#### populateDataFromFile(filepath)    
This function send data to traccar by given flat file with each input perline.    
```text
-8.1257,113.2190
-8.1260,113.2190,10
```

### Contact:
mail: aryya.widigdha@yahoo.com    
YT Traccar Tutorial: https://www.youtube.com/playlist?list=PLAog7t_ArobujtC6UMWjUiOWwsSrUKpi-       


### Stats
[![Downloads](https://static.pepy.tech/personalized-badge/traccardatapopulator?period=total&units=international_system&left_color=black&right_color=orange&left_text=Downloads)](https://pepy.tech/project/traccardatapopulator)


License    
----     

MIT License
