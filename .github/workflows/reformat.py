import os
import re
import sys

template = """
name: Build and Deploy TOOL_NAME VERSION to GHCR
on:
  push:
    branches:
      - prod
    paths:
      - "tools/TOOL_NAME/vVERSION/**"

env:
  REGISTRY: ghcr.io
  ORG: scleestacks
  REPOSITORY: TOOL_NAME
  VER: VERSION
  BUILD_PATH: tools/TOOL_NAME/vVERSION

permissions:
  contents: read
  packages: write

jobs:
  deploy:
    name: Deploy
    runs-on: ubuntu-latest
    environment: production

    steps:
      - name: Checkout
        uses: actions/checkout@v3

      - name: Login to GHCR
        run: echo "${{ secrets.GHCR_PAT }}" | docker login ghcr.io -u ${{ github.actor }} --password-stdin

      - name: Add SHORT_SHA env property with commit short sha
        run: echo "SHORT_SHA=`echo ${{ github.sha }} | cut -c1-7`" >> $GITHUB_ENV

      - name: Build, tag, and push docker image to GHCR
        run: |
          docker build -t $REGISTRY/$ORG/$REPOSITORY:$VER $BUILD_PATH
          docker push $REGISTRY/$ORG/$REPOSITORY:$VER
"""

def replace_placeholders(template, tool_name, version):
    version_with_v = f"v{version}"
    # Replace TOOL_NAME and VERSION placeholders
    result = template.replace('TOOL_NAME', tool_name)
    # Replace instances of '/VERSION' with '/vVERSION'
    result = result.replace('/VERSION', f'/{version_with_v}')
    # Replace other instances of 'VERSION' with the plain version
    result = result.replace('VERSION', version)
    return result

def process_yaml_file(file_path):
    # Extract tool name and version from the filename
    file_name = os.path.basename(file_path)
    match = re.match(r'(.+)-v(\d+\.\d+\.\d+)\.yml', file_name)
    if not match:
        raise ValueError(f"Filename '{file_name}' does not match the expected pattern.")

    tool_name, version = match.groups()

    # Replace placeholders in the template
    new_content = replace_placeholders(template, tool_name, version)

    # Overwrite the existing file with the new content
    with open(file_path, 'w') as file:
        file.write(new_content)

    print(f"Processed file saved as {file_path}")

def process_directory(directory_path):
    for file_name in os.listdir(directory_path):
        if file_name.endswith('.yml'):
            file_path = os.path.join(directory_path, file_name)
            process_yaml_file(file_path)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <path_to_directory>")
        sys.exit(1)

    directory_path = sys.argv[1]
    if not os.path.isdir(directory_path):
        print(f"The path '{directory_path}' is not a directory.")
        sys.exit(1)

    process_directory(directory_path)

