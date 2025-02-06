#!/usr/bin/env python3
import sys
import yaml
import json
import os

def getenv_and_log(key, default=""):
    """ Функция для получения переменной окружения с логированием """
    value = os.getenv(key, default)
    print(f"{key}: {value}")  # Для отладки
    return value

def sanitize_json(value):
    """ Преобразует многострочный YAML в JSON-строку """
    if isinstance(value, str):
        try:
            return json.dumps(json.loads(value))  # Попытка загрузить как JSON и пересобрать
        except json.JSONDecodeError:
            return json.dumps(value)  # Если не JSON, просто в кавычки
    elif isinstance(value, dict):
        return json.dumps(value)  # Если уже dict, просто превращаем в JSON строку
    return str(value)

def main():
    if len(sys.argv) < 2:
        print("Usage: load_env_params.py <yaml_config_file>")
        sys.exit(1)

    config_file = sys.argv[1]

    # Загружаем YAML
    with open(config_file, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)

    # Преобразуем в ENV-формат для GitHub Actions
    with open(os.getenv('GITHUB_ENV'), 'a', encoding='utf-8') as env_file:
        for key, value in data.items():
            if key == "ENV_SPECIFIC_PARAMETERS":
                value = sanitize_json(value)  # Преобразуем в одну JSON-строку

            env_file.write(f"{key}={value}\n")  # Записываем в переменные окружения

        # ✅ Формируем ENV_GENERATION_PARAMS как JSON-объект для дальнейшего использования
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

        # ✅ Записываем ENV_GENERATION_PARAMS в виде JSON-строки в ENV
        env_file.write(f'ENV_GENERATION_PARAMS={json.dumps(env_generation_params)}\n')

if __name__ == "__main__":
    main()
