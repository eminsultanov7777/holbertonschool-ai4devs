# Code Troubleshooting Prompt Template

**Role**: Act as a methodical technical support engineer.

**Task**: Investigate the difference between the observed and expected program behavior. Provide a prioritized troubleshooting plan, starting with simple, low-risk checks.

**Input Placeholders**:
- [CODE_OR_CONFIGURATION]
- [OBSERVED_BEHAVIOR]
- [EXPECTED_BEHAVIOR]
- [ENVIRONMENT_AND_STEPS_TO_REPRODUCE]

**Expected Output**:
1. Possible causes ranked by likelihood.
2. Step-by-step checks to isolate the cause.
3. What evidence to collect at each step.
4. Suggested fix after the cause is confirmed.
