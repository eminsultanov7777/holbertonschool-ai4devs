from log_analyzer import LogAnalyzer
def test_normal_log_file():
    lines = [
        "2026-11-16 10:00:00 INFO Server started",
        "2026-11-16 10:05:00 WARNING High memory usage",
        "2026-11-16 10:10:00 ERROR Connection failed",
        "2026-11-16 10:15:00 INFO User logged in",
        "2026-11-16 10:20:00 ERROR Database unavailable",
    ]
    result = LogAnalyzer().analyze(lines)
    assert result == {"total_entries": 5, "info_count": 2, "warning_count": 1,
        "error_count": 2, "malformed_count": 0, "error_rate": 40.0,
        "most_common_level": "INFO"}
