from log_analyzer import LogAnalyzer
def test_empty_input():
    result = LogAnalyzer().analyze([])
    assert result["total_entries"] == 0
    assert result["error_rate"] == 0.0
    assert result["most_common_level"] is None
