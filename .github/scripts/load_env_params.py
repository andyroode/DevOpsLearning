#!/usr/bin/env python3
import sys
import yaml

def main():
    if len(sys.argv) < 2:
        print("Usage: load_env_params.py <yaml_config_file>")
        sys.exit(1)

    config_file = sys.argv[1]

    with open(config_file, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)

    for key, value in data.items():
        print(f'{key}={value} >> $GITHUB_ENV')

if __name__ == "__main__":
    main()