# Traffic Light Simulator System
import time

def traffic_light_simulator():
    while True:
        print("Traffic Light: RED")
        time.sleep(5)  # Red light for 5 seconds
        
        print("Traffic Light: GREEN")
        time.sleep(5)  # Green light for 5 seconds
        
        print("Traffic Light: YELLOW")
        time.sleep(2)  # Yellow light for 2 seconds
if __name__ == "__main__":
    traffic_light_simulator()