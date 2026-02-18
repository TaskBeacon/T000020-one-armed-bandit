from __future__ import annotations

from dataclasses import dataclass, field
import random
from typing import Any

from psychopy import logging


@dataclass
class Controller:
    """Stationary block-wise one-armed-bandit controller."""

    block_probabilities: list[dict[str, float]] = field(
        default_factory=lambda: [
            {"left": 0.75, "right": 0.25},
            {"left": 0.25, "right": 0.75},
            {"left": 0.65, "right": 0.35},
            {"left": 0.35, "right": 0.65},
        ]
    )
    no_choice_policy: str = "random"
    randomize_within_block: bool = False
    enable_logging: bool = True

    def __post_init__(self) -> None:
        self._rng = random.Random(0)
        self.completed_trials: int = 0
        self.cumulative_reward: int = 0
        self.history: list[dict[str, Any]] = []
        self.block_probabilities = [self._normalize_prob_row(row) for row in self.block_probabilities]
        self.no_choice_policy = str(self.no_choice_policy).strip().lower()
        if self.no_choice_policy not in {"random", "left", "right"}:
            raise ValueError(
                "[BanditController] no_choice_policy must be one of: random, left, right."
            )

    @classmethod
    def from_dict(cls, config: dict[str, Any]) -> "Controller":
        allowed = {
            "block_probabilities",
            "no_choice_policy",
            "randomize_within_block",
            "enable_logging",
        }
        extra = set(config.keys()) - allowed
        if extra:
            raise ValueError(f"[BanditController] Unsupported config keys: {sorted(extra)}")
        return cls(
            block_probabilities=list(config.get("block_probabilities", [])),
            no_choice_policy=str(config.get("no_choice_policy", "random")),
            randomize_within_block=bool(config.get("randomize_within_block", False)),
            enable_logging=bool(config.get("enable_logging", True)),
        )

    @staticmethod
    def _normalize_prob_row(row: dict[str, Any]) -> dict[str, float]:
        if not isinstance(row, dict):
            raise ValueError(f"[BanditController] block probability row must be dict, got: {row!r}")
        if "left" not in row or "right" not in row:
            raise ValueError(f"[BanditController] block probability row missing left/right: {row!r}")
        left = max(0.0, min(1.0, float(row["left"])))
        right = max(0.0, min(1.0, float(row["right"])))
        return {"left": left, "right": right}

    def prepare_block(self, *, block_idx: int, n_trials: int, seed: int) -> list[tuple[float, float]]:
        if n_trials <= 0:
            return []
        if not self.block_probabilities:
            raise ValueError("[BanditController] block_probabilities is empty.")

        self._rng = random.Random(int(seed))
        prob = self.block_probabilities[int(block_idx) % len(self.block_probabilities)]
        trials: list[tuple[float, float]] = []
        for t in range(int(n_trials)):
            _ = t
            trials.append((float(prob["left"]), float(prob["right"])))

        if self.randomize_within_block:
            self._rng.shuffle(trials)

        if self.enable_logging:
            logging.data(
                f"[BanditController] block={block_idx} n_trials={n_trials} seed={seed} "
                f"p_left={prob['left']:.2f} p_right={prob['right']:.2f}"
            )
        return trials

    def fallback_choice(self, *, left_key: str, right_key: str) -> str:
        if self.no_choice_policy == "left":
            return left_key
        if self.no_choice_policy == "right":
            return right_key
        return left_key if self._rng.random() < 0.5 else right_key

    def draw_reward(self, *, choice_side: str, p_left: float, p_right: float) -> bool:
        p = float(p_left) if choice_side == "left" else float(p_right)
        p = max(0.0, min(1.0, p))
        return bool(self._rng.random() < p)

    def update(self, trial_summary: dict[str, Any]) -> None:
        self.completed_trials += 1
        reward_delta = int(trial_summary.get("reward_delta", 0) or 0)
        self.cumulative_reward += reward_delta
        self.history.append(dict(trial_summary))
        if self.enable_logging:
            logging.data(
                f"[BanditController] trial={self.completed_trials} "
                f"choice={trial_summary.get('choice_side')} "
                f"win={bool(trial_summary.get('reward_win', False))} "
                f"delta={reward_delta} total={self.cumulative_reward}"
            )
