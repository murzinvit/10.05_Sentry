#!/usr/bin/env python3
import logging
import random
import time
import sentry_sdk

sentry_sdk.init(
    "https://e12b4c87e70a4997bf5594e72869789d@o1019220.ingest.sentry.io/5986871",
    traces_sample_rate=1.0
)

count = 0
while True:
  number = random.randrange(0, 10)
  print(number)
  if count == 5:
        number/0
  count += 1
  time.sleep(1)