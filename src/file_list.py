#!/usr/bin/env python3
"""指定ディレクトリ内のファイル一覧を表示する簡単なスクリプト。"""

from __future__ import annotations

import sys
from pathlib import Path


def list_files(directory: Path) -> None:
    """対象ディレクトリ内のファイル名を一覧表示する。"""
    if not directory.exists():
        raise FileNotFoundError(f"Directory does not exist: {directory}")
    if not directory.is_dir():
        raise NotADirectoryError(f"Not a directory: {directory}")

    files = sorted(path.name for path in directory.iterdir() if path.is_file())

    if not files:
        print(f"No files found in {directory}")
        return

    for filename in files:
        print(filename)


def main() -> int:
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()

    try:
        list_files(target)
    except (FileNotFoundError, NotADirectoryError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
