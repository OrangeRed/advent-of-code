#!/bin/bash

AOC="$HOME/Personal/advent-of-code"
AOC_COOKIE=$(cat $AOC/.env | grep -e AOC_COOKIE | cut -d = -f2)

if [ ! $AOC_COOKIE ]; then
    echo "Error: Advent of Code Auth Cookie is missing."
    exit 1
fi

# $1 is puzzle year, $2 is puzzle day
if [ $1 ] && [ $2 ]; then
    curl --cookie "session=$AOC_COOKIE" https://adventofcode.com/$1/day/$2/input
else
    curl --cookie "session=$AOC_COOKIE" "$(echo `date +https://adventofcode.com/%Y/day/%d/input` | sed 's/\/0/\//g')"
fi