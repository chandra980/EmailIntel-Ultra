# EMAILINTEL ULTRA — EXTREME ADVANCED INTELLIGENCE UPGRADE

This specification EXTENDS the existing EmailIntel Ultra master specification.

Treat every requirement below as part of the final repository.

Do not remove existing functionality.

Project:

**EMAILINTEL ULTRA**

Owner / Maintainer:

**Chandra Kumar Yadav**

Primary design philosophy:

> Maximum legitimate public-source intelligence, minimum false positives, complete evidence provenance, reproducible investigations, understandable results, professional interface, and zero mandatory API/login configuration.

IMPORTANT:

“AGGRESSIVE” in this project means:

- aggressive coverage
- aggressive verification
- aggressive correlation
- aggressive performance optimization
- aggressive provider health testing
- aggressive false-positive elimination
- aggressive evidence enrichment
- aggressive public-source discovery

It must NEVER mean:

- authentication bypass
- CAPTCHA bypass
- password attacks
- credential acquisition
- unauthorized access
- private-data extraction
- rate-limit evasion
- proxy rotation for bypassing provider controls

============================================================
EXTREME PRODUCT OBJECTIVE
============================================================

Transform EmailIntel Ultra from an email-scanning CLI into a complete:

**Public Identity Intelligence + Evidence Analysis + Investigation Management Framework**

The architecture must support:

EMAIL
↓
PUBLIC REFERENCES
↓
IDENTIFIERS
↓
TIMELINE
↓
ENTITY CORRELATION
↓
SOURCE INDEPENDENCE ANALYSIS
↓
EVIDENCE VALIDATION
↓
CONTRADICTION ANALYSIS
↓
CONFIDENCE CALIBRATION
↓
INVESTIGATION GRAPH
↓
PROFESSIONAL REPORT

The application must remain understandable to beginners while exposing advanced analyst capabilities.

Create three interface levels:

1. SIMPLE
2. ANALYST
3. EXPERT

============================================================
FEATURE 1 — TARGET-AWARE INTELLIGENCE PLANNER
============================================================

Create a component named:

TargetIntelligencePlanner

Before scanning, analyze the target.

Example:

target@gmail.com

The planner determines:

Email Provider:
Gmail

Domain Intelligence Value:
LOW

Developer/Public Web Intelligence Value:
HIGH

Mail Infrastructure Investigation:
SKIP SHARED PROVIDER INFRASTRUCTURE

Corporate Intelligence:
NOT APPLICABLE

Then automatically create the most useful scan plan.

For:

employee@company.com

the plan should prioritize:

DNS
RDAP
organization
mail infrastructure
public repositories
documents
staff references
developer footprint

Usage:

emailintel scan target@example.com --smart

Output:

SCAN PLAN

Target Type: Corporate Email
Selected Providers: 73
Skipped as Irrelevant: 31

Priority:
1. Domain Infrastructure
2. Organization Intelligence
3. Developer References
4. Documents
5. Public Profiles

Explain WHY each provider group was selected.

============================================================
FEATURE 2 — SCAN PLAN EXPLAINABILITY
============================================================

Implement:

emailintel plan target@example.com

Display:

Target Classification
Selected Categories
Excluded Categories
Expected Provider Count
Estimated Network Request Budget
Historical Provider Reliability
Reasons for selection

Example:

Provider: PublicGitX
Selected: YES

Reason:
Exact-email searches are supported by this provider and historical reliability is 98%.

Provider: CorporateRDAP
Selected: NO

Reason:
Target uses gmail.com; organization-level RDAP would describe Google infrastructure rather than the individual.

============================================================
FEATURE 3 — ADAPTIVE REQUEST-BUDGET ENGINE
============================================================

Allow:

--max-time
--max-requests
--max-concurrency
--confidence-target

Examples:

emailintel scan EMAIL --max-time 60

emailintel scan EMAIL --max-requests 150

emailintel scan EMAIL --confidence-target high

The scheduler must determine which providers provide the highest expected intelligence value within the available budget.

Do not simply execute providers alphabetically.

Use:

provider reliability
average latency
historical yield
target compatibility
evidence quality
source independence

============================================================
FEATURE 4 — EVIDENCE PROVENANCE LEDGER
============================================================

Create:

EvidenceProvenanceLedger

Every finding receives:

Evidence ID
Scan ID
Target
Provider
Source URL
Retrieval timestamp
Parser version
Provider version
Normalized evidence hash
Confidence
Freshness
Validation status

Example:

Evidence ID:
EVD-93F7A11C

SHA-256:
...

Provider:
PublicGitProvider

Retrieved:
2026-09-24T13:50:41Z

Parser:
git-parser-3.1

This creates a forensic-quality evidence trail.

============================================================
FEATURE 5 — CONTENT-ADDRESSED EVIDENCE STORAGE
============================================================

Evidence should optionally be stored using content hashes.

Example:

evidence/
  sha256/
      9f/
        9f381....

Benefits:

duplicate evidence can be detected,
evidence changes can be identified,
reports can reference immutable local evidence identifiers.

Do not unnecessarily save complete remote pages.

Store only what is required to reproduce the finding where appropriate.

============================================================
FEATURE 6 — EVIDENCE INTEGRITY VERIFICATION
============================================================

Implement:

emailintel evidence verify SCAN_ID

Verify locally stored evidence hashes.

Output:

Evidence Records: 31
Valid: 31
Modified: 0
Missing: 0

This is integrity verification, NOT a claim that remote web content has remained unchanged.

============================================================
FEATURE 7 — SOURCE-INDEPENDENCE GRAPH
============================================================

Five websites repeating information copied from one upstream source must NOT count as five independent confirmations.

Create:

SourceIndependenceEngine

Model relationships:

Original Source
├── Mirror A
├── Aggregator B
├── Archive C
└── Search Index D

Confidence must distinguish:

5 references

from:

5 independent sources.

Example:

Raw References: 12
Independent Evidence Families: 3

Confidence calculations should use independent evidence families.

============================================================
FEATURE 8 — EVIDENCE FAMILY FINGERPRINTING
============================================================

Detect likely copied/derived content using:

normalized text fingerprints
URL relationships
canonical URLs
timestamps
shared metadata
document hashes
content similarity

Return:

Evidence Family ID:
FAM-42

Sources:
4

Likely Origin:
Public repository commit

Derived Copies:
3

Do not claim copying unless evidence supports it.

Use:

LIKELY_DERIVED
POSSIBLY_DERIVED
INDEPENDENT
UNKNOWN

============================================================
FEATURE 9 — TEMPORAL IDENTITY GRAPH
============================================================

Do not build only a static relationship graph.

Create a time-aware graph.

Example:

2018
Email → Repository A

2020
Email → Project B

2023
Email → Organization X

2025
Email → Public Document Y

Each relationship stores:

first observed
last observed
evidence timestamp
retrieval timestamp
freshness
historical/current status

============================================================
FEATURE 10 — EVIDENCE FRESHNESS ENGINE
============================================================

Confidence and freshness must be separate concepts.

Example:

Confidence:
VERIFIED

Freshness:
HISTORICAL

Observed:
2018

Another result:

Confidence:
HIGH

Freshness:
RECENT

Observed:
2026

Support:

CURRENT
RECENT
AGING
HISTORICAL
UNKNOWN

Never imply that historical evidence is current.

============================================================
FEATURE 11 — TEMPORAL DECAY MODEL
============================================================

Add optional temporal weighting.

For certain evidence categories, older evidence may be less useful for CURRENT identity correlation.

Do not delete historical evidence.

Instead display:

Evidence Strength:
HIGH

Current-Relevance:
LOW

Reason:
Last observed 8 years ago.

Document the temporal model.

============================================================
FEATURE 12 — CONTRADICTION DETECTION ENGINE
============================================================

Create:

ContradictionEngine

Identify conflicting public evidence.

Example:

Source A:
Organization = Example Corp

Source B:
Organization = Other Corp

Timeline:

Source A observed: 2019
Source B observed: 2025

Possible interpretation:

Employment/affiliation may have changed.

Do NOT automatically choose one result.

Show:

CONFLICT DETECTED

and provide supporting evidence.

============================================================
FEATURE 13 — UNCERTAINTY PROPAGATION
============================================================

If an upstream finding is uncertain, downstream correlations must not magically become certain.

Example:

Email → Username
confidence 0.55

Username → Profile
confidence 0.95

Do NOT calculate:

Profile belongs to email = 0.95

Confidence must propagate uncertainty.

Document the mathematical strategy.

============================================================
FEATURE 14 — EXPLAINABLE CONFIDENCE
============================================================

Implement:

emailintel explain EVIDENCE_ID

Example output:

CONFIDENCE EXPLANATION

Result:
Public repository association

Final Confidence:
0.91 HIGH

Supporting factors:

+ Exact normalized email match
+ Direct public source
+ Source parser passed validation
+ Independent confirmation

Reducing factors:

- Evidence is 4 years old
- Organization relationship not independently confirmed

No unexplained confidence numbers are allowed.

============================================================
FEATURE 15 — CONFIDENCE CALIBRATION LAB
============================================================

Create automated confidence testing using known positive/negative fixtures.

Command:

emailintel calibrate

Measure:

false positive rate
false negative rate
precision
recall
calibration error

Where sufficient labeled fixtures exist, optionally report:

Brier score

Do not claim statistical calibration without enough test data.

============================================================
FEATURE 16 — NEGATIVE-EVIDENCE MODEL
============================================================

Absence of a result must NOT automatically mean:

ACCOUNT DOES NOT EXIST.

Distinguish:

NOT_FOUND
NOT_INDEXED
SOURCE_UNAVAILABLE
SOURCE_BLOCKED
QUERY_INCONCLUSIVE
NEGATIVE_CONFIRMED

Document what constitutes a genuine negative result for every provider.

============================================================
FEATURE 17 — PROVIDER DRIFT SENTINEL
============================================================

Websites change constantly.

Create:

ProviderDriftSentinel

It should detect:

HTML structure changes
JSON schema changes
status-code changes
redirect-pattern changes
expected marker disappearance
parser mismatch

Provider should automatically transition from:

WORKING

to:

PARSER_DRIFT_SUSPECTED

when validation tests fail.

============================================================
FEATURE 18 — PROVIDER CANARY TESTS
============================================================

Each supported provider may define safe public canary fixtures.

Command:

emailintel provider-test ProviderName

or:

emailintel providers --self-test

Output:

Provider        Parser   Positive   Negative   Latency
Git-X           PASS     PASS       PASS       310ms
Docs-X          PASS     PASS       PASS       820ms
Profile-X       FAIL     UNKNOWN    PASS       1.2s

Do not rely on private accounts as canaries.

============================================================
FEATURE 19 — AUTOMATIC PROVIDER QUARANTINE
============================================================

When a provider begins generating abnormal results:

quarantine it temporarily.

States:

HEALTHY
DEGRADED
DRIFT_SUSPECTED
QUARANTINED
RECOVERING

Example:

Provider quarantined because positive-response ratio suddenly changed from 4% to 97%.

This may indicate parser failure.

============================================================
FEATURE 20 — PROVIDER BEHAVIOR BASELINE
============================================================

Maintain historical statistics:

normal response size
normal latency
normal redirect count
positive-result ratio
common HTTP status
parser signature

Use anomaly detection to identify provider breakage.

Do not treat behavior anomaly as malicious activity.

============================================================
FEATURE 21 — REPRODUCIBILITY CAPSULE
============================================================

Every investigation should be exportable as:

SCAN CAPSULE

Containing:

tool version
Python version
OS
scan configuration
provider versions
provider statuses
target hash
timestamps
scan plan
evidence metadata
result schema version
dependency lock fingerprint

Command:

emailintel capsule create SCAN_ID

Output:

EI-XXXX.capsule.zip

The capsule must avoid storing credential material.

============================================================
FEATURE 22 — OFFLINE REPLAY
============================================================

Implement:

emailintel replay SCAN_ID

Replay previously stored normalized evidence without contacting remote providers.

Allow:

report regeneration
confidence recalculation
new report template
graph generation
timeline generation
deduplication rerun

Clearly mark replayed results as:

OFFLINE_REPLAY

============================================================
FEATURE 23 — SCAN DIFF ENGINE
============================================================

Implement:

emailintel diff SCAN_A SCAN_B

and:

emailintel scan EMAIL --compare-last

Output sections:

NEW FINDINGS
REMOVED REFERENCES
CHANGED EVIDENCE
CONFIDENCE CHANGES
PROVIDER CHANGES
INFRASTRUCTURE CHANGES

Example:

NEW
+ Public repository reference

CHANGED
~ Organization evidence changed

MISSING
- Previous profile URL now returns 404

Do not interpret disappearance as deletion by the target unless evidence establishes that.

============================================================
FEATURE 24 — HISTORICAL SNAPSHOT MODE
============================================================

Allow reports to answer:

“What was publicly observable at scan time?”

Preserve:

scan timestamp
source URL
evidence fingerprint
provider version
normalized extracted fields

This makes scans comparable.

============================================================
FEATURE 25 — INVESTIGATION CASE MANAGEMENT
============================================================

Implement:

emailintel case create CASE-001

emailintel case add CASE-001 target@example.com

emailintel case scan CASE-001

emailintel case report CASE-001

Structure:

cases/
  CASE-001/
      case.json
      targets/
      scans/
      evidence/
      reports/
      timeline/

Allow case title and analyst notes.

Do not require external databases.

============================================================
FEATURE 26 — INVESTIGATION NOTES
============================================================

Allow:

emailintel note CASE-001 "Public repository reference manually reviewed."

Notes require:

author field
timestamp
optional evidence reference

Do not silently mix analyst notes with automated findings.

Label them:

ANALYST_NOTE

============================================================
FEATURE 27 — EVIDENCE REVIEW WORKFLOW
============================================================

Every finding can have:

UNREVIEWED
REVIEWED
CONFIRMED_BY_ANALYST
REJECTED_BY_ANALYST

Automated confidence and analyst disposition must remain separate fields.

============================================================
FEATURE 28 — PUBLIC-IDENTIFIER PIVOT ENGINE
============================================================

When a legitimate public result exposes another identifier such as:

public username
public website
public organization
public repository

allow controlled pivoting.

Example:

emailintel pivot EVD-123

The application must show:

Pivot source
Original evidence
New identifier
Confidence
Reason

Never pivot from private/restricted data.

============================================================
FEATURE 29 — PIVOT DEPTH CONTROL
============================================================

Support:

--pivot-depth 0
--pivot-depth 1
--pivot-depth 2

Default:

0 or conservative value.

Prevent uncontrolled recursive expansion.

============================================================
FEATURE 30 — INVESTIGATION PATH VISUALIZER
============================================================

Show exactly how a finding was reached.

Example:

Email
  ↓ exact public commit match
Username
  ↓ public project profile
Repository
  ↓ organization metadata
Organization

Every edge shows:

provider
timestamp
confidence
evidence ID

============================================================
FEATURE 31 — ADVANCED GRAPH ENGINE
============================================================

Build an interactive local graph containing:

Email
Domain
Username
Profile
Repository
Package
Organization
Document
Archive
IP
ASN
Mail Provider
Website

Support:

search
filter
zoom
category toggles
confidence filters
time filters
source filters

Export:

JSON
GraphML
SVG where practical

Do not require Neo4j or external services.

============================================================
FEATURE 32 — TIME-LAPSE GRAPH
============================================================

Optional advanced visualization:

move a time slider and view which relationships were observable at different times.

Example:

2018 → 2020 → 2022 → 2026

Historical evidence must be visually distinct from recent evidence.

============================================================
FEATURE 33 — EVIDENCE TIMELINE
============================================================

Create:

emailintel timeline SCAN_ID

Example:

2017-04
Public mailing-list reference

2019-09
Git commit

2022-01
Package metadata

2025-08
Public document

2026-09
Current public profile

Support HTML timeline visualization.

============================================================
FEATURE 34 — INVESTIGATION SUMMARY ENGINE
============================================================

Do not require cloud AI.

Implement deterministic rule-based summarization first.

Example:

PUBLIC FOOTPRINT SUMMARY

The target produced 17 validated public references across 6 independent evidence families.

Strongest categories:
Developer repositories
Public documents
Package metadata

Historical references:
8

Recent references:
9

Contradictions:
1

Exposure metadata:
No verified result

Do not invent conclusions.

============================================================
FEATURE 35 — LOCAL OPTIONAL AI MODE
============================================================

If implemented, AI must be OPTIONAL.

The project must work fully without AI.

Support local models only as an optional extension where practical.

Example:

emailintel summarize SCAN_ID --local-model

Never send target information to external AI services by default.

============================================================
FEATURE 36 — PRIVACY-PRESERVING REPORT GENERATOR
============================================================

Support:

--report-full
--report-redacted
--report-public

PUBLIC report may automatically suppress:

local paths
internal notes
unnecessary target details
raw provider diagnostics

Redacted reports must visibly state:

REDACTED REPORT

============================================================
FEATURE 37 — EPHEMERAL INVESTIGATION MODE
============================================================

Implement:

emailintel scan EMAIL --ephemeral

Behavior:

no persistent history
no persistent cache
no SQLite target storage
temporary files cleaned after report generation
optional report suppression

Example:

emailintel scan target@example.com --deep --ephemeral

============================================================
FEATURE 38 — ENCRYPTED LOCAL CASE VAULT
============================================================

Optional local-only case encryption.

No cloud account.

No server.

No login service.

Support encryption of saved investigation cases using a user-supplied local passphrase.

Do not invent custom cryptography.

Use established audited libraries.

Keep this OPTIONAL.

============================================================
FEATURE 39 — DATA RETENTION CONTROLS
============================================================

Implement:

emailintel retention show

emailintel retention set --days 30

emailintel purge --older-than 90d

Support:

keep indefinitely
X days
ephemeral

Never silently delete analyst-marked evidence unless explicitly configured.

============================================================
FEATURE 40 — SOURCE DISCLOSURE LEVEL
============================================================

Every report should show:

AUTOMATED QUERY
PUBLIC REFERENCE
HISTORICAL ARCHIVE
LOCAL ANALYSIS
MANUAL REVIEW

This allows the reader to understand how information was obtained.

============================================================
FEATURE 41 — ADVANCED MAIL SECURITY POSTURE
============================================================

For custom domains analyze:

SPF
DMARC
DKIM indicators
MTA-STS
TLS-RPT
DNSSEC
CAA
BIMI where publicly discoverable
MX redundancy
mail-provider fingerprint
SPF include depth
SPF lookup-count risk
DMARC enforcement mode

Example:

MAIL SECURITY

SPF:
PRESENT

DMARC:
p=reject

MTA-STS:
PRESENT

TLS-RPT:
PRESENT

DNSSEC:
ENABLED

This is infrastructure analysis, not a vulnerability exploit.

============================================================
FEATURE 42 — MAIL-ROUTING VISUALIZATION
============================================================

Visualize:

Domain
↓
MX
↓
Mail Provider
↓
IP
↓
ASN

Provide evidence URLs/data sources.

============================================================
FEATURE 43 — PUBLIC PGP / OPENPGP INTELLIGENCE
============================================================

Where publicly available, search legitimate public-key metadata.

Return:

Public Key Found
UID
Email
Fingerprint
Creation Date
Expiration
Source

Do not use discovered keys for impersonation or unauthorized access.

============================================================
FEATURE 44 — EMAIL PROVIDER BEHAVIOR PROFILE
============================================================

Maintain a provider knowledge base for:

Gmail
Googlemail
Outlook
Hotmail
Yahoo
Proton
iCloud
common corporate mail providers

Knowledge should include only technical/public characteristics useful for deciding scan strategy.

No private login probing.

============================================================
FEATURE 45 — DOMAIN RELATIONSHIP INTELLIGENCE
============================================================

For corporate domains discover legitimate public relationships such as:

parent domain
subdomains when directly relevant/public
MX provider
DNS provider
ASN
CDN
public repositories
organization references

Avoid broad intrusive infrastructure scanning.

============================================================
FEATURE 46 — SOURCE COVERAGE MATRIX
============================================================

Implement:

emailintel coverage

Output:

Category          Catalog  Working  Limited  Unavailable
DNS               12       12       0        0
Developer         34       28       4        2
Documents         21       13       5        3
Archives          11       8        1        2
Profiles          42       29       8        5

Generate this automatically for README.

============================================================
FEATURE 47 — PROVIDER BENCHMARK DASHBOARD
============================================================

Implement:

emailintel benchmark

Output:

Provider
Median latency
P95 latency
Success rate
Timeout rate
Recent health
Yield rate

Historical performance should drive scan ordering.

============================================================
FEATURE 48 — WHY-SKIPPED
============================================================

Implement:

emailintel why-skipped ProviderName

Example:

Provider:
ExampleX

Status:
UNSUPPORTED_NO_AUTH

Reason:
Anonymous access unavailable.

Last Verified:
2026-09-20

Required User Action:
None

Behavior:
Provider excluded automatically.

============================================================
FEATURE 49 — WHY-NOT-FOUND
============================================================

Implement:

emailintel explain-negative EVIDENCE_OR_PROVIDER

Explain whether:

provider genuinely returned negative
provider could not verify
target type unsupported
rate limited
parser failed
source unavailable

This prevents users from misreading missing data.

============================================================
FEATURE 50 — DECLARATIVE SCAN RECIPES
============================================================

Support safe configuration files such as:

recipes/developer.yaml
recipes/corporate.yaml
recipes/quick.yaml
recipes/deep.yaml

Example concepts:

categories
maximum time
concurrency
provider tags
pivot depth
report format

Do NOT allow arbitrary code execution from recipe files.

Usage:

emailintel scan EMAIL --recipe developer

============================================================
FEATURE 51 — CUSTOM SAFE RECIPE BUILDER
============================================================

Implement:

emailintel recipe create

Interactive wizard:

Choose categories
Choose time budget
Choose report types
Choose pivot depth
Choose privacy mode

Save:

my-recipe.yaml

============================================================
FEATURE 52 — PROVIDER MANIFEST SIGNING
============================================================

Maintain provider metadata manifest.

Where release signing infrastructure is available:

sign provider manifests.

At minimum support:

manifest checksum verification.

Detect accidental/tampered provider database changes.

============================================================
FEATURE 53 — SOURCE DATABASE VERSIONING
============================================================

Display:

Provider DB Version
Provider Count
Last Update
Manifest Hash

Command:

emailintel provider-db info

============================================================
FEATURE 54 — PROVIDER DATABASE ROLLBACK
============================================================

If provider update causes failures:

allow:

emailintel provider-db rollback

Keep a small number of recent known-good provider manifests.

============================================================
FEATURE 55 — PARSER VERSIONING
============================================================

Every evidence record identifies the parser version used.

This allows future investigations to understand why an older scan produced a different result.

============================================================
FEATURE 56 — SCHEMA MIGRATION SYSTEM
============================================================

Version:

database schema
report schema
provider metadata schema
scan-capsule schema

Implement migrations.

Never silently discard evidence during migration.

============================================================
FEATURE 57 — DETERMINISTIC REPORT GENERATION
============================================================

Given the same normalized evidence and report version, report generation should be as deterministic as practical.

Sort results consistently.

Use stable IDs.

Separate dynamic retrieval timestamps from content.

============================================================
FEATURE 58 — PROFESSIONAL THREE-LEVEL INTERFACE
============================================================

Build three user experiences.

------------------------------------------------------------
SIMPLE MODE
------------------------------------------------------------

For beginners.

Command:

emailintel

or:

emailintel scan EMAIL

Show only:

Target
Progress
Important Findings
Confidence
Summary
Report Location

Avoid overwhelming technical logs.

------------------------------------------------------------
ANALYST MODE
------------------------------------------------------------

Command:

emailintel scan EMAIL --analyst

Show:

provider categories
evidence IDs
confidence explanations
timeline
correlations
contradictions
source independence
provider health

------------------------------------------------------------
EXPERT MODE
------------------------------------------------------------

Command:

emailintel scan EMAIL --expert

Show:

request timing
parser versions
provider states
retry counts
rate limits
evidence fingerprints
scheduler decisions
network diagnostics

============================================================
FEATURE 59 — FULL-SCREEN PROFESSIONAL TUI
============================================================

Create an optional local terminal dashboard.

Command:

emailintel tui

Suggested layout:

┌─────────────────────────────────────────────────────────────┐
│ EMAILINTEL ULTRA                                            │
│ Investigation: EI-20260924-F3A91C                          │
├──────────────┬──────────────────────────────────────────────┤
│ Navigation   │ Overview                                     │
│              │                                              │
│ Overview     │ Target: target@example.com                  │
│ Findings     │ Mode: Deep                                  │
│ Timeline     │ Progress: ████████████░░░ 78%               │
│ Graph        │                                              │
│ Sources      │ Verified: 18   High: 11   Possible: 4       │
│ Providers    │                                              │
│ Errors       │ Independent Evidence Families: 9             │
│ Reports      │ Contradictions: 1                            │
└──────────────┴──────────────────────────────────────────────┘

Support keyboard navigation.

Do not require mouse interaction.

============================================================
FEATURE 60 — PROFESSIONAL LOCAL WEB DASHBOARD
============================================================

Implement optional:

emailintel dashboard

Bind by default ONLY to:

127.0.0.1

Do not expose publicly by default.

Pages:

Overview
New Scan
Cases
Findings
Evidence
Timeline
Graph
Providers
Provider Health
Benchmarks
Reports
Settings
Doctor
About

No external cloud backend.

============================================================
FEATURE 61 — DASHBOARD DESIGN SYSTEM
============================================================

Use a premium professional visual hierarchy.

Include:

dark mode
light mode
responsive layout
accessible contrast
clear typography
keyboard navigation
tooltips
status badges
filter chips
search
sortable tables

Avoid flashy hacker clichés.

Do NOT make the interface look like a movie hacking terminal.

It must look like a serious professional investigation product.

============================================================
FEATURE 62 — BEGINNER EXPLANATIONS
============================================================

Every technical item should have a plain-language explanation.

Example:

MX Records

Technical:
Mail exchange servers responsible for receiving email for this domain.

Simple:
Shows which service handles email for this domain.

Provide a:

?

help icon in the web dashboard.

============================================================
FEATURE 63 — “WHAT DOES THIS MEAN?” PANEL
============================================================

For every major finding, provide:

WHAT WAS FOUND
WHY IT MATTERS
HOW RELIABLE IT IS
WHERE IT CAME FROM
WHEN IT WAS OBSERVED
WHAT IT DOES NOT PROVE

Example:

WHAT IT DOES NOT PROVE:

“This historical public Git commit does not prove that the person currently uses this organization.”

============================================================
FEATURE 64 — FINDING DETAIL DRAWER
============================================================

Clicking a finding in the dashboard should open:

Finding
Confidence
Freshness
Source
Evidence
Independent confirmations
Contradictions
Timeline
Provider
Parser
Retrieved time
Evidence ID
Direct URL

============================================================
FEATURE 65 — ADVANCED FILTER ENGINE
============================================================

Allow filtering by:

confidence
freshness
category
provider
date
evidence family
review status
finding status
historical/current
source type

CLI examples:

emailintel findings SCAN_ID --confidence high

emailintel findings SCAN_ID --after 2025-01-01

============================================================
FEATURE 66 — GLOBAL INVESTIGATION SEARCH
============================================================

Search local stored cases:

emailintel search-local "Example Corp"

Search:

findings
notes
organizations
domains
repositories
documents

This is local database search only.

============================================================
FEATURE 67 — PROFESSIONAL REPORT LEVELS
============================================================

Generate:

Executive Report
Analyst Report
Technical Report
Raw Machine Report

EXECUTIVE:

short
clear
high-confidence results only

ANALYST:

evidence
timeline
graph
confidence explanations

TECHNICAL:

providers
parsers
latencies
diagnostics
hashes

RAW:

structured JSON/NDJSON

============================================================
FEATURE 68 — EXECUTIVE SUMMARY
============================================================

Top report section:

TARGET
SCAN DATE
SCAN MODE
PUBLIC FOOTPRINT LEVEL
VERIFIED FINDINGS
INDEPENDENT EVIDENCE FAMILIES
RECENT FINDINGS
HISTORICAL FINDINGS
CONTRADICTIONS
EXPOSURE METADATA
PROVIDER COVERAGE

Avoid sensational risk labels.

============================================================
FEATURE 69 — REPORT EVIDENCE TABLE
============================================================

Columns:

Evidence ID
Finding
Category
Confidence
Freshness
Independent?
Source
Observed
Reviewed
Link

Make tables:

sortable
filterable
searchable

============================================================
FEATURE 70 — REPORT TIMELINE
============================================================

Interactive HTML timeline.

Users should be able to filter by:

category
confidence
source
date range

============================================================
FEATURE 71 — REPORT GRAPH
============================================================

Interactive graph embedded in HTML.

Clicking nodes should reveal evidence.

No external Internet connection should be required to view an exported report when practical.

Bundle required frontend assets locally.

============================================================
FEATURE 72 — REPORT LIMITATION SECTION
============================================================

Automatically list:

unavailable providers
rate-limited providers
unverified providers
sources requiring authentication
network errors
historical evidence caveats
confidence limitations

This section is mandatory.

============================================================
FEATURE 73 — PROFESSIONAL ERROR UX
============================================================

Do NOT show beginners:

Traceback...

Instead show:

Provider X could not be queried.

Reason:
Remote service timed out.

Impact:
Other providers continued normally.

Advanced details:
Press [D]

Store technical traceback in debug logs.

============================================================
FEATURE 74 — GUIDED CLI
============================================================

Implement:

emailintel guided

Workflow:

1. Enter email
2. Select scan depth
3. Select privacy mode
4. Select report type
5. Start scan

Explain choices in one sentence.

============================================================
FEATURE 75 — INTERACTIVE TOUR
============================================================

Implement:

emailintel tour

Explain:

Scan
Providers
Findings
Evidence
Confidence
Timeline
Graph
Reports
Doctor
Repair

This helps first-time users.

============================================================
FEATURE 76 — FEATURE HELP SYSTEM
============================================================

Implement:

emailintel feature confidence

emailintel feature timeline

emailintel feature provider-health

Output:

WHAT IT DOES
WHEN TO USE IT
COMMAND
OUTPUT
LIMITATIONS

============================================================
FEATURE 77 — AUTO-GENERATED FEATURE DOCUMENTATION
============================================================

The repository must include:

docs/features/

Every implemented feature requires:

Purpose
How it works
Command
Example
Output
Limitations
Security/privacy notes

Generate README feature tables from this metadata where possible.

============================================================
FEATURE 78 — FEATURE MATRIX IN README
============================================================

Create:

| Feature | Purpose | Command | Status |
|---|---|---|---|
| Smart Scan Planner | Select useful providers | emailintel plan EMAIL | Working |
| Timeline | Historical view | emailintel timeline ID | Working |
| Evidence Explain | Explain confidence | emailintel explain ID | Working |
| Diff | Compare scans | emailintel diff A B | Working |

Never list roadmap features as Working.

============================================================
FEATURE 79 — COMMAND CHEAT SHEET
============================================================

README:

QUICK SCAN

emailintel scan EMAIL --fast

FULL PUBLIC SCAN

emailintel scan EMAIL --deep

PLAN ONLY

emailintel plan EMAIL

GRAPH

emailintel graph SCAN_ID

TIMELINE

emailintel timeline SCAN_ID

EXPLAIN FINDING

emailintel explain EVD-ID
COMPARE SCANS

emailintel diff SCAN1 SCAN2

DIAGNOSTICS

emailintel doctor

============================================================
FEATURE 80 — FIRST-RUN USER EXPERIENCE
============================================================

First successful installation should show:

EMAILINTEL ULTRA READY

Quick Start:

emailintel scan someone@example.com

Need help?

emailintel guided
emailintel tour

Advanced:

emailintel --help

Do not force a configuration wizard.

============================================================
FEATURE 81 — SMART DEFAULTS
============================================================

A beginner should not need to understand:

concurrency
timeouts
provider tags
cache TTL
confidence weights

Provide safe defaults.

Experts may override them.

============================================================
FEATURE 82 — REPORT OPENING
============================================================

After successful report generation:

Report created:

reports/EI-XXXX/report.html

Where safely supported provide:

emailintel report open EI-XXXX

Use the system default browser.

============================================================
FEATURE 83 — MACHINE-READABLE EXIT CODES
============================================================

Define documented exit codes.

Example:

0 success
1 invalid target
2 partial scan
3 network unavailable
4 installation problem
5 report failure
6 database problem

Do not use exit code 0 when a critical operation failed.

============================================================
FEATURE 84 — NDJSON STREAM OUTPUT
============================================================

For automation:

emailintel scan EMAIL --stream-json

Output one normalized event per line.

Useful for:

SIEM ingestion
shell pipelines
data processing

No external service required.

============================================================
FEATURE 85 — STANDARD EXPORT FORMATS
============================================================

Support where appropriate:

JSON
NDJSON
CSV
TXT
HTML
GraphML
Markdown

Optionally evaluate:

STIX 2.1 export

but implement it only if the mapping is semantically correct.

============================================================
FEATURE 86 — SOURCE TRANSPARENCY SCORECARD
============================================================

Do not score PEOPLE.

Instead score source transparency.

Example:

Provider Documentation:
PASS

Anonymous Access:
PASS

Validation Fixture:
PASS

Parser Tests:
PASS

Last Verified:
2026-09-20

This scorecard describes provider quality, not the target.

============================================================
FEATURE 87 — REPOSITORY QUALITY DASHBOARD
============================================================

README badges should cover:

Tests
Python Versions
Windows
Linux
Package Build
License
Provider Database Version

Avoid meaningless decorative badges.

============================================================
FEATURE 88 — REPRODUCIBLE RELEASES
============================================================

Where practical produce:

source archive
wheel
Windows standalone build
Linux standalone build
SHA256SUMS
SBOM

Document exactly which builds were actually produced.

============================================================
FEATURE 89 — SBOM
============================================================

Generate Software Bill of Materials using a standard such as:

CycloneDX

or:

SPDX

Include:

dependency
version
license
package source

============================================================
FEATURE 90 — RELEASE INTEGRITY
============================================================

Publish checksums for release artifacts.

Installer should verify known release artifacts when the installation flow supports it.

============================================================
FEATURE 91 — DEPENDENCY SECURITY CHECKS
============================================================

CI should check:

known dependency vulnerabilities
accidental secrets
static-analysis findings
package integrity

Do not automatically suppress warnings.

============================================================
FEATURE 92 — PROVIDER LICENSE INVENTORY
============================================================

Every integrated external open-source project/library must list:

Name
Version
License
Source
Integration Method

Create:

THIRD_PARTY_NOTICES.md

============================================================
FEATURE 93 — SNAPSHOT TESTING
============================================================

Reports and normalized schemas should have snapshot tests.

Unexpected output-schema changes must be detected during CI.

============================================================
FEATURE 94 — FUZZ TESTING
============================================================

Where practical fuzz:

email parser
URL parser
provider parser
HTML sanitizer
JSON normalization

Test malformed remote responses.

============================================================
FEATURE 95 — CHAOS / FAILURE TEST MODE
============================================================

Development-only:

emailintel dev chaos-test

Simulate:

timeouts
DNS failures
HTTP 429
broken JSON
HTML layout changes
database lock
cache corruption
provider exception

Validate graceful degradation.

============================================================
FEATURE 96 — PERFORMANCE REGRESSION TESTING
============================================================

Track benchmark history.

Flag significant regressions such as:

startup time
memory
provider throughput
report-generation time

Do not fail releases solely on tiny noisy differences.

============================================================
FEATURE 97 — QUERY TRACE
============================================================

Expert mode may generate:

emailintel trace SCAN_ID

Show:

scheduler decision
provider start
provider finish
retry
timeout
validation
normalization
deduplication

Do not expose sensitive raw content unnecessarily.

============================================================
FEATURE 98 — PROVIDER VALUE METRICS
============================================================

Measure:

successful query rate
unique finding yield
duplicate finding rate
latency
confidence contribution

Use this information to optimize future scan order.

Do not automatically disable low-yield providers solely because a target produced no finding.

============================================================
FEATURE 99 — EVIDENCE REDUNDANCY ANALYSIS
============================================================

Report:

Total Findings: 40
Unique Evidence: 17
Independent Families: 9
Duplicates/Mirrors: 23

This makes the report much more honest.

============================================================
FEATURE 100 — INVESTIGATION COMPLETENESS VIEW
============================================================

Do NOT claim:

“100% complete Internet scan.”

Instead show category coverage:

Email Validation        COMPLETE
DNS                     COMPLETE
Public Git              STRONG
Documents               PARTIAL
Archives                PARTIAL
Profiles                PARTIAL
Breach Metadata         LIMITED

Explain why each category has its state.

============================================================
PROFESSIONAL OUTPUT REQUIREMENT
============================================================

Every final scan should produce something similar to:

╭──────────────────────────────────────────────────────────────╮
│                      EMAILINTEL ULTRA                        │
│          Public Identity Intelligence Framework              │
│                 Chandra Kumar Yadav                         │
╰──────────────────────────────────────────────────────────────╯

INVESTIGATION

Target               target@example.com
Scan ID              EI-20260924-F3A91C
Mode                 SMART-DEEP
Started              2026-09-24 13:50 UTC

PROGRESS

Providers Eligible   84
Completed            67
Running               8
Skipped                9

███████████████████████░░░░ 79%

INTELLIGENCE

Verified Findings        14
High Confidence           9
Possible                  3

Independent Families      8
Historical Findings       6
Recent Findings           9
Contradictions            1

CATEGORY COVERAGE

Validation          COMPLETE
DNS                 COMPLETE
Developer           STRONG
Documents           PARTIAL
Archives            PARTIAL
Profiles            STRONG
Exposure            LIMITED

TOP FINDINGS

[VERIFIED] Public repository association
Evidence: EVD-81A3
Freshness: RECENT
Source: Direct Public Source

[HIGH] Public document reference
Evidence: EVD-22C1
Freshness: HISTORICAL
Independent Confirmations: 2

LIMITATIONS

3 providers rate limited
2 providers unavailable
1 provider parser drift suspected

REPORTS

Executive:
reports/.../executive.html

Analyst:
reports/.../analyst.html

Technical:
reports/.../technical.html

Machine:
reports/.../report.json

============================================================
PROFESSIONAL HTML DASHBOARD
============================================================

Top navigation:

Overview
Findings
Timeline
Graph
Infrastructure
Providers
Evidence
Reports

OVERVIEW:

Target
Scan Status
Coverage
Findings
Evidence Families
Confidence
Freshness
Limitations

FINDINGS:

searchable/sortable table

TIMELINE:

interactive chronological view

GRAPH:

interactive relationship graph

PROVIDERS:

provider status + health

EVIDENCE:

full evidence ledger

REPORTS:

download/export options

============================================================
README — FEATURE EXPLANATIONS
============================================================

For EVERY significant feature include:

### Feature Name

**What it does**

Explain in simple language.

**Why it exists**

Explain the problem solved.

**How to use**

Show exact CLI command.

**Example**

Show sample output.

**When to use**

Explain practical scenario.

**Limitations**

Explain what it cannot prove/do.

Example:

### Evidence Explain

What it does:

Shows exactly why a finding received its confidence level.

How to use:

emailintel explain EVD-93F7A11C

When to use:

Use this when you want to understand whether a finding is supported by direct or indirect evidence.

Limitations:

Confidence is evidence-based but does not prove a person's real-world identity.

============================================================
README — BEGINNER QUICK START
============================================================

Provide a section:

IF YOU ARE NEW, START HERE

1. Install EmailIntel Ultra.

2. Run:

emailintel scan example@example.com

3. Wait for the scan to finish.

4. Look at:

Verified Findings
High Confidence Findings
Limitations

5. Open:

report.html

6. Click any evidence URL to inspect the public source.

============================================================
README — ADVANCED WORKFLOW
============================================================

Example:

emailintel plan EMAIL

emailintel scan EMAIL --deep --analyst

emailintel timeline SCAN_ID

emailintel graph SCAN_ID

emailintel explain EVD-ID

emailintel diff OLD_SCAN NEW_SCAN

emailintel capsule create SCAN_ID

============================================================
REPOSITORY DOCUMENTATION STRUCTURE
============================================================

Create:

docs/
├── getting-started.md
├── installation.md
├── windows.md
├── linux.md
├── kali.md
├── architecture.md
├── privacy.md
├── responsible-use.md
│
├── features/
│   ├── smart-planner.md
│   ├── evidence-ledger.md
│   ├── confidence.md
│   ├── freshness.md
│   ├── contradictions.md
│   ├── timeline.md
│   ├── graph.md
│   ├── diff.md
│   ├── cases.md
│   ├── replay.md
│   ├── capsule.md
│   └── provider-health.md
│
├── providers/
│   ├── overview.md
│   ├── status-model.md
│   └── provider-development.md
│
├── reports/
│   ├── executive.md
│   ├── analyst.md
│   └── technical.md
│
└── troubleshooting/
    ├── installation.md
    ├── network.md
    ├── providers.md
    └── repair.md

============================================================
FEATURE STATUS POLICY
============================================================

Each feature must be labeled:

IMPLEMENTED
EXPERIMENTAL
ROADMAP
UNAVAILABLE

Do not mix them.

README must generate separate sections:

AVAILABLE NOW

EXPERIMENTAL

ROADMAP

============================================================
ADVANCED ACCEPTANCE TESTS
============================================================

Add tests for:

Target-aware planning
Evidence provenance
Evidence hashes
Source independence
Temporal graph
Freshness calculations
Temporal decay
Contradiction detection
Uncertainty propagation
Confidence explanation
Negative evidence
Provider drift
Provider quarantine
Offline replay
Scan diff
Case management
Pivot depth
Graph export
Timeline
Ephemeral mode
Report redaction
Mail-security analysis
Provider coverage
Provider benchmark
Recipes
Provider database rollback
Schema migrations
NDJSON streaming
SBOM generation
Report sanitization
Snapshot tests
Failure simulation

============================================================
FINAL FEATURE VERIFICATION
============================================================

Produce:

| Advanced Feature | Status | Test Evidence |
|---|---|---|
| Smart Planner | PASS/FAIL/NOT TESTED | ... |
| Evidence Ledger | PASS/FAIL/NOT TESTED | ... |
| Source Independence | PASS/FAIL/NOT TESTED | ... |
| Temporal Graph | PASS/FAIL/NOT TESTED | ... |
| Freshness Engine | PASS/FAIL/NOT TESTED | ... |
| Contradiction Engine | PASS/FAIL/NOT TESTED | ... |
| Explainable Confidence | PASS/FAIL/NOT TESTED | ... |
| Drift Detection | PASS/FAIL/NOT TESTED | ... |
| Replay | PASS/FAIL/NOT TESTED | ... |
| Diff Engine | PASS/FAIL/NOT TESTED | ... |
| Cases | PASS/FAIL/NOT TESTED | ... |
| Timeline | PASS/FAIL/NOT TESTED | ... |
| Graph | PASS/FAIL/NOT TESTED | ... |
| Professional TUI | PASS/FAIL/NOT TESTED | ... |
| Local Dashboard | PASS/FAIL/NOT TESTED | ... |
| Executive Report | PASS/FAIL/NOT TESTED | ... |
| Analyst Report | PASS/FAIL/NOT TESTED | ... |
| Technical Report | PASS/FAIL/NOT TESTED | ... |
| Coverage Matrix | PASS/FAIL/NOT TESTED | ... |
| Provider Benchmark | PASS/FAIL/NOT TESTED | ... |
| SBOM | PASS/FAIL/NOT TESTED | ... |

Never mark PASS without test evidence.

============================================================
IMPLEMENTATION PRIORITY
============================================================

Do not attempt to implement every advanced feature badly at once.

Priority 1:

Core scanner
Evidence model
Provider framework
Professional CLI
Reporting

Priority 2:

Smart Planner
Explainable confidence
Freshness
Evidence provenance
Source independence
Contradiction detection

Priority 3:

Timeline
Graph
Diff
Case management
Replay

Priority 4:

Professional TUI
Local Dashboard
Executive/Analyst/Technical reports

Priority 5:

Provider drift
Provider quarantine
Benchmarking
Reproducibility capsule
SBOM
Advanced QA

============================================================
FINAL QUALITY PRINCIPLE
============================================================

EmailIntel Ultra must NOT compete by making the largest unsupported provider-count claim.

It should compete by producing:

BETTER EVIDENCE
BETTER VERIFICATION
BETTER EXPLAINABILITY
BETTER TEMPORAL CONTEXT
BETTER SOURCE TRANSPARENCY
BETTER FALSE-POSITIVE CONTROL
BETTER REPRODUCIBILITY
BETTER USER EXPERIENCE
BETTER PROFESSIONAL REPORTS

A result should never simply say:

ACCOUNT FOUND

Instead it should explain:

WHAT WAS FOUND
WHERE IT WAS FOUND
WHEN IT WAS OBSERVED
WHY IT MATCHES
HOW STRONG THE EVIDENCE IS
HOW FRESH THE EVIDENCE IS
WHETHER SOURCES ARE INDEPENDENT
WHAT CONTRADICTS IT
WHAT IT DOES NOT PROVE

============================================================
FINAL REPOSITORY EXPECTATION
============================================================

The repository must include documentation explaining every implemented feature.

For each user-facing command include:

command
purpose
example
output
limitations

A beginner should be able to install the tool, enter an email, understand the terminal output, open the HTML report, understand each finding, and know what is verified versus uncertain.

An advanced analyst should be able to inspect:

evidence lineage
provider state
parser version
source independence
historical changes
confidence reasoning
contradictions
scan differences
provider health
performance
reproducibility information

Do not make unsupported claims that a feature is unique across all GitHub repositories.

Instead describe genuinely differentiating features factually and demonstrate them with working code and tests.

Maintain the existing EmailIntel Ultra rules:

NO mandatory API key
NO mandatory login
NO OAuth dependency
NO browser plugin requirement
NO credential acquisition
NO private account access
NO fabricated findings

Build these capabilities as part of:

**EMAILINTEL ULTRA**

Owner / Maintainer:

**Chandra Kumar Yadav**
