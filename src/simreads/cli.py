import argparse
import logging
import yaml

def main(argv=None):
    p = argparse.ArgumentParser()
    p.add_argument("config", type=argparse.FileType('r'), help="the config file")
    p.add_argument("--log-level", default="INFO", help="the logging level")

    p.add_argument("")

    args = p.parse_args(argv)
    logging.basicConfig()
    logging.getLogger().setLevel(args.log_level)

    config = yaml.safe_load(args.config)
