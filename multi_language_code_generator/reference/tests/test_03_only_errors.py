from log_analyzer import LogAnalyzer
def test_only_error_messages():
    lines = [f"2026-11-16 10:0{i}:00 ERROR Failure {i}" for i in range(3)]
    result = LogAnalyzer().analyze(lines)
    assert result["error_count"] == 3
    assert result["error_rate"] == 100.0
    assert result["most_common_level"] == "ERROR"
