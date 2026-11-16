from log_analyzer import LogAnalyzer
def test_tie_breaking_prefers_info():
    lines = ["2026-11-16 10:00:00 INFO A",
             "2026-11-16 10:01:00 WARNING B",
             "2026-11-16 10:02:00 ERROR C"]
    assert LogAnalyzer().analyze(lines)["most_common_level"] == "INFO"
