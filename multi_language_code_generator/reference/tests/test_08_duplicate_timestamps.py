from log_analyzer import LogAnalyzer
def test_duplicate_timestamps_are_counted():
    lines = ["2026-11-16 10:00:00 INFO First",
             "2026-11-16 10:00:00 ERROR Second"]
    result = LogAnalyzer().analyze(lines)
    assert result["total_entries"] == 2
    assert result["info_count"] == 1
    assert result["error_count"] == 1
