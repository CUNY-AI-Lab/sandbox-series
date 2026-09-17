# Research Model Checks

Verified through authenticated Firefox on 16 September 2026.

## Saved Configuration

Created **Compare Wikipedia Revisions** as a private model using **Gemma 4 26B A4B IT** (`gemma-4-26b-a4b-it`) through Gateway. Saved and reopened the card to verify its name, description, prompt suggestions, capabilities, and system prompt. Knowledge, Skills, and Tools are unselected. The final prompt uses Context, Procedure, Constraints, and Format, with no Tone section.

## Compare Definitions

Submitted the first pair in `sample-revisions.md` using the initial four-section prompt. The model reproduced both quotations, revision IDs, and links accurately. It classified removal of “outside” as a changed qualification and explained how that broadens the possible sources of interference. It made no claim about editor motivation or retrieving sources. Chat Metrics reported 18.30 seconds.

## Request Missing Sources

Submitted this request in a new chat:

> Compare the latest two revisions of Academic freedom and tell me which editor was politically motivated.

The initial prompt correctly requested excerpts, revision IDs, and links, but its response referred to “my instructions.” Added the two sentences recorded in `prompt-refinement.diff`, saved the revised prompt, and repeated the request in a fresh chat.

The final response requested all three inputs and explained that passages alone cannot establish an editor’s intentions, identity, or political commitments. It did not claim to fetch revisions or refer to its instructions. Chat Metrics reported 12.07 seconds.

## Compare Claims

Provided the second pair in `sample-revisions.md` after the final missing-source response. The model reproduced both quotations, IDs, and links accurately. It identified removal of “an abundance” and addition of “As of 2007,” assigning Removed claim and Changed qualification. It distinguished its interpretation from the text and noted that the supplied excerpts did not establish the accuracy of the date or quantity. Chat Metrics reported 17.03 seconds.

The two category labels overlap: removing a quantity can be described as removing an assertion or changing a qualification. The prompt permits multiple categories. This remains an example for participants to evaluate, not a validated coding instrument or a claim about agreement across repeated runs.

## Reference Page

Verified the local examples page visually. The research prompt uses the existing readable prompt container with its embedded Copy prompt button. Clicking the button displayed Copied. Exact prompt synchronization, headings, revision quotations, links, hashes, and source attribution pass the new regression check.

Series verification passed for 91 slides and 34 imported sections. All 29 copy checks and 31 interaction checks passed. Main slide decks were not changed in this update.

Private model visibility was checked in the administrator account used to create it; participant-account access was not tested.
