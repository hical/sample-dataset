# Description of sampled test collection
The text collection in this repository is a sample of the Athome4 collection,
which was used in the TREC 2016 Total Recall Track [1]. The original dataset
contains 290,000 Jeb Bush emails and 34 topics. 

We provided 9 topics (`athome4.topics.sample`), 50000 sampled documents 
(`athome4_sample.tgz`), and sampled relevance judgments (`athome4.qrel.sample`) for this sampled test collection.

# Extract paragraphs for full documents
```bash
python3 process.py athome4_sample.tgz
```

[1] Grossman, Maura R., Gordon V. Cormack, and Adam Roegiest. "TREC 2016 Total Recall Track Overview." TREC. 2016.
