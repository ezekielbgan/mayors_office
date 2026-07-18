# Changelog

## Unreleased

### Added
- Reusable UI banner and header functions

### Changed
- Refactored main game loop to remove duplicate Year 1 logic
- Combined Year 1 setup with the main yearly cycle
- Configuration section for game constants
- Starting city statistics now use configuration constants
- Improved screen formatting with reusable UI components
- Redesigned Annual Municipal Report interface
- Updated game introduction and opening narration


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