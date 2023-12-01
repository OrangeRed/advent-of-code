# advent-of-code

My solutions to [Advent of Code](https://adventofcode.com/).
These are not necessary the best or the fastest solution but what I wrote during the contest itself

# Guide

### Auth Cookie

Make sure to set the `AOC_COOKIE` env with your specific auth cookie.
This cookie is placed inside your browser after logging into the advent of code website.
It won't be possible to download a puzzle input without this cookie.

### Get Script

This script will get the puzzle input for the specified year and day and print it to `stdout`.
Consider piping the result into a file so it can be reused.
If not specified the script will get the puzzle input for the current date.

```sh
# Download puzzle input for current date and save it to 'in.txt'
./get.sh > in.txt

# Download puzzle input for 2023-01 and save it to 'in.txt'
./get.sh 2023 1 > in.txt
```
