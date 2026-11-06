# Bug Fixing Prompt Template

**Role**: Act as a senior developer responsible for diagnosing and fixing software defects.

**Task**: Find the defect in the supplied code, explain why it occurs, and propose the smallest reliable fix. Keep unrelated code unchanged.

**Input Placeholders**:
- [CODE_WITH_BUG]
- [EXPECTED_BEHAVIOR]
- [ACTUAL_BEHAVIOR]
- [LANGUAGE]

**Expected Output**:
1. Brief diagnosis.
2. Corrected code in a code block.
3. Explanation of the fix.
4. Relevant regression tests or test cases.
