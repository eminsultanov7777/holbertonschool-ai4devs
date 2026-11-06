# Error Analysis Prompt Template

**Role**: Act as an experienced debugging engineer.

**Task**: Analyze the error message and related code. Explain the most likely cause, distinguish confirmed facts from hypotheses, and suggest a safe way to verify the diagnosis. Do not invent missing details.

**Input Placeholders**:
- [ERROR_MESSAGE_OR_STACK_TRACE]
- [RELEVANT_CODE]
- [LANGUAGE_AND_ENVIRONMENT]

**Expected Output**:
1. Plain-language explanation of the error.
2. Most likely cause(s), with reasoning.
3. Steps to reproduce or verify the issue.
4. Recommended fix, including code if appropriate.
