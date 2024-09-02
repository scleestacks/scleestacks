#!/usr/bin/env python3

"""
This Python script is executed by the generate_metadata.sh bash script present
in-place along side each image build file. It generates metadata files by
extracting version information from a Dockerfile. The bash script locates this
script based on the METADATA_SCRIPT_NAME variable defined in a .config file at
the project root.
"""

import os
import yaml
import json
from datetime import datetime, timezone
import re


def extract_versions_from_dockerfile():
    versions = {}
    with open('Dockerfile', 'r') as f:
        for line in f:
            match = re.search(
                r'FROM ghcr.io/scleestacks/(\w+):(\d+\.\d+\.\d+)\s+AS\s+(\w+)',
                line
            )
            if match:
                app_name = match.group(3).capitalize()
                version = match.group(2)
                versions[app_name] = version
    return versions


def insert_labels_into_dockerfile(labels):
    with open('Dockerfile', 'r') as f:
        lines = f.readlines()

    # Check if labels are already present and if versions match
    labels_present = False
    for line in lines:
        if re.search(r'org\.opencontainers\.image\.stack_name\s*=', line):
            labels_present = True
            break

    if labels_present:
        print("Labels with the same stack version"
              "are already present in the Dockerfile.")
        return

    final_stage_found = False
    new_lines = []
    for line in lines:
        new_lines.append(line)
        if re.search(r'FROM .+ AS final', line):
            final_stage_found = True
            new_lines.append('\n' + labels + '\n')

    if final_stage_found:
        with open('Dockerfile', 'w') as f:
            f.writelines(new_lines)
    else:
        raise ValueError("No 'final' stage found in Dockerfile.")


# Get stack version from directory name
stack_version = os.path.basename(os.getcwd()).lstrip('v')
if not re.match(r'^\d+\.\d+\.\d+$', stack_version):
    raise ValueError(
        "Invalid directory name format. Expected 'vX.Y.Z' "
        "where X, Y, and Z are numbers."
    )

# Get stack name from parent directory name
stack_name = os.path.basename(os.path.dirname(os.getcwd()))

created_at = datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')

# Extract versions from Dockerfile
versions = extract_versions_from_dockerfile()

# Generate versions.yml
versions_data = {
    'stack_version': stack_version,
    'stack_name': stack_name,
    'created_at': created_at,
    'applications': [{'name': k, 'version': v} for k, v in versions.items()]
}

with open('versions.yml', 'w') as f:
    yaml.dump(versions_data, f)

# Generate versions.json
with open('versions.json', 'w') as f:
    json.dump(versions_data, f, indent=2)

# Generate Dockerfile labels
labels = (
    "# Auto-generated labels\n"
    f'LABEL org.opencontainers.image.source="https://github.com/scleestacks/scleestacks" \\\n'
    f'      maintainer="Chris Tastad <christopher.tastad@mssm.edu>" \\\n'
    f'      org.opencontainers.image.stack_name="{stack_name}" \\\n'
    f'      org.opencontainers.image.version="{stack_version}" \\\n'
)
for app, version in versions.items():
    labels += (
        f'      org.scleestacks.{app.lower().replace(" ", "-")}.version="{version}" \\\n'
    )
labels = labels.rstrip(" \\\n")  # Remove the trailing backslash and newline

# Insert labels into Dockerfile
insert_labels_into_dockerfile(labels)

# Generate README.md section
with open('README_versions.md', 'w') as f:
    f.write("## Stack Versions\n\n")
    f.write(f"Stack Name: {stack_name}\n\n")
    f.write(f"Stack Version: {stack_version}\n\n")
    f.write("| Application | Version |\n")
    f.write("|-------------|---------|\n")
    for app, version in versions.items():
        f.write(f"| {app} | {version} |\n")

# Generate build-args.env
with open('build-args.env', 'w') as f:
    f.write(f"STACK_VERSION={stack_version}\n")
    f.write(f"STACK_NAME={stack_name}\n")
    for app, version in versions.items():
        f.write(f"{app.upper().replace(' ', '_')}_VERSION={version}\n")

print("Metadata files generated and Dockerfile updated successfully.")
