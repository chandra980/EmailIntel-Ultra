# Project Status

This page separates **implemented code** from **specification / roadmap**.

## Implemented

### Core
- Email validation/classification
- Target-aware scan planning
- Async provider execution
- Evidence IDs
- Evidence hashes / family IDs
- Confidence metadata
- Freshness metadata
- SQLite history

### Public Providers
- Google Public DNS-over-HTTPS
- RDAP.org
- GitHub public commit search
- crt.sh certificate transparency
- Gravatar public profile
- keys.openpgp.org

### Terminal
- Rich-formatted terminal output
- Provider/source table
- Live QUERYING / RESULT trace
- Source URLs
- Final results table
- Detailed evidence panels

### Reports
- HTML
- JSON
- CSV
- TXT

### Analysis Commands
- plan
- providers
- coverage
- doctor
- timeline
- explain
- diff
- version

## Specification / Next Implementation Target

The following are described in `docs/TERMINAL_UI_SPEC.md` and/or `docs/ADVANCED_SPEC.md`, but should not be treated as implemented until corresponding code/tests land:

- full-screen persistent TUI command center;
- dark/light-green neon interface;
- interactive keyboard navigation;
- single normal command with automatic full-deep behavior;
- live ETA recalculation;
- provider-health history;
- adaptive concurrency;
- persistent status bar;
- interactive findings browser;
- evidence graph;
- command palette;
- multi-level Simple/Analyst/Technical views;
- contradiction engine;
- source-independence engine;
- provider drift sentinel;
- case management;
- reproducibility capsule;
- local web dashboard.

## Status Rule

A feature is only marked **Implemented** when:

1. executable code exists;
2. the feature is reachable through the application;
3. tests or reproducible verification exist;
4. documentation matches real behavior.

This prevents roadmap items from being presented as already working.
