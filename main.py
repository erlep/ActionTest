import logging
import logging.handlers
import os

import requests
import time

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger_file_handler = logging.handlers.RotatingFileHandler(
    "status.log",
    maxBytes=1024 * 1024,
    backupCount=1,
    encoding="utf8",
)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger_file_handler.setFormatter(formatter)
logger.addHandler(logger_file_handler)

try:
  SOME_SECRET = os.environ["SOME_SECRET"]
except KeyError:
  SOME_SECRET = "Token not available!"
  #logger.info("Token not available!")
  # raise


if __name__ == "__main__":
  # import time - strftime - https://bit.ly/3Edt2np
  s1 = time.strftime("%Y/%m/%d %H:%M:%S")
  logger.info(f"Token value: {SOME_SECRET}")
  # r = requests.get('https://weather.talkpython.fm/api/weather/?city=Berlin&country=DE')
  r = requests.get('https://weather.talkpython.fm/api/weather?city=Brno&country=CZ')
  if r.status_code == 200:
    data = r.json()
    temperature = data["forecast"]["temp"]
    s2 = f'Weather in Brno: {temperature}'
    logger.info(s2)
    # pridani do README.md
    with open('README.md', "a+") as f:
      f.write(s1 + ' '+s2+'\n\n')
