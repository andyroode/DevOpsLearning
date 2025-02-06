#!/usr/bin/env python3
import sys
import yaml
import json

def main():
    if len(sys.argv) < 2:
        print("Usage: load_env_params.py <yaml_config_file>")
        sys.exit(1)

    config_file = sys.argv[1]

    with open(config_file, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)

    for key, value in data.items():
        if isinstance(value, dict):
            json_file = f"/tmp/{key}.json"
            with open(json_file, 'w', encoding='utf-8') as f:
                json.dump(value, f, indent=2)
            print(f"{key}_FILE={json_file}")  # Записываем путь в ENV
        else:
            print(f"{key}={value}")

if __name__ == "__main__":
    main()
