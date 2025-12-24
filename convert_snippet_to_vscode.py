#!/usr/bin/env python3

import json
import sys


def to_dict(lines: list[str]) -> tuple[dict, str]:
    if len(lines) == 0:
        return {}, ""
    # else
    d = {"prefix": "", "body": [], "description": ""}
    first_line = lines.pop(0)
    assert first_line.startswith("snippet "), f"Error: the first line is '{first_line}'"
    key = first_line.removeprefix("snippet ").strip()
    d["body"] = [line.removeprefix("\t").replace("\t", "    ") for line in lines]
    desc = d["body"][0]
    d["description"] = desc  # long version
    limit = 25
    if len(desc) > limit:
        desc = desc[:limit].strip() + "..."
    d["prefix"] = f"{key} {desc}"  # short description is used

    return d, key


def process(fname: str) -> None:
    result = {}
    entry_lines = []
    with open(fname) as f:
        for line in f:
            line = line.rstrip("\r\n")
            if line.startswith("#"):
                continue
            # else
            if line.startswith("snippet "):
                d, key = to_dict(entry_lines)
                if d:
                    result[key] = d
                #
                entry_lines = [line]
            else:
                entry_lines.append(line)
            #
        #
    #
    d, key = to_dict(entry_lines)
    if d:
        result[key] = d
    #
    print(
        f"// DON'T EDIT THIS FILE MANUALLY! It's generated from `{fname}`. Edit `{fname}` instead."
    )
    print(f"// Location: ~/Dropbox/home/jabba/.config/nvim.ks/snippets/{fname}")
    print(json.dumps(result, indent=4))


def main() -> None:
    args = sys.argv[1:]
    if len(args) != 1:
        print("Error: provide a snippet file", file=sys.stderr)
        exit(1)
    # else
    fname = args[0]
    process(fname)


##############################################################################

if __name__ == "__main__":
    main()
