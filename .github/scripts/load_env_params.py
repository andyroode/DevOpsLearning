#!/usr/bin/env python3
import sys
import yaml
import json
import os

def getenv_and_log(key, default=""):
    value = os.getenv(key, default)
    print(f"{key}: {value}")
    return value

def sanitize_json(value):
    if isinstance(value, str):
        try:
            return json.dumps(json.loads(value))
        except json.JSONDecodeError:
            return json.dumps(value)
    elif isinstance(value, dict):
        return json.dumps(value)
    return str(value)

def main():
    if len(sys.argv) < 2:
        print("Usage: load_env_params.py <yaml_config_file>")
        sys.exit(1)

    config_file = sys.argv[1]

    with open(config_file, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)

    with open(os.getenv('GITHUB_ENV'), 'a', encoding='utf-8') as env_file:
        for key, value in data.items():
            if key == "ENV_SPECIFIC_PARAMETERS":
                value = sanitize_json(value)

            env_file.write(f"{key}={value}\n")

        env_generation_params = {
            "SD_SOURCE_TYPE": data.get("SD_SOURCE_TYPE", ""),
            "SD_VERSION": data.get("SD_VERSION", ""),
            "SD_DATA": data.get("SD_DATA", "{}"),
            "SD_DELTA": data.get("SD_DELTA", ""),
            "ENV_INVENTORY_INIT": data.get("ENV_INVENTORY_INIT", ""),
            "ENV_SPECIFIC_PARAMETERS": json.loads(data.get("ENV_SPECIFIC_PARAMETERS", "{}")),  # JSON
            "ENV_TEMPLATE_NAME": data.get("ENV_TEMPLATE_NAME", ""),
            "ENV_TEMPLATE_VERSION": data.get("ENV_TEMPLATE_VERSION", "")
        }

        env_file.write(f'ENV_GENERATION_PARAMS={json.dumps(env_generation_params)}\n')

if __name__ == "__main__":
    main()
