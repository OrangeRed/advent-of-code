# advent-of-code

My solutions to [Advent of Code](https://adventofcode.com/).
These are not necessary the best or the fastest solution but what I wrote during the contest itself

![](https://img.shields.io/badge/Advent%20of%20Code%202023-1/25-thistle?style=for-the-badge)&nbsp;

## Guide

### Auth Cookie

Make sure to set the `AOC_COOKIE` env with your session secret.
To get your session secret press F12 while you are logged in on [adventofcode.com](https://adventofcode.com/) to open the developer tools of your browser.
Then open the `Application` Tab on Chromium Browsers or `Storage` on firefox. There you can have a look at your cookies and copy the session id.
It won't be possible to download a puzzle input without this session id.

### Get Script

This script will get the puzzle input for the specified year and day and print it to `stdout`.
Consider piping the result into a file so it can be reused.
If not specified the script will get the puzzle input for the current date.

```shell
# Download puzzle input for current date and save it to 'in.txt'
$ ./get.sh > in.txt

# Download puzzle input for 2023-01 and save it to 'in.txt'
$ ./get.sh 2023 1 > in.txt
```
