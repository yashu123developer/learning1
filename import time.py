import random
import time


while True:
    distance= round(random.uniform(5,60),2)

    if distance<80:
        print("buzzer on -object detected")
    else:
        print("buzzer off -object for away")

        time.sleep(4)