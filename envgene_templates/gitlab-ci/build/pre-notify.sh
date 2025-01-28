#!/usr/bin/env bash

function log_info() {
  >&2 echo -e "[\\e[1;94mINFO\\e[0m] $*"
}

function log_warn() {
  >&2 echo -e "[\\e[1;93mWARN\\e[0m] $*"
}

function log_error() {
  >&2 echo -e "[\\e[1;91mERROR\\e[0m] $*"
}

# check number of arguments
if [[ "$#" -le 2 ]]; then
  log_error "Missing arguments"
  log_error "Usage: $0 <release type> <release url> <release notes>"
  exit 1
fi

releaseType=$1
releaseUrl=$2
releaseNotes=$3

log_info "Release type: \\e[33;1m${releaseType}\\e[0m"
log_info "Release URL: \\e[33;1m${releaseUrl}\\e[0m"
log_info "Original Release Notes (\\e[33;1m${releaseNotes}\\e[0m):"
cat $releaseNotes

releaseTitle="${CI_PROJECT_DIR}/release_title.md"
releaseBody="${CI_PROJECT_DIR}/release_body.md"
releaseLink="${CI_PROJECT_DIR}/release_link.md"
releaseNotesResult="${CI_PROJECT_DIR}/release_notes.md"
releaseTriggeredInfo="${CI_PROJECT_DIR}/triggered_info.md"
releasePipelineMetadata="${CI_PROJECT_DIR}/pipeline_metadata.env"


log_info "Updating Release Notes..."
head -n 1 ${releaseNotes} | sed -r 's/## //g' | sed "1 s/$/ - ${releaseType}/" > ${releaseTitle}.tmp && mv ${releaseTitle}.tmp ${releaseTitle}
tail -n+2 ${releaseNotes} | sed -r 's/###/####/g' > ${releaseBody}.tmp && mv ${releaseBody}.tmp ${releaseBody}
echo "🎉 The release is available on [GitLab release](${releaseUrl}) 🎉" > ${releaseLink}
cat ${releaseTitle} ${releaseBody} ${releaseLink} > ${releaseNotesResult}
log_info "Resulted Release Notes (\\e[33;1m${releaseNotesResult}\\e[0m):"
cat $releaseNotesResult

log_info "Generating Triggered Info..."
echo -n "${GITLAB_USER_NAME} [pushed](${CI_PROJECT_URL}/-/commit/${CI_COMMIT_SHA}) into '${CI_COMMIT_REF_NAME}'" > ${releaseTriggeredInfo}
log_info "Resulted Triggered Info (\\e[33;1m${releaseTriggeredInfo}\\e[0m):"
cat $releaseTriggeredInfo

log_info "Saving Pipeline Metadata..."
echo "CI_PIPELINE_ID=$CI_PIPELINE_ID" >> ${releasePipelineMetadata}
