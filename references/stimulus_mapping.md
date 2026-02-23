# Stimulus Mapping

Task: `One-Armed Bandit Task`

| Stage | Implemented Stimulus IDs | Source Paper ID | Evidence | Implementation Mode | Notes |
|---|---|---|---|---|---|
| Condition registry | `bandit` | `DAW2006_NATURE`, `WILSON2014_JEPG` | Canonical two-option probabilistic bandit choice condition repeated across trials. | `psychopy_builtin` | Base condition token used in `config/config.yaml`. |
| Pre-choice fixation | `fixation` | `DAW2006_NATURE` | Trial-by-trial bandit tasks include pre-choice fixation/ready interval. | `psychopy_builtin` | Neutral pre-choice fixation. |
| Choice | `machine_left`, `machine_right`, `machine_left_label`, `machine_right_label`, `choice_prompt`, `highlight_left/right` | `DAW2006_NATURE`, `WILSON2014_JEPG` | Discrete option selection with explicit response mapping. | `psychopy_builtin` | No condition labels shown to participants. |
| Selection confirmation | `target_prompt` + selected highlight | `inferred` | Short post-choice confirmation improves response auditability and participant certainty. | `psychopy_builtin` | Kept brief to avoid altering learning dynamics. |
| Outcome feedback | `feedback_win`, `feedback_loss` | `DAW2006_NATURE`, `SCHULZ2019_PNAS` | Outcome feedback reflects stochastic reward from chosen option. | `psychopy_builtin` | Displays per-trial reward delta and running total. |
| Inter-block / end | `block_break`, `good_bye` | `inferred` | Standard task operation and participant pacing. | `psychopy_builtin` | Reports summary metrics only. |

Implementation mode legend:
- `psychopy_builtin`: stimulus rendered via PsychoPy primitives in config.
