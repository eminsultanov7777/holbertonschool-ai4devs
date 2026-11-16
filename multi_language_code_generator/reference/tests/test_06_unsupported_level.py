from log_analyzer import LogAnalyzer
def test_unsupported_level_is_malformed():
    lines = ["2026-11-16 10:00:00 INFO Started",
             "2026-11-16 10:01:00 DEBUG Details"]
    result = LogAnalyzer().analyze(lines)
    assert result["total_entries"] == 1
    assert result["malformed_count"] == 1
