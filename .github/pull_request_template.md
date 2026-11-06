## What
Added shipment region normalisation logic to standardise incoming dispatch payload region formats.

## Why
The dispatch API returns inconsistent region names (e.g., variations in casing and whitespace), causing shipment records to fail when joining against the region dimension table.

Closes #42

## How I tested
- [x] Ran unit tests using `pytest` to confirm non-breaking changes.
- [x] Tested common region name variations against `ingestion.py`.
- [x] Verified normalised region codes map correctly ($f(x) = y$).

## Checklist
- [x] Changes are focused.
- [x] No secrets or credentials committed.
- [x] Tests updated.
- [x] README updated where necessary.
