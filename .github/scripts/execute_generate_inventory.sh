#!/usr/bin/env bash
set -e

ENV_GENERATION_PARAMS="$(jq -nc \
  --arg sd_source_type "$SD_SOURCE_TYPE" \
  --arg sd_version "$SD_VERSION" \
  --arg sd_data "$SD_DATA" \
  --arg sd_delta "$SD_DELTA" \
  --arg env_inventory_init "$ENV_INVENTORY_INIT" \
  --arg env_specific_params "$ENV_SPECIFIC_PARAMETERS" \
  --arg env_template_name "$ENV_TEMPLATE_NAME" \
  --arg env_template_version "$ENV_TEMPLATE_VERSION" \
  '{
    "SD_SOURCE_TYPE": $sd_source_type,
    "SD_VERSION": $sd_version,
    "SD_DATA": $sd_data,
    "SD_DELTA": $sd_delta,
    "ENV_INVENTORY_INIT": $env_inventory_init,
    "ENV_SPECIFIC_PARAMETERS": $env_specific_params,
    "ENV_TEMPLATE_NAME": $env_template_name,
    "ENV_TEMPLATE_VERSION": $env_template_version
  }'
)"

CLUSTER_NAME=$(echo "$ENV_NAME" | cut -d'/' -f1)
ENVIRONMENT_NAME=$(echo "$ENV_NAME" | cut -d'/' -f2 | xargs)

export ENV_GENERATION_PARAMS
export CLUSTER_NAME

docker run --rm \
  -v "$GITHUB_WORKSPACE:/repo" \
  -w /repo \
  -e CI_PROJECT_DIR="${CI_PROJECT_DIR:-""}" \
  -e ENV_NAME="${ENV_NAME:-""}" \
  -e ENV_BUILDER="${ENV_BUILDER:-""}" \
  -e GENERATE_EFFECTIVE_SET="${GENERATE_EFFECTIVE_SET:-""}" \
  -e ENV_TEMPLATE_VERSION="${ENV_TEMPLATE_VERSION:-""}" \
  -e ENV_TEMPLATE_TEST="${ENV_TEMPLATE_TEST:-""}" \
  -e IS_OFFSITE="${IS_OFFSITE:-""}" \
  -e JSON_SCHEMAS_DIR="${JSON_SCHEMAS_DIR:-""}" \
  -e SD_DATA="${SD_DATA:-"{}"}" \
  -e SD_VERSION="${SD_VERSION:-""}" \
  -e ENV_INVENTORY_INIT="${ENV_INVENTORY_INIT:-""}" \
  -e CI_COMMIT_REF_NAME="${CI_COMMIT_REF_NAME:-""}" \
  -e ENV_GENERATION_PARAMS="${ENV_GENERATION_PARAMS:-""}" \
  -e CLUSTER_NAME="${CLUSTER_NAME:-""}" \
  ghcr.io/netcracker/qubership-build-envgene:main \
  python3 /build_env/scripts/build_env/env_inventory_generation.py