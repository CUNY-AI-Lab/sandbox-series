**Name:** Bibliography Duplicate Reviewer
**Skill ID:** bibliography-duplicate-reviewer
**Description:** Identifies duplicate or near-duplicate entries in a bibliography by comparing author, title, and year.

**Skill Instructions:**
Review the provided bibliography for redundant entries.
1. Parse each entry to extract the author, title, and year.
2. Compare these three fields across all entries in the list.
3. Flag exact matches and highlight uncertain matches (e.g., similar titles or different years).
4. Present a list of flagged items without deleting or modifying any original text.
**Expected Output:** A list of flagged exact duplicates and uncertain matches.

**Ordinary Test**
**Input:** "Doe, A. (2020). Science." and "Doe, A. (2020). Science."
**Expected Behavior:** Flags both entries as an exact match.

**Boundary Test**
**Input:** "Doe, A. (2020). Science." and "Doe, A. (?). Science."
**Expected Behavior:** Flags as an uncertain match due to the missing year.
