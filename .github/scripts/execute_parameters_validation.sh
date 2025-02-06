#!/usr/bin/env bash
set -e

docker run --rm \
  -v "$GITHUB_WORKSPACE:/repo" \
  -w /repo \
  -e CI_PROJECT_DIR="/repo" \
  -e ENV_NAMES="${ENV_NAMES:-""}" \
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
  ghcr.io/netcracker/qubership-build-gcip:main \
  python /module/scripts/github_actions.py validate_pipeline