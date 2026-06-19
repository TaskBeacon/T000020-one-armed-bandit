# Task Plot Brief

## Task

- Title: One-Armed Bandit Task
- Construct: reinforcement learning / value-based decision making / adaptive choice
- Paradigm: two-option bandit task with block-wise reward probability reversals.

## Rows

- Block 1: left 75%, right 25%
- Block 2: left 25%, right 75%
- Block 3: left 65%, right 35%
- Block 4: left 35%, right 65%

## Trial Timeline

1. Pre-choice fixation: 500 ms fixation, no response.
2. Bandit choice: 2500 ms. Show left and right bandit options. Press F for left or J for right.
3. Choice confirmation: 400 ms. Highlight selected option; if no response, internal fallback may impute a choice.
4. Outcome feedback: 800 ms. Show reward win (+10) or no reward (+0), plus running total.
5. ITI: 600 ms fixation, no response.

## Notes

- Reward is sampled from the selected side's block-specific probability.
- The visual should emphasize that probabilities are stable within a block and change across blocks.
