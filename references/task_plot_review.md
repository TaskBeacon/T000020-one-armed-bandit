# Task Plot Review

## Evidence Match

- Pass: title and construct match the two-option bandit learning task.
- Pass: rows match configured block reward probabilities: 75/25, 25/75, 65/35, and 35/65.
- Pass: phase order matches README and `src/run_trial.py`: Fixation -> Bandit choice -> Confirmation -> Outcome feedback -> ITI.
- Pass: timing labels match config: 500 ms fixation, 2500 ms choice, 400 ms confirmation, 800 ms feedback, 600 ms ITI.
- Pass: choice key mapping shows F for left and J for right.
- Pass: outcome feedback shows reward +10, no reward +0, and running total.

## Visual Quality

- Pass: labels and timings are readable.
- Pass: generated timeline content stays below the header band.
- Pass: fixed title and Construct subtitle are centered.
- Pass: top-right TaskBeacon logo lockup is borderless and non-overlapping.
- Pass: no generated title, logo, watermark, people, devices, or decorative scene is present.

## README Embed

- Pass: `README.md` contains `## 2. Task Flow`.
- Pass: the section embeds `![Task Flow](task_flow.png)`.
- Pass: final image is saved as `task_flow.png`; raw timeline is saved as `references/task_plot_timeline_raw.png`.
