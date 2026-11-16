"""Reference implementation for the cross-language Log Analyzer."""

from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Iterable
import json
import sys


class LogAnalyzer:
    """Analyze log lines using the rules in cross_language_spec.md."""

    LEVELS = ("INFO", "WARNING", "ERROR")
    TIMESTAMP_FORMAT = "%Y-%m-%d %H:%M:%S"

    def parse_line(self, line: str) -> dict | None:
        """Return a parsed record, or None when the line is malformed."""
        parts = line.strip().split(maxsplit=3)

        if len(parts) != 4:
            return None

        date_part, time_part, level, message = parts

        if level not in self.LEVELS or not message.strip():
            return None

        try:
            datetime.strptime(
                f"{date_part} {time_part}", self.TIMESTAMP_FORMAT
            )
        except ValueError:
            return None

        return {
            "timestamp": f"{date_part} {time_part}",
            "level": level,
            "message": message.strip(),
        }

    def analyze(self, lines: Iterable[str]) -> dict:
        """Analyze lines and return the required statistics."""
        counts = {level: 0 for level in self.LEVELS}
        total_entries = 0
        malformed_count = 0

        for line in lines:
            # Blank lines are malformed entries, consistent across languages.
            record = self.parse_line(line)
            if record is None:
                malformed_count += 1
                continue

            total_entries += 1
            counts[record["level"]] += 1

        if total_entries == 0:
            error_rate = 0.0
            most_common_level = None
        else:
            error_rate = round((counts["ERROR"] / total_entries) * 100, 2)
            # max() keeps the first item on ties, following LEVELS order.
            most_common_level = max(
                self.LEVELS, key=lambda level: counts[level]
            )

        return {
            "total_entries": total_entries,
            "info_count": counts["INFO"],
            "warning_count": counts["WARNING"],
            "error_count": counts["ERROR"],
            "malformed_count": malformed_count,
            "error_rate": error_rate,
            "most_common_level": most_common_level,
        }


def analyze_file(file_path: str | Path) -> dict:
    """Read a UTF-8 log file and analyze it."""
    path = Path(file_path)
    with path.open("r", encoding="utf-8") as log_file:
        return LogAnalyzer().analyze(log_file)


def main() -> int:
    """Run the analyzer against server.log in the current directory."""
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("server.log")

    try:
        result = analyze_file(path)
    except FileNotFoundError:
        print(f"Error: log file not found: {path}", file=sys.stderr)
        return 1
    except OSError as error:
        print(f"Error: cannot read log file: {error}", file=sys.stderr)
        return 1

    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
