#!/bin/bash
set -e

build_name="env_templates.zip"
git_location=$(git symbolic-ref -q --short HEAD || git describe --tags --exact-match)
version_file=version.txt

. ./build_vars.sh

add_git_version(
  local git_tag_branch=$1
  local file=$2
  if git tag --list |grep -q -e "^$git_tag_branch$"; then
    git_line=tags/$git_tag_branch
  elif git branch -r |grep -q -e "origin/$git_tag_branch$"; then
    git_line=origin/$git_tag_branch
  else
    git_line=$git_tag_branch
  fi
  git show --format=format:'date:          %ci
commit hash:   %H
branch or tag: %d%n' -s "$git_line" >> "$file"
}

# backup
cp .gitlab-ci.yml .gitlab-ci.yml_bk

# Remove NC specific values
sed -i '/# CUT OFF FOR OPERATIONS PORTAL START/,/# CUT OFF FOR OPERATIONS PORTAL END/d' ./.gitlab-ci.yml
sed -i 's/# portal_uncomment //g' ./.gitlab-ci.yml

# Add version file
add_git_version "$git_location" "$version_file"

rm -f "$build_name"

mkdir -p ./target

echo "Create repo archive"

# zip -r "target/${build_name}" \
#     -x="target/${build_name}" \
#     -x="description_template.yaml" \
#     -x='manifest/*' \
#     -x='.gitlab-ci.yml_bk' . *

zip -r "target/${build_name}" templates

echo "Archive has been created"

# restore
mv .gitlab-ci.yml_bk .gitlab-ci.yml
rm -f $version_file

echo "done."

mvn org.apache.maven.plugins:maven-deploy-plugin:2.7:deploy-file \
  -DgeneratePom=false \
  -Durl=file:/localRepositories/pd.sandbox.mvn.staging/ \
  -DrepositoryId=pd.sandbox.mvn.staging \
  -DgroupId=com.netcracker.deploy.product \
  -DartifactId=${artifact_id} \
  -Dversion=${DVERSION} \
  -Dfile=target/${build_name} \
  -Dpackaging=zip
