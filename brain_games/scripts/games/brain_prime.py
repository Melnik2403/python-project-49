#!/usr/bin/env python3

from brain_games import cli


def main():
    cli.ask_question(cli.welcome_user(),
                     cli.brain_prime(),
                     cli.brain_prime(),
                     cli.brain_prime())


if __name__ == '__main__':
    main()
