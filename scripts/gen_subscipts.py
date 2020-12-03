#!/usr/bin/env python
"""
gen_subscripts.py

script for generating submission scripts for multiple fits must be ran from
root directory of the repo

"""
import argparse

from global_settings import (
    JOBSCRIPT_DIR, FIT_PREFIX, SETUP_PREFIX, POST_PREFIX, TEMPLATE_DIR
)

def copy_jobscript(fit_name, input_name):
    """Copies the script found in TEMPLATE_DIR/input_name.sh
    to JOBSCRIPT_DIR/input_name_fit_name.sh and substitutes
    fitname into the file where appropriate

    """
    file_contents = []
    with open(f"{TEMPLATE_DIR}/{input_name}.sh", "r") as f:
        for line in f:
            file_contents.append(line.replace("<FITNAME>", fit_name))
    with open(f"{JOBSCRIPT_DIR}/{input_name}_{fit_name}.sh", "w+") as f:
        f.writelines(file_contents)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("fit_name", type=str, help="name of fit")
    args = parser.parse_args()
    fit_name = args.fit_name

    copy_jobscript(fit_name, FIT_PREFIX)
    copy_jobscript(fit_name, SETUP_PREFIX)
    copy_jobscript(fit_name, POST_PREFIX)

if __name__ == "__main__":
    main()
