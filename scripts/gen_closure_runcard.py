#!/usr/bin/env python
"""
gen_closure_runcard.py

Script which takes a base `n3fit` runcard for closure tests and generates a
single new runcard with different filter and dataseeds for multiple closure test
studies. Similar to `vp-nextfitruncard` except that also iterates preprocessing
and t0, which we don't want.

"""
import argparse
import random

from reportengine.compat import yaml

from global_settings import BASENAME, TEMPLATE_DIR


def gen_seed():
    """Generate a random long int"""
    return random.randrange(0, 2**32)


def main():
    with open(f"{TEMPLATE_DIR}/{BASENAME}", "r") as f:
        base_config = yaml.load(f, Loader=yaml.RoundTripLoader)
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("fit_name", type=str, help="name of fit")
    parser.add_argument("fit_desc", type=str, help="fit description")
    args = parser.parse_args()

    outname = args.fit_name
    out = outname + ".yml"
    base_config["description"] = args.fit_desc
    base_config["closuretest"]["filterseed"] = gen_seed()
    base_config["fitting"]["trvlseed"] = gen_seed()
    base_config["fitting"]["nnseed"] = gen_seed()
    base_config["fitting"]["mcseed"] = gen_seed()

    with open(out, "w+") as f:
        yaml.dump(base_config, f, Dumper=yaml.RoundTripDumper)
    
if __name__ == "__main__":
    main()
