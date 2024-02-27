#!/usr/bin/env python3

from brain_games import cli
from brain_games.games import progression


def main():
    cli.ask_question(cli.welcome_user(), progression.TITLE,
                     progression.brain_progression)


if __name__ == '__main__':
    main()
