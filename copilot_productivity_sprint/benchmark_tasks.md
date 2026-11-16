# Benchmark Tasks

This document defines three Python programming tasks for the Copilot Productivity Sprint.

Each task is designed to take approximately 15–30 minutes. The same tasks will be completed twice: first without AI assistance and then with GitHub Copilot.

---

## Task 1 - Word Counter

**Estimated Time:** 15–20 minutes

### Requirements
Create a Python program that reads a text file and analyzes its contents.

The program must:
- Read text from a file named `text.txt`.
- Count the total number of words.
- Calculate the frequency of each word.
- Display the five most common words.
- Handle an empty or missing file.
- Ignore differences between uppercase and lowercase letters.

### Inputs
- A text file named `text.txt` containing plain text.

### Outputs
- Total number of words.
- The five most frequently used words and their frequencies.
- An appropriate error message if the file is missing or empty.

### Acceptance Criteria
- Correctly counts all words.
- Correctly identifies the five most common words.
- Treats uppercase and lowercase versions of a word as identical.
- Handles missing and empty files without crashing.

---

## Task 2 - CSV Data Analyzer

**Estimated Time:** 20–25 minutes

### Requirements
Create a Python program that reads a CSV file and generates a basic data summary.

The program must:
- Read data from a file named `data.csv`.
- Count the total number of rows.
- Display all column names.
- Identify missing or empty values in each column.
- Calculate the average of a specified numeric column.
- Handle missing or invalid CSV files.

### Inputs
A CSV file named `data.csv` containing sample records with at least three columns, including one numeric column.

Example:

```csv
name,age,score
Alice,22,85
Bob,25,90
Charlie,,75
David,23,80
```

### Outputs
- Total number of records.
- List of column names.
- Number of missing values in each column.
- Average value of the numeric score column.
- Error message if the CSV file cannot be read.

### Acceptance Criteria
- Correctly counts the CSV records.
- Displays all column names.
- Correctly identifies missing values.
- Calculates the correct average of valid numeric values.
- Handles missing files and invalid data without crashing.

---

## Task 3 - Log File Analyzer

**Estimated Time:** 20–30 minutes

### Requirements
Create a Python program that analyzes a server log file.

The program must:
- Read log entries from a file named `server.log`.
- Count INFO, WARNING, and ERROR messages.
- Display the total number of log entries.
- Identify the most common log level.
- Handle missing or empty log files.

### Inputs
A text file named `server.log` containing log entries.

Example:

```text
2026-11-16 10:00:00 INFO Server started
2026-11-16 10:05:00 WARNING High memory usage
2026-11-16 10:10:00 ERROR Connection failed
2026-11-16 10:15:00 INFO User logged in
2026-11-16 10:20:00 ERROR Database unavailable
```

### Outputs
- Total number of log entries.
- Number of INFO messages.
- Number of WARNING messages.
- Number of ERROR messages.
- Most common log level.
- Error message if the log file is missing or empty.

### Acceptance Criteria
- Correctly counts INFO, WARNING, and ERROR messages.
- Calculates the total number of log entries.
- Identifies the most common log level.
- Handles empty and missing files without crashing.
- Produces readable and clearly structured output.

---

## Benchmark Evaluation Method

Each task will be completed using two approaches:

1. **Without AI:** Write and test the solution independently.
2. **With AI:** Complete the same task using GitHub Copilot.

The following metrics will be recorded:

- Time required to complete the task.
- Lines of code written.
- Number of errors encountered.
- Test results and code correctness.
- Overall code quality.

The results will be compared to evaluate the impact of AI assistance on programming productivity.
