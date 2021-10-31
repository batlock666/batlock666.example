#!/usr/bin/env python

import subprocess
import venv

SETUPTOOLS_VERSION = "51.3.3"
ZC_BUILDOUT_VERSION = "2.13.5"

if __name__ == "__main__":
    # Create the virtual environment
    builder = venv.EnvBuilder(with_pip=True)
    builder.create("venv")

    # Update package pip
    subprocess.check_call([
        "venv/bin/python",
        "-m", "pip",
        "install",
        "--upgrade",

        # Packages
        "pip",
    ])

    # Install packages setuptools and zc.buildout
    subprocess.check_call([
        "venv/bin/python",
        "-m", "pip",
        "install",

        # Packages
        "setuptools==%s" % SETUPTOOLS_VERSION,
        "zc.buildout==%s" % ZC_BUILDOUT_VERSION,
    ])
