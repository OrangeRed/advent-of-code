import os
from datetime import date

import regex
import requests
from requests.exceptions import JSONDecodeError

# environment variables
userid = os.getenv("AOC_USER_ID")
session = os.getenv("AOC_COOKIE")
year = os.getenv("YEAR")


if not userid:
    print("::error::Leaderboard AOC_USER_ID was not provided")
    exit(1)

if not session:
    print("::error title=NO::AOC_COOKIE was not provided")
    exit(1)

first_aoc = date(2015, 12, 1)
target = today = date.today()
try:
    if year:
        target = date(int(year), 12, 1)
    else:
        print(f"::notice title=NO_DATE::year input not provided, using {today.year}")
except ValueError:
    print("::error::year input is not an integer")
    exit(1)

if not first_aoc <= target <= today:
    print(f"::error::year input must be between {first_aoc.year} and {today.year}")
    exit(1)


# fetch data
res = requests.get(
    f"https://adventofcode.com/{target.year}/leaderboard/private/view/{userid}.json",
    cookies={"session": session},
)

if res.status_code != 200:
    print(
        f"::error title=Not_OK::Leaderboard API returned status code {res.status_code}: {res.text}"
    )
    exit(1)

try:
    data = res.json()
except JSONDecodeError as json_err:
    print(f"::error title=JSON_ERROR::Could not parse leaderboard json: {json_err}")
    exit(1)

# stars
# stars = data["members"][userid]["stars"]

# completed days
days_completed = 0
for day in data["members"][userid]["completion_day_level"].values():
    days_completed += 1 if "2" in day else 0


# read file
f = open("README.md", mode="r", encoding="utf-8")
txt = f.read()
f.close()

# look for "https://img.shields.io/badge/2022*[num]/25*"
badge = "https:\/\/img\.shields\.io\/badge\/"
# txt = regex.sub(f"(?<={badge}{target.year}.*)\d+(?=\/50*)", str(stars), txt)
txt = regex.sub(f"(?<={badge}{target.year}.*)\d+(?=\/25*)", str(days_completed), txt)

# write back file
f = open("README.md", mode="w", encoding="utf-8")
f.write(txt)
f.close()
