# Unit Test Generation Prompt Template

**Role**: Act as a software test engineer experienced with [TEST_FRAMEWORK].

**Task**: Create unit tests for the supplied function or component. Cover normal behavior, edge cases, and invalid inputs where applicable. Do not change the production code unless asked.

**Input Placeholders**:
- [SOURCE_CODE]
- [EXPECTED_BEHAVIOR]
- [LANGUAGE_AND_TEST_FRAMEWORK]

**Expected Output**:
1. Runnable unit-test code in a code block.
2. A brief description of each test.
3. Any assumptions or missing cases.
4. Instructions for running the tests, if known.
