# Test Failure Analysis Prompt Template

**Role**: Act as a test automation engineer investigating failing tests.

**Task**: Analyze the failing test output alongside the test and application code. Identify likely causes and distinguish product defects from test, environment, or data issues.

**Input Placeholders**:
- [TEST_FAILURE_OUTPUT]
- [TEST_CODE]
- [RELATED_APPLICATION_CODE]
- [TEST_ENVIRONMENT]

**Expected Output**:
1. Summary of the failure.
2. Likely cause(s) with supporting evidence.
3. Recommended investigation steps.
4. Proposed correction to the test or application code, clearly identifying which one.
5. Regression checks to run afterward.
