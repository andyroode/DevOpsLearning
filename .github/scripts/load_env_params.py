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
    """ Преобразует строку JSON в корректный JSON-объект """
    if isinstance(value, str):
        try:
            return json.dumps(json.loads(value))
        except json.JSONDecodeError:
            return json.dumps(value)
    elif isinstance(value, dict):
        return json.dumps(value)
    return str(value)

def convert_to_github_env(value):
    """ Преобразует значения в строковый формат для GitHub Actions """
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, str) and value.lower() in ["true", "false"]:
        return value.lower()
    return value

def main():
    if len(sys.argv) < 2:
        print("Usage: load_env_params.py <yaml_config_file>")
        sys.exit(1)

    config_file = sys.argv[1]

    with open(config_file, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)

    github_env_file = os.getenv('GITHUB_ENV')
    github_output_file = os.getenv('GITHUB_OUTPUT')

    if not github_env_file or not github_output_file:
        print("Error: GITHUB_ENV or GITHUB_OUTPUT variable is not set!")
        sys.exit(1)

    with open(github_env_file, 'a', encoding='utf-8') as env_file, \
         open(github_output_file, 'a', encoding='utf-8') as output_file:

        for key, value in data.items():
            if key == "ENV_SPECIFIC_PARAMETERS":
                if not value:  # Проверяем на пустоту или None
                    sanitized_value = "{}"
                else:
                    sanitized_value = sanitize_json(value)
                env_file.write(f"{key}={sanitized_value}\n")
                output_file.write(f"{key}={sanitized_value}\n")
            else:
                converted_value = convert_to_github_env(value)
                env_file.write(f"{key}={converted_value}\n")
                output_file.write(f"{key}={converted_value}\n")

        # Обработка ENV_SPECIFIC_PARAMETERS для ENV_GENERATION_PARAMS
        try:
            env_specific_params = json.loads(data.get("ENV_SPECIFIC_PARAMETERS", "{}") or "{}")
        except json.JSONDecodeError:
            env_specific_params = {}

        env_generation_params = {
            "SD_SOURCE_TYPE": data.get("SD_SOURCE_TYPE", ""),
            "SD_VERSION": data.get("SD_VERSION", ""),
            "SD_DATA": data.get("SD_DATA", "{}"),
            "SD_DELTA": data.get("SD_DELTA", ""),
            "ENV_INVENTORY_INIT": convert_to_github_env(data.get("ENV_INVENTORY_INIT", "")),
            "ENV_SPECIFIC_PARAMETERS": env_specific_params,
            "ENV_TEMPLATE_NAME": data.get("ENV_TEMPLATE_NAME", ""),
            "ENV_TEMPLATE_VERSION": data.get("ENV_TEMPLATE_VERSION", "")
        }

        env_file.write(f'ENV_GENERATION_PARAMS={json.dumps(env_generation_params)}\n')
        output_file.write(f'ENV_GENERATION_PARAMS={json.dumps(env_generation_params)}\n')

if __name__ == "__main__":
    main()
