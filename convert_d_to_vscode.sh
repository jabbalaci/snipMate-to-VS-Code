#!/usr/bin/env bash

PRG="convert_snippet_to_vscode.py"
DEST_DIR="$HOME/Dropbox/share/vscode_settings_windows_linux/snippets"
#
SNIPPET="d.snippets"
VSCODE="d.json"

python3 $PRG $SNIPPET
# python3 $PRG $SNIPPET >${DEST_DIR}/${VSCODE}
