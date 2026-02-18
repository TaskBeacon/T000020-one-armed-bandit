# Task Logic Audit Template

Use this file as `references/task_logic_audit.md` before coding.

## 1. Paradigm Intent

- Task: One-Armed Bandit (or Multi-Armed Bandit)
- Primary construct: Decision making under uncertainty, exploration-exploitation trade-off, learning, reward processing.
- Manipulated factors: Number of arms, reward probabilities (fixed or volatile), reward magnitudes, number of trials, feedback type.
- Dependent measures: Choice data (arm selection), reaction times, cumulative reward, switching behavior, exploration/exploitation rates, model-derived parameters (e.g., learning rates).
- Key citations: [To be filled in Phase 1: Discover and Filter Literature]

## 2. Block/Trial Workflow

### Block Structure

- Total blocks: Typically 1 (or multiple if reward probabilities change over time)
- Trials per block: E.g., 200 trials (can vary greatly)
- Randomization/counterbalancing: Arm positions (left/right) randomized or counterbalanced across participants. Order of reward outcomes within an arm is probabilistic.

### Trial State Machine

List each state in order with entry/exit conditions:

1. State name: Choice Screen
   - Onset trigger: Start of trial / end of ITI
   - Stimuli shown: Two "arms" (e.g., images, symbols) presented side-by-side. Optional cumulative score display.
   - Valid keys: Keys corresponding to left/right arm choice (e.g., 'F' and 'J').
   - Timeout behavior: If no response, trial is marked as missed, proceed to ITI.
   - Next state: Feedback Screen

2. State name: Feedback Screen
   - Onset trigger: Participant makes a choice or timeout occurs.
   - Stimuli shown: Indication of reward (+X points) or no reward, update to cumulative score.
   - Valid keys: None (automatic progression after fixed duration).
   - Timeout behavior: Auto-advance after e.g., 1000ms.
   - Next state: ITI Screen

3. State name: ITI (Inter-Trial Interval) Screen
   - Onset trigger: End of Feedback Screen.
   - Stimuli shown: Blank screen or fixation cross.
   - Valid keys: None (automatic progression after fixed duration).
   - Timeout behavior: Auto-advance after e.g., 1000ms.
   - Next state: Choice Screen (for next trial) / End of Block

## 3. Condition Semantics

For each condition token in `task.conditions`:

- Condition ID: `arm_A`
  - Participant-facing meaning: Represents one of the choice options.
  - Concrete stimulus realization (visual/audio): E.g., "Blue Square" on the left side of the screen.
  - Outcome rules: Associated with a specific reward probability (e.g., 75% chance of +10 points).

- Condition ID: `arm_B`
  - Participant-facing meaning: Represents another choice option.
  - Concrete stimulus realization (visual/audio): E.g., "Green Circle" on the right side of the screen.
  - Outcome rules: Associated with a specific reward probability (e.g., 25% chance of +10 points).

(Note: Actual `task.conditions` will be defined in `config.yaml` and may include parameters like `reward_probability`, `reward_magnitude`, `stimulus_image_path`, etc.)

## 4. Response and Scoring Rules

- Response mapping: Key presses (e.g., 'F' for left arm, 'J' for right arm) map directly to arm selection.
- Missing-response policy: If no response within the allotted time for the Choice Screen, the trial is marked as a missed response. No reward is given. Proceed to ITI.
- Correctness logic: There is no "correct" or "incorrect" response in the traditional sense, as outcomes are probabilistic. The participant's goal is to maximize total reward.
- Reward/penalty updates: A reward (e.g., +10 points) is probabilistically delivered based on the chosen arm's reward probability. No explicit penalties other than not receiving a reward. The cumulative score is updated after each trial.
- Running metrics:
    - Choice per trial (which arm was selected)
    - Reaction time per choice
    - Outcome per trial (rewarded/not rewarded)
    - Cumulative reward
    - (Derived: proportion of choices for each arm over time, switching behavior, etc.)

## 5. Stimulus Layout Plan

For every screen with multiple simultaneous options/stimuli:

- Screen name:
- Stimulus IDs shown together:
- Layout anchors (`pos`):
- Size/spacing (`height`, width, wrap):
- Readability/overlap checks:
- Rationale:

## 6. Trigger Plan

Map each phase/state to trigger code and semantics.

## 7. Inference Log

List any inferred decisions not directly specified by references:

- Decision:
- Why inference was required:
- Citation-supported rationale:
