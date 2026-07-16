# Changelog

## Unreleased

### Changed
- Refactored main game loop to remove duplicate Year 1 logic
- Combined Year 1 setup with the main yearly cycle
- Added configuration section
- Replaced hardcoded starting values with configuration constants

## v0.1.0 - Initial Release (2026-07-15)

### Added
- Core city management gameplay loop
- Player mayor introduction and naming system
- Four city statistics:
  - Population
  - Budget
  - Approval
  - Infrastructure
- Random breaking news events with three response options
- Event outcome system that changes city statistics
- Annual municipal summaries displaying stat changes
- Game-over conditions based on city collapse
- Separate event database from main game logic using `events.py`
- Prevention of consecutive duplicate events

### Changed
- None

### Fixed
- None
