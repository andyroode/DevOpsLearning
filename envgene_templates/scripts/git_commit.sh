#!/bin/bash
set -e
retries=0
exit_code=0

exclude_files=("GAV_coordinates.yaml" "archive.yaml" "generated-config.yml")
for file in *; do
    if [[ ! " ${exclude_files[@]} " =~ " $file " ]]; then
        git add -f "$file"
    fi
done

git checkout ${CI_COMMIT_REF_NAME}
git commit --allow-empty -m "feat: ${CI_COMMIT_MESSAGE}"

# echo "exit CODE: ${exit_code}"
if [ "$exit_code" -ne 0 ]
then
    while [ "$exit_code" -ne 0 ] && [ "$retries" -ne 10 ]
    do
        echo "fail to push, retries: $retries"
        exit_code=0
        retries=$((retries+1))
        echo "Try to pull changes"
        git pull origin ${CI_COMMIT_REF_NAME}
        echo "Try to push, retries: $retries"
        git push origin HEAD:${CI_COMMIT_REF_NAME} || exit_code=$?
        sleep 5
    done
fi
