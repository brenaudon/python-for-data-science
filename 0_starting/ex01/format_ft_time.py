import time
import datetime


now_seconds = time.time()
now_date = datetime.datetime.now()

print(f"Seconds since January 1, 1970: {now_seconds:,.4f} or {now_seconds:.2e} in scientific notation")
print(now_date.strftime("%b %d %Y"))