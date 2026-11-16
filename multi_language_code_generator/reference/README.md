# Reference Implementation

This folder contains the Python baseline implementation for the Log Analyzer.

## Files

- `log_analyzer.py` — reference implementation and command-line entry point.
- `tests/test_log_analyzer.py` — 12 automated unit tests.

## Run the analyzer

From this `reference` directory:

```bash
python3 log_analyzer.py server.log
```

If no path is supplied, the program reads `server.log` from the current directory.

## Run the tests

```bash
python3 -m unittest discover -s tests -v
```

The implementation treats unsupported log levels, invalid timestamps, blank lines,
and malformed records as malformed. The most-common-level tie order is INFO,
then WARNING, then ERROR, as defined in the specification.
