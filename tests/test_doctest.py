# NOQA: D100

import doctest

OPTIONFLAGS = (
    doctest.REPORT_ONLY_FIRST_FAILURE |  # NOQA: W504
    doctest.NORMALIZE_WHITESPACE |  # NOQA: W504
    doctest.ELLIPSIS
)


def load_tests(loader, tests, ignore):  # NOQA: D103
    """Load the tests.
    """
    tests.addTests(doctest.DocFileSuite(
        "../README.rst",
        optionflags=OPTIONFLAGS,
    ))
    return tests


if __name__ == "__main__":
    doctest.testfile("../README.rst", optionflags=OPTIONFLAGS)
