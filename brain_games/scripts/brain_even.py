#!/usr/bin/env python
from brain_games.games.even import even
from brain_games.scripts.brain_engine import brain_play
from brain_games.games.even import TEXT_TASK

def main():
    brain_play(even())

if __name__ == '__main__':
    main()