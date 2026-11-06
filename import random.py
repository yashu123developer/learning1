import random
import time


while True:
    value=random.randint(200,400)/1023
    moisture=round((1-value)*100,0)
    print("moisturevalue:",moisture,"%")
    print("digital value read from sensor:",int(value*1023))


    time.sleep(5)  