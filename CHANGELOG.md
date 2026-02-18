# CHANGELOG

All notable development changes for `T000020-one-armed-bandit` are documented here.

## [0.2.0] - 2026-02-17

### Changed
- Replaced MID-style placeholder implementation with a real one-armed-bandit trial flow:
  - choice between left/right machines
  - probabilistic reward draw based on selected machine
  - selection confirmation stage
  - reward/score feedback with cumulative scoring
- Replaced adaptive target-duration controller with block probability schedule controller (`src/utils.py`).
- Refactored `main.py` to generate per-block probability conditions via controller and report bandit metrics (left choice rate, win rate, score).
- Rewrote configs to human-friendly, mode-separated profiles with Chinese participant text and `SimHei` font:
  - `config.yaml`
  - `config_qa.yaml`
  - `config_scripted_sim.yaml`
  - `config_sampler_sim.yaml`
- Replaced generic sampler with task-specific bandit sampler policy in `responders/task_sampler.py`.
- Updated `README.md` to standardized task2doc contract sections and one-armed-bandit logic.

### Fixed
- Removed non-bandit cue/target hit-miss logic inherited from MID scaffold.
- Removed condition labels shown as participant-facing protocol cues.

### Verified
- `python -m psyflow.validate <task_path>`
- `python main.py qa --config config/config_qa.yaml`
- `python main.py sim --config config/config_scripted_sim.yaml`
- `python main.py sim --config config/config_sampler_sim.yaml`

## [0.1.0] - 2026-02-17

### Added
- Added initial PsyFlow/TAPS task scaffold for One-Armed Bandit Task.
- Added mode-aware runtime (`human|qa|sim`) in `main.py`.
- Added split configs (`config.yaml`, `config_qa.yaml`, `config_scripted_sim.yaml`, `config_sampler_sim.yaml`).
- Added responder trial-context plumbing via `set_trial_context(...)` in `src/run_trial.py`.
- Added generated cue/target image stimuli under `assets/generated/`.

### Verified
- `python -m psyflow.validate <task_path>`
- `psyflow-qa <task_path> --config config/config_qa.yaml --no-maturity-update`
- `python main.py sim --config config/config_scripted_sim.yaml`
- `python main.py sim --config config/config_sampler_sim.yaml`
