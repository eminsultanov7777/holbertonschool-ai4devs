from log_analyzer import LogAnalyzer
def test_mixed_valid_and_malformed():
    lines = ["2026-11-16 10:00:00 INFO Started", "bad line",
             "2026-11-16 10:01:00 ERROR Failed",
             "2026-11-16 10:02:00 INFO Retried",
             "2026-11-16 10:03:00 DEBUG Debug"]
    result = LogAnalyzer().analyze(lines)
    assert result["total_entries"] == 3
    assert result["malformed_count"] == 2
    assert result["error_rate"] == 33.33
    assert result["most_common_level"] == "INFO"
