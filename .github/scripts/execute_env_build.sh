#!/usr/bin/env bash
set -e

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
  -e ENVIRONMENT_NAME="${ENVIRONMENT_NAME:-""}" \
  -e GROUP_ID="" \
  -e ARTIFACT_ID="" \
  -e INSTANCES_DIR="${CI_PROJECT_DIR}/environments" \
  -e module_ansible_dir="/module/ansible" \
  -e module_inventory="${CI_PROJECT_DIR}/configuration/inventory.yaml" \
  -e module_ansible_cfg="/module/ansible/ansible.cfg" \
  -e module_config_default="/module/templates/defaults.yaml" \
  -e GIT_STRATEGY="none" \
  -e COMMIT_ENV="true" \
  -e SECRET_KEY="${SECRET_KEY:-""}" \
  -e GITHUB_ACTIONS="${GITHUB_ACTIONS:-""}" \
  -e GITHUB_REPOSITORY="${GITHUB_REPOSITORY:-""}" \
  -e GITHUB_REF_NAME="${GITHUB_REF_NAME:-""}" \
  -e GITHUB_USER_EMAIL="${GITHUB_USER_EMAIL:-""}" \
  -e GITHUB_USER_NAME="${GITHUB_USER_NAME:-""}" \
  -e GITHUB_TOKEN="${GITHUB_TOKEN:-""}" \
  ghcr.io/netcracker/qubership-build-envgene:main \
  bash -c '
      set -e

      export ENV_NAME="$ENV_NAME"
      export ENV_NAME_SHORT=$(echo "$ENV_NAME" | awk -F "/" "{print \$NF}")
      export ENVIRONMENT_NAME="$ENVIRONMENT_NAME"
      export ENV_TEMPLATE_TEST="$ENV_TEMPLATE_TEST"
      export CLUSTER_NAME="$CLUSTER_NAME"
      export CI_PROJECT_DIR="$CI_PROJECT_DIR"
      export ENV_TEMPLATE_VERSION="$ENV_TEMPLATE_VERSION"
      export GROUP_ID="$GROUP_ID"
      export ARTIFACT_ID="$ARTIFACT_ID"

      if [ -d "${CI_PROJECT_DIR}/configuration/certs" ]; then
        cert_path=$(ls -A "${CI_PROJECT_DIR}/configuration/certs")
        for path in $cert_path; do
          . /module/scripts/update_ca_cert.sh "${CI_PROJECT_DIR}/configuration/certs/$path"
        done
      fi

      if [ "$ENV_TEMPLATE_VERSION" != "" ] && [ "$ENV_TEMPLATE_TEST" == "false" ]; then
        /module/scripts/prepare.sh "set_template_version.yaml"
        /module/scripts/prepare.sh "build_env.yaml"
      else
        /module/scripts/prepare.sh "build_env.yaml"
      fi

      if [ "$ENV_TEMPLATE_TEST" == "true" ]; then
        env_name=$(cat set_variable.txt)
        sed -i "s|\\\"envgeneNullValue\\\"|\\\"test_value\\\"|g" "${CI_PROJECT_DIR}/environments/$env_name/Credentials/credentials.yml"
      else
        export env_name=$(echo "$ENV_NAME" | awk -F "/" "{print \$NF}")
      fi

      env_path=$(find "${CI_PROJECT_DIR}/environments" -type d -name "$env_name")
      for path in $env_path; do
        if [ -d "$path/Credentials" ]; then
          chmod ugo+rw "$path/Credentials/"*
        fi
      done
  '