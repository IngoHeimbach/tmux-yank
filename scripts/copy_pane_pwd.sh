#!/usr/bin/env bash

CURRENT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
HELPERS_DIR="$CURRENT_DIR"

# shellcheck source=scripts/helpers.sh
source "${HELPERS_DIR}/helpers.sh"

pane_current_path() {
    tmux display -p -F "#{pane_current_path}"
}

display_notice() {
    if [[ "${1}" = "pastebuffer" ]]; then
        display_message 'PWD copied to tmux paste buffer!'
    else
        display_message 'PWD copied to clipboard!'
    fi
}

main() {
    local copy_command
    local payload
    # shellcheck disable=SC2119
    if [[ "${1}" = "pastebuffer" ]]; then
        copy_command="$(tmux_copy_command)"
    else
        copy_command="$(clipboard_copy_command)"
    fi
    payload="$(pane_current_path | tr -d '\n')"
    # $copy_command below should not be quoted
    echo "$payload" | $copy_command
    tmux set-buffer "$payload"
    display_notice "${1}"
}
main "$@"
