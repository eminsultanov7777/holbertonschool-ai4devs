# Cross-Language Specification — Log Analyzer

## 1. Algorithm Description

The Log Analyzer is a program designed to read and analyze server log files.

The algorithm processes log entries and generates statistical information about system events.

The program must:

- Read log entries from a text file.
- Count the total number of log entries.
- Count INFO, WARNING, and ERROR messages.
- Calculate the error rate as a percentage of valid log entries.
- Identify the most common log level.
- Ignore malformed entries and count them separately.

The algorithm will be implemented in three programming languages:

- Python
- JavaScript (Node.js)
- Go

All implementations must produce equivalent results for the same input data.

## 2. Input Format

The program receives a text file named `server.log`.

Each valid log entry must follow this format:

```text
YYYY-MM-DD HH:MM:SS LEVEL Message
```

Supported log levels:

- INFO
- WARNING
- ERROR

Example:

```text
2026-11-16 10:00:00 INFO Server started
2026-11-16 10:05:00 WARNING High memory usage
2026-11-16 10:10:00 ERROR Connection failed
2026-11-16 10:15:00 INFO User logged in
2026-11-16 10:20:00 ERROR Database unavailable
```

## 3. Output Format

The program must return a JSON object containing:

- total_entries
- info_count
- warning_count
- error_count
- malformed_count
- error_rate
- most_common_level

Example:

```json
{
  "total_entries": 5,
  "info_count": 2,
  "warning_count": 1,
  "error_count": 2,
  "malformed_count": 0,
  "error_rate": 40.0,
  "most_common_level": "INFO"
}
```

The error rate is calculated using:

ERROR count / valid entries * 100.

If there are no valid entries, the error rate must be 0.0.

If multiple log levels have the same highest frequency, the result must be the first level in this order: INFO, WARNING, ERROR.

## 4. Edge Cases

The algorithm must handle:

1. Empty log file.
2. Missing log file.
3. File containing only malformed entries.
4. Entries with unsupported log levels.
5. Multiple entries with the same timestamp.
6. Files containing only one valid log entry.
7. Log files containing a mixture of valid and malformed entries.

Malformed entries must not be included in valid log statistics.

## 5. Test Cases

### Test Case 1 - Normal Log File

**Input:** 5 valid entries:
- 2 INFO
- 1 WARNING
- 2 ERROR

**Expected Output:**
- total_entries: 5
- info_count: 2
- warning_count: 1
- error_count: 2
- malformed_count: 0
- error_rate: 40.0
- most_common_level: INFO

### Test Case 2 - Empty File

**Input:** Empty log file.

**Expected Output:**
- total_entries: 0
- info_count: 0
- warning_count: 0
- error_count: 0
- malformed_count: 0
- error_rate: 0.0
- most_common_level: null

### Test Case 3 - Only ERROR Messages

**Input:** 3 valid ERROR entries.

**Expected Output:**
- total_entries: 3
- info_count: 0
- warning_count: 0
- error_count: 3
- malformed_count: 0
- error_rate: 100.0
- most_common_level: ERROR

### Test Case 4 - Mixed Valid and Malformed Entries

**Input:**
- 2 valid INFO entries.
- 1 valid ERROR entry.
- 2 malformed entries.

**Expected Output:**
- total_entries: 3
- info_count: 2
- warning_count: 0
- error_count: 1
- malformed_count: 2
- error_rate: 33.33
- most_common_level: INFO

### Test Case 5 - Equal Frequency

**Input:**
- 1 INFO entry.
- 1 WARNING entry.
- 1 ERROR entry.

**Expected Output:**
- total_entries: 3
- info_count: 1
- warning_count: 1
- error_count: 1
- malformed_count: 0
- error_rate: 33.33
- most_common_level: INFO

### Test Case 6 - Unsupported Log Level

**Input:**
- 2 valid INFO entries.
- 1 entry with unsupported level DEBUG.

**Expected Output:**
- total_entries: 2
- info_count: 2
- warning_count: 0
- error_count: 0
- malformed_count: 1
- error_rate: 0.0
- most_common_level: INFO

## 6. Functional Equivalence Requirements

All three implementations (Python, JavaScript, and Go) must:

- Follow the same input format.
- Apply identical validation rules.
- Calculate statistics using the same formulas.
- Handle all specified edge cases.
- Produce equivalent JSON outputs.

The implementations will be tested using the same test cases.

## 7. Performance Benchmarking

Each implementation will be tested using identical log files.

The following metrics will be measured:

- Execution time.
- Memory usage.
- Correctness of results.

The benchmark results will be documented and compared.
