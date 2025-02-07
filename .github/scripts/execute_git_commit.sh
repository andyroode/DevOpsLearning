#!/usr/bin/env bash
set -e

CLUSTER_NAME=$(echo "$ENV_NAME" | cut -d'/' -f1)
ENVIRONMENT_NAME=$(echo "$ENV_NAME" | cut -d'/' -f2)

GITHUB_USER_EMAIL="${GITHUB_USER_EMAIL}"
GITHUB_USER_NAME="${GITHUB_USER_NAME}"
GITHUB_TOKEN="${GITHUB_TOKEN}"

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
  -e module_ansible_dir="/module/ansible" \
  -e module_inventory="${CI_PROJECT_DIR}/configuration/inventory.yaml" \
  -e module_ansible_cfg="/module/ansible/ansible.cfg" \
  -e module_config_default="/module/templates/defaults.yaml" \
  -e GIT_STRATEGY="none" \
  -e COMMIT_ENV="true" \
  -e GITHUB_ACTIONS="${GITHUB_ACTIONS:-""}" \
  -e GITHUB_REPOSITORY="${GITHUB_REPOSITORY:-""}" \
  -e GITHUB_REF_NAME="${GITHUB_REF_NAME:-""}" \
  -e GITHUB_USER_EMAIL="${GITHUB_USER_EMAIL}" \
  -e GITHUB_USER_NAME="${GITHUB_USER_NAME}" \
  -e GITHUB_TOKEN="${GITHUB_TOKEN}" \
  ghcr.io/netcracker/qubership-build-envgene:main \
  bash -c "
    set -e

    export ENV_NAME=\"$ENV_NAME\"
    export ENV_NAME_SHORT=\$(echo \"\$ENV_NAME\" | awk -F '/' '{print \$NF}')
    export ENVIRONMENT_NAME=\"$ENVIRONMENT_NAME\"

    echo 'Prepare git_commit job for \${ENVIRONMENT_NAME}...'

    echo 'Installing the certs if exist...'
    if [ -d \"\${CI_PROJECT_DIR}/configuration/certs\" ]; then
      cert_path=\$(find \"\${CI_PROJECT_DIR}/configuration/certs\" -type f)
      if [ -n \"\$cert_path\" ]; then
        for path in \$cert_path; do
          . /module/scripts/update_ca_cert.sh \"\$path\"
        done
      fi
    fi


    /module/scripts/prepare.sh \"git_commit.yaml\"

    env_path=\$(sudo find \"\$CI_PROJECT_DIR/environments\" -type d -name \"\$ENV_NAME_SHORT\")
    echo \"Found environment path: \$env_path\"

    for path in \$env_path; do
      if [ -d \"\$path/Credentials\" ]; then
        sudo chmod ugo+rw \"\$path/Credentials\"/*
      fi
    done

    cp -rf \"\$CI_PROJECT_DIR/environments\" \"\$CI_PROJECT_DIR/git_envs\"
  "