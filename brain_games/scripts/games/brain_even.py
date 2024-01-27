#!/usr/bin/env python3

from brain_games import cli, games


def main():
    cli.ask_question(cli.welcome_user(),
                     games.brain_even(),
                     games.brain_even(),
                     games.brain_even())


if __name__ == '__main__':
    main()
