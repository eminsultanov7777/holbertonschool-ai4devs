"""Unit tests: 12 cases for the reference Log Analyzer."""

import tempfile
import unittest
from pathlib import Path

from log_analyzer import LogAnalyzer, analyze_file


class TestLogAnalyzer(unittest.TestCase):
    def setUp(self):
        self.analyzer = LogAnalyzer()

    def test_01_normal_log_file(self):
        lines = [
            "2026-11-16 10:00:00 INFO Server started",
            "2026-11-16 10:05:00 WARNING High memory usage",
            "2026-11-16 10:10:00 ERROR Connection failed",
            "2026-11-16 10:15:00 INFO User logged in",
            "2026-11-16 10:20:00 ERROR Database unavailable",
        ]
        self.assertEqual(self.analyzer.analyze(lines), {
            "total_entries": 5, "info_count": 2, "warning_count": 1,
            "error_count": 2, "malformed_count": 0,
            "error_rate": 40.0, "most_common_level": "INFO",
        })

    def test_02_empty_input(self):
        result = self.analyzer.analyze([])
        self.assertEqual(result["total_entries"], 0)
        self.assertEqual(result["error_rate"], 0.0)
        self.assertIsNone(result["most_common_level"])

    def test_03_only_error_messages(self):
        lines = [
            "2026-11-16 10:00:00 ERROR First",
            "2026-11-16 10:01:00 ERROR Second",
            "2026-11-16 10:02:00 ERROR Third",
        ]
        result = self.analyzer.analyze(lines)
        self.assertEqual(result["error_count"], 3)
        self.assertEqual(result["error_rate"], 100.0)
        self.assertEqual(result["most_common_level"], "ERROR")

    def test_04_mixed_valid_and_malformed(self):
        lines = [
            "2026-11-16 10:00:00 INFO Started",
            "not a valid log line",
            "2026-11-16 10:01:00 ERROR Failed",
            "2026-11-16 10:02:00 INFO Retried",
            "2026-11-16 10:03:00 DEBUG Debug message",
        ]
        result = self.analyzer.analyze(lines)
        self.assertEqual(result["total_entries"], 3)
        self.assertEqual(result["malformed_count"], 2)
        self.assertEqual(result["error_rate"], 33.33)
        self.assertEqual(result["most_common_level"], "INFO")

    def test_05_equal_frequency_uses_specified_tie_order(self):
        lines = [
            "2026-11-16 10:00:00 INFO A",
            "2026-11-16 10:01:00 WARNING B",
            "2026-11-16 10:02:00 ERROR C",
        ]
        result = self.analyzer.analyze(lines)
        self.assertEqual(result["most_common_level"], "INFO")
        self.assertEqual(result["error_rate"], 33.33)

    def test_06_unsupported_level_is_malformed(self):
        lines = [
            "2026-11-16 10:00:00 INFO Started",
            "2026-11-16 10:01:00 DEBUG Details",
            "2026-11-16 10:02:00 INFO Finished",
        ]
        result = self.analyzer.analyze(lines)
        self.assertEqual(result["total_entries"], 2)
        self.assertEqual(result["malformed_count"], 1)
        self.assertEqual(result["most_common_level"], "INFO")

    def test_07_invalid_timestamp_is_malformed(self):
        result = self.analyzer.analyze([
            "not-a-date 10:00:00 ERROR Broken timestamp"
        ])
        self.assertEqual(result["total_entries"], 0)
        self.assertEqual(result["malformed_count"], 1)

    def test_08_duplicate_timestamps_are_counted(self):
        lines = [
            "2026-11-16 10:00:00 INFO First event",
            "2026-11-16 10:00:00 ERROR Second event",
        ]
        result = self.analyzer.analyze(lines)
        self.assertEqual(result["total_entries"], 2)
        self.assertEqual(result["info_count"], 1)
        self.assertEqual(result["error_count"], 1)

    def test_09_single_valid_entry(self):
        result = self.analyzer.analyze([
            "2026-11-16 10:00:00 WARNING Disk space low"
        ])
        self.assertEqual(result["total_entries"], 1)
        self.assertEqual(result["warning_count"], 1)
        self.assertEqual(result["error_rate"], 0.0)
        self.assertEqual(result["most_common_level"], "WARNING")

    def test_10_blank_line_is_malformed(self):
        result = self.analyzer.analyze([""])
        self.assertEqual(result["total_entries"], 0)
        self.assertEqual(result["malformed_count"], 1)

    def test_11_missing_file_raises_file_not_found(self):
        with tempfile.TemporaryDirectory() as directory:
            missing = Path(directory) / "missing.log"
            with self.assertRaises(FileNotFoundError):
                analyze_file(missing)

    def test_12_file_is_read_and_analyzed(self):
        with tempfile.TemporaryDirectory() as directory:
            log_path = Path(directory) / "server.log"
            log_path.write_text(
                "2026-11-16 10:00:00 INFO Server started\n"
                "2026-11-16 10:01:00 ERROR Server failed\n",
                encoding="utf-8",
            )
            result = analyze_file(log_path)
            self.assertEqual(result["total_entries"], 2)
            self.assertEqual(result["error_count"], 1)
            self.assertEqual(result["error_rate"], 50.0)


if __name__ == "__main__":
    unittest.main()
