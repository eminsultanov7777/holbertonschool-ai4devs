from log_analyzer import LogAnalyzer
def test_invalid_timestamp_is_malformed():
    result = LogAnalyzer().analyze(["not-a-date 10:00:00 ERROR Broken"])
    assert result["total_entries"] == 0
    assert result["malformed_count"] == 1
