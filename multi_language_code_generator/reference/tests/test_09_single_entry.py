from log_analyzer import LogAnalyzer
def test_single_valid_entry():
    result = LogAnalyzer().analyze(["2026-11-16 10:00:00 WARNING Disk low"])
    assert result["total_entries"] == 1
    assert result["warning_count"] == 1
    assert result["error_rate"] == 0.0
    assert result["most_common_level"] == "WARNING"
