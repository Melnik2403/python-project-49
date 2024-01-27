#!/usr/bin/env python3

from brain_games import cli, games


def main():
    cli.ask_question(cli.welcome_user(),
                     games.brain_gcd(),
                     games.brain_gcd(),
                     games.brain_gcd())


if __name__ == '__main__':
    main()
