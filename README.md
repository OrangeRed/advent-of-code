<h1 align="center">🎄 Advent of Code 🎄</h1>

This is a repository of my solutions for [Advent of Code](https://adventofcode.com/).

![](https://img.shields.io/badge/2023%20Puzzles-15/25-lightpink?style=for-the-badge)
<br>
![](https://img.shields.io/badge/2022%20Puzzles-15/25-lightpink?style=for-the-badge)

## Guide

### Auth Cookie

Make sure to set the `AOC_COOKIE` env with your session secret.
To get your session secret press F12 while you are logged in on [adventofcode.com](https://adventofcode.com/) to open the developer tools of your browser.
Then open the `Application` Tab on Chromium Browsers or `Storage` on firefox. There you can have a look at your cookies and copy the session id.
It won't be possible to use the puzzle input get script without this session id.

### Get Script

This script will get the puzzle input for the specified year and day and print it to `stdout`.
Consider piping the result into a file so it can be reused.
If not specified the script will get the puzzle input for the current date.

```shell
# Download puzzle input for current date and save it to 'in.txt'
$ ./get.sh > in.txt

# Download puzzle input for 2023 day 1 and save it to 'in.txt'
$ ./get.sh 2023 1 > in.txt
```

### Running

```shell
# Run python script using stdin
$ python 2023/day01a.py < in.txt

# Run python script using the result from ./get.sh
$ ./get.sh 2023 1 > python 2023/day01a.py
```
