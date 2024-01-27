#!/usr/bin/env python3

from brain_games import cli


def main():
    cli.ask_question(cli.welcome_user(),
                     cli.brain_gcd(),
                     cli.brain_gcd(),
                     cli.brain_gcd())


if __name__ == '__main__':
    main()
