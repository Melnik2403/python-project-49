#!/usr/bin/env python3

from brain_games import cli
from brain_games.games import gcd


def main():
    cli.ask_question(cli.welcome_user(), gcd.TITLE, gcd.brain_gcd)


if __name__ == '__main__':
    main()
