import time

print("time()         ", time.time())
print("monotonic()    ", time.monotonic())
print("process_time() ", time.process_time())
print("perf_counter() ", time.perf_counter())

print()

print("time()         ", time.get_clock_info('time'))
print("monotonic()    ", time.get_clock_info('monotonic'))
print("process_time() ", time.get_clock_info('process_time'))
print("perf_counter() ", time.get_clock_info('perf_counter'))

print()

import datetime

print(datetime.datetime.today())
print(datetime.datetime.now())
print(datetime.datetime.utcnow())
