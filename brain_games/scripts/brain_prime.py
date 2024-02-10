#!/usr/bin/env python3

from brain_games import cli
from brain_games.games import prime


def main():
    cli.ask_question(cli.welcome_user(), prime.brain_prime)


if __name__ == '__main__':
    main()
