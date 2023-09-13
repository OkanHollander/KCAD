import datetime
import random
import time
import uuid

LOG_PATH = "/app/logs/mytestlog.log"
RANDOM_NUMBER = uuid.uuid4()
MIN_SLEEP = 0.3
MAX_SLEEP = 0.8

def random_sleep():
    sleep_duration = random.uniform(MIN_SLEEP, MAX_SLEEP)
    time.sleep(sleep_duration)


if __name__ == "__main__":
    for i in range(10000):
        random_sleep()
        with open(LOG_PATH, "a", encoding="utf-8") as f:
            f.write(f"{datetime.datetime.now()} New GUID: {RANDOM_NUMBER}\n")
