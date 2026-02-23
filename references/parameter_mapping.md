# Parameter Mapping

| Parameter | Implemented Value | Source Paper ID | Confidence | Rationale |
|---|---|---|---|---|
| `task.total_blocks` | `4` | `DAW2006_NATURE` | `inferred` | Multi-block structure supports evolving choice strategy under contingency changes. |
| `task.trial_per_block` | `40` | `WILSON2014_JEPG` | `inferred` | Repeated choices per context are needed for stable learning estimates. |
| `task.key_list` | `["f","j","space"]` | `inferred` | `inferred` | Two-key forced choice plus continue key for instruction/break pages. |
| `task.left_key/right_key` | `f / j` | `inferred` | `inferred` | Keyboard mapping follows existing TaskBeacon convention. |
| `task.reward_win/reward_loss` | `10 / 0` | `DAW2006_NATURE` | `inferred` | Binary reward outcome encoded as points for behavioral scoring. |
| `timing.pre_choice_fixation_duration` | `0.5` | `inferred` | `inferred` | Brief fixation before each choice. |
| `timing.bandit_choice_duration` | `2.5` | `WILSON2014_JEPG` | `inferred` | Time-limited choice window for consistent RT collection. |
| `timing.choice_confirmation_duration` | `0.4` | `inferred` | `inferred` | Short confirmation epoch after response selection. |
| `timing.outcome_feedback_duration` | `0.8` | `DAW2006_NATURE` | `inferred` | Explicit outcome feedback period. |
| `timing.iti_duration` | `0.6` | `inferred` | `inferred` | Short ITI balances pacing and temporal separation. |
| `controller.block_probabilities` | `[[0.75/0.25],[0.25/0.75],[0.65/0.35],[0.35/0.65]]` | `SCHULZ2019_PNAS` | `inferred` | Structured block-wise reward asymmetry and reversals for adaptive learning. |
| `controller.no_choice_policy` | `random` | `inferred` | `inferred` | Avoid deterministic bias when no response occurs. |
| `triggers.map.pre_choice_fixation_onset` | `20` | `inferred` | `inferred` | Phase onset trigger for pre-choice fixation. |
| `triggers.map.bandit_choice_onset` | `30` | `inferred` | `inferred` | Phase onset trigger for choice window. |
| `triggers.map.choice_confirmation_onset` | `40` | `inferred` | `inferred` | Phase onset trigger for confirmation display. |
| `triggers.map.outcome_feedback_win_onset / outcome_feedback_loss_onset` | `50 / 51` | `inferred` | `inferred` | Outcome-valence feedback onset triggers. |
| `triggers.map.iti_onset` | `60` | `inferred` | `inferred` | Inter-trial interval onset trigger. |
