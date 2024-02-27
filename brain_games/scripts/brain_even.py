#!/usr/bin/env python3

from brain_games import cli
from brain_games.games import even


def main():
    cli.ask_question(cli.welcome_user(), even.TITLE, even.brain_even)


if __name__ == '__main__':
    main()
