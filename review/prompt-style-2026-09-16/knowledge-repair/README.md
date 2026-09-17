# Repair Wikipedia Import

Prepared a faithful plain-text copy of Wikipedia’s List of experiments using revision 1371680817 from 2026-08-27T21:03:19Z. The import keeps the original Knowledge filename and includes source attribution, permanent revision link, license, and contributor-history link.

[Import file](https___en_wikipedia_org_wiki_list_of_experiments.txt) contains complete article text, all nine section headings, figure captions, and references. HTML-to-text conversion changes whitespace and layout only. Navigational templates, site controls, styles, and citation backlinks are omitted. A sequential check confirms that all retained article text appears without paraphrase or omission. Redundant rendered HTML, wikitext, and API copies were removed after verification. Their hashes and revision source are retained in provenance.

[Provenance](provenance.json) records retrieval time, revision identifiers, extraction details, and hashes. The prepared UTF-8 file is 18779 bytes, with SHA-256 `6bb8223134e2fedc6f4d33c83b36245c975679717f682812e4378c765591bbe5`.

The parent task repaired the existing Knowledge file in place through Firefox, saved it, closed it, and reopened it. Complete persisted text matched all 18,708 trimmed characters of the prepared import; the revision header remained and the rate-limit error was absent. This verifies saved text. Retrieval behavior is a separate test.

The source register and Advanced prompt now describe the repaired article as an overview for selecting experiments and checking relevant source passages. Other original sources are unchanged. [Source-register transfer page](source-register-import.html) contains the complete updated register. [Exact copy diff](repair-copy.diff) records both wording changes, with complete before-and-after files alongside it.

[Browser transfer page](import.html) contains the complete escaped import text. Its decoded text exactly matches the import file. Public source downloads used no authentication or cookies and contained no credential-pattern matches.
