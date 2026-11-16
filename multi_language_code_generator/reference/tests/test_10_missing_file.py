import tempfile
from pathlib import Path
import pytest
from log_analyzer import analyze_file
def test_missing_file_raises_error():
    with tempfile.TemporaryDirectory() as directory:
        missing = Path(directory) / "missing.log"
        with pytest.raises(FileNotFoundError):
            analyze_file(missing)
