# Parameter Mapping

## Mapping Table

| Parameter ID | Config Path | Implemented Value | Source Paper ID | Evidence (quote/figure/table) | Decision Type | Notes |
|---|---|---|---|---|---|---|
| total_blocks | `task.total_blocks` | `4` | DAW2006_NATURE | Repeated block-level learning under changing contingencies | inferred | QA/sim uses shorter profile |
| trial_per_block | `task.trial_per_block` | `40` | WILSON2014_JEPG | Repeated choices needed to estimate explore/exploit tendencies | inferred | Human profile |
| response_keys | `task.left_key`, `task.right_key` | `f`, `j` | WILSON2014_JEPG | Binary discrete choice stage | inferred | Keyboard-side mapping |
| continue_key | `task.key_list` | `space` included | inferred | Instruction/break continuation key | inferred | Operational UI detail |
| reward_values | `task.reward_win`, `task.reward_loss` | `10`, `0` | DAW2006_NATURE | Bernoulli win/loss outcomes mapped to score delta | inferred | Score display format |
| pre_choice_fixation_duration | `timing.pre_choice_fixation_duration` | `0.5` | DAW2006_NATURE | Pre-choice fixation before each decision event | inferred | Timing parameter |
| bandit_choice_duration | `timing.bandit_choice_duration` | `2.5` | WILSON2014_JEPG | Time-limited decision window for RT capture | inferred | Choice stage |
| choice_confirmation_duration | `timing.choice_confirmation_duration` | `0.4` | inferred | Brief post-choice separation from feedback | inferred | Auditability/timing clarity |
| outcome_feedback_duration | `timing.outcome_feedback_duration` | `0.8` | DAW2006_NATURE | Distinct reward feedback epoch | inferred | Reinforcement signal display |
| iti_duration | `timing.iti_duration` | `0.6` | inferred | Event separation between trials | inferred | ITI stage |
| block_probabilities | `condition_generation.block_probabilities` | `[[0.75,0.25],[0.25,0.75],[0.65,0.35],[0.35,0.65]]` | SCHULZ2019_PNAS | Structured option probability asymmetry and reversals | inferred | Block-level contingency schedule |
| no_choice_policy | `condition_generation.no_choice_policy` | `random` | inferred | Policy when choice times out | inferred | Prevent deterministic side bias |
| trigger_fixation | `triggers.map.pre_choice_fixation_onset` | `20` | inferred | Fixation phase marker | inferred | EEG-friendly event code |
| trigger_choice | `triggers.map.bandit_choice_onset` | `30` | inferred | Choice phase marker | inferred | Stage onset code |
| trigger_confirm | `triggers.map.choice_confirmation_onset` | `40` | inferred | Confirmation phase marker | inferred | Stage onset code |
| trigger_feedback | `triggers.map.outcome_feedback_win_onset/loss_onset` | `50/51` | inferred | Win/loss feedback markers | inferred | Outcome-valence coding |
| trigger_iti | `triggers.map.iti_onset` | `60` | inferred | ITI onset marker | inferred | Phase boundary |
