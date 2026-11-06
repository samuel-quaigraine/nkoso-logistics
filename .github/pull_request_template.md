## What
Added input validation logic for incoming shipment payload data within `ingestion.py`.

## Why
Malformed or missing shipment data (e.g., invalid tracking numbers, negative weights, or null payload values) was causing silent downstream processing failures during pipeline ingestion.

Closes #43

## How I tested
- [x] Executed unit test suite via `pytest tests/test_shipment_validation.py`.
- [x] Tested boundary cases (e.g., zero weight, missing tracking ID, malformed ISO timestamps).
- [x] Verified that invalid records are flagged/logged correctly without crashing the pipeline execution.

## Checklist
- [x] Changes are focused and scoped to shipment validation.
- [x] No secrets, API keys, or production credentials committed.
- [x] Unit tests added/updated for all new validation rules.
- [x] Documentation or inline docstrings updated where necessary.
