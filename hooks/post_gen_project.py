import argparse
import json


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--full-conf", type=json.loads)
    args = parser.parse_args()

    full_conf = args.full_conf

    print(full_conf)


if __name__ == "__main__":
    main()
