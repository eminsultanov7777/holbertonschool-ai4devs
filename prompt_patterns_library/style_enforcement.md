# Style Enforcement Prompt Template

**Role**: Act as a code reviewer enforcing a consistent team coding standard.

**Task**: Review and rewrite the supplied code to follow the given style guide, naming conventions, and formatting rules. Preserve functionality.

**Input Placeholders**:
- [CODE_BLOCK]
- [LANGUAGE]
- [STYLE_GUIDE_OR_RULES]

**Expected Output**:
1. Revised code in a code block.
2. A concise list of style changes.
3. Any rules that could not be applied and why.
