# NOQA: D100

import argparse

from ..functions import hello


def main():
    """Script ``hello``.
    """
    # Define the arguments
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "name",
        type=str,
        nargs="?",
        default=None,
    )

    # Parse the arguments
    args = parser.parse_args()

    # Calculate and print the result
    print(hello(args.name))


if __name__ == "__main__":
    main()
