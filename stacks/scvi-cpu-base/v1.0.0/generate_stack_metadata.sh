#!/bin/bash
set -e

# This script locates and executes a Python script to generate metadata files along side the image build files.
# It searches for a .config file at the project root to find the name of the Python script (METADATA_SCRIPT_NAME).
# Then, it searches for the Python script, generate_stack_metadata.py in the scripts directory at the project root.

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CONFIG_FILE=""
METADATA_SCRIPT_PATH=""

# Search for the .config file in parent directories
while [ "$SCRIPT_DIR" != "/" ]; do
    if [ -f "$SCRIPT_DIR/.config" ]; then
        CONFIG_FILE="$SCRIPT_DIR/.config"
        break
    fi
    SCRIPT_DIR="$(dirname "$SCRIPT_DIR")"
done

if [ -z "$CONFIG_FILE" ]; then
    echo "ERROR: Could not find .config file"
    exit 1
fi

source "$CONFIG_FILE"

# Search for the main script in parent directories
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
while [ "$SCRIPT_DIR" != "/" ]; do
    if [ -f "$SCRIPT_DIR/scripts/$METADATA_SCRIPT_NAME" ]; then
        METADATA_SCRIPT_PATH="$SCRIPT_DIR/scripts/$METADATA_SCRIPT_NAME"
        break
    fi
    SCRIPT_DIR="$(dirname "$SCRIPT_DIR")"
done

if [ -z "$METADATA_SCRIPT_PATH" ]; then
    echo "ERROR: Could not find $METADATA_SCRIPT_NAME"
    exit 1
fi

"$METADATA_SCRIPT_PATH"

