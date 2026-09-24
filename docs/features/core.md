# Core Feature Guide

## Smart scan plan
**What it does:** Classifies consumer vs custom-domain email targets and explains selected categories.  
**Use:** `emailintel plan EMAIL`  
**Limitation:** It optimizes implemented providers only; it does not imply complete Internet coverage.

## Evidence ledger
**What it does:** Assigns IDs, normalized hashes, evidence families, provider/parser versions, confidence and freshness.  
**Use:** Created automatically by `emailintel scan`.  
**Limitation:** Hash integrity proves local record consistency, not that a remote website has not changed.

## Confidence explanation
**What it does:** Explains major factors behind a stored confidence value.  
**Use:** `emailintel explain SCAN_ID EVD_ID`  
**Limitation:** Confidence is evidence strength, not proof of a person's real-world identity.

## Timeline
**What it does:** Shows evidence in chronological observation/retrieval order.  
**Use:** `emailintel timeline SCAN_ID`  
**Limitation:** Providers without a public observation date use retrieval time.

## Diff
**What it does:** Compares two locally stored scans using normalized evidence hashes.  
**Use:** `emailintel diff SCAN_A SCAN_B`  
**Limitation:** A missing reference can mean a provider/source changed; it does not prove deliberate deletion.
