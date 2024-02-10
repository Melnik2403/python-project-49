#!/usr/bin/env python3

from brain_games import cli
from brain_games.games import calc


def main():
    cli.ask_question(cli.welcome_user(), calc.brain_calc)


if __name__ == '__main__':
    main()
