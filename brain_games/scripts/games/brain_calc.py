#!/usr/bin/env python3

from brain_games import cli, games


def main():
    cli.ask_question(cli.welcome_user(),
                     games.brain_calc(),
                     games.brain_calc(),
                     games.brain_calc())


if __name__ == '__main__':
    main()
