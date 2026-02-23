from __future__ import annotations
from typing import Dict, List, Optional, Any
from psychopy import logging
import random

class AdaptiveController:
    """
    AdaptiveController dynamically adjusts stimulus duration based on participant performance,
    aiming to maintain a target accuracy rate (hits within deadline).
    """

    def __init__(
        self,
        initial_duration: float = 2.0,
        min_duration: float = 0.5,
        max_duration: float = 5.0,
        step: float = 0.1,
        target_accuracy: float = 0.85,
        enable_logging: bool = True
    ):
        self.initial_duration = initial_duration
        self.min_duration = min_duration
        self.max_duration = max_duration
        self.step = step
        self.target_accuracy = target_accuracy
        self.enable_logging = enable_logging

        self.duration: float = initial_duration
        self.history: List[bool] = []

    @classmethod
    def from_dict(cls, config: dict[str, Any]) -> "AdaptiveController":
        allowed = {
            "initial_duration": 2.0,
            "min_duration": 0.5,
            "max_duration": 5.0,
            "step": 0.1,
            "target_accuracy": 0.85,
            "enable_logging": True
        }
        params = {k: config.get(k, default) for k, default in allowed.items()}
        return cls(**params)

    def update(self, hit: bool) -> None:
        self.history.append(bool(hit))
        acc = sum(self.history) / len(self.history)
        old_duration = self.duration

        if acc > self.target_accuracy:
            new_duration = max(self.min_duration, old_duration - self.step)
        else:
            new_duration = min(self.max_duration, old_duration + self.step)

        self.duration = new_duration

        if self.enable_logging:
            logging.data(
                f"[AdaptiveController] Accuracy:{acc:.1%} Trials:{len(self.history)} "
                f"duration:{old_duration:.3f}→{new_duration:.3f}"
            )

    def get_duration(self) -> float:
        return self.duration

class RewardTracker:
    """Tracks cumulative reward across trials."""
    def __init__(self, initial_reward: int = 0):
        self.cumulative_reward = initial_reward

    def update(self, delta: int) -> int:
        self.cumulative_reward += int(delta)
        return self.cumulative_reward

def generate_bandit_schedule(
    block_idx: int,
    n_trials: int,
    seed: int,
    block_probabilities: list[dict[str, float]]
) -> list[tuple[float, float]]:
    """
    Generate a sequence of (p_left, p_right) for a block.
    """
    if not block_probabilities:
        return [(0.5, 0.5)] * n_trials
    
    row = block_probabilities[int(block_idx) % len(block_probabilities)]
    p_left = float(row.get("left", 0.5))
    p_right = float(row.get("right", 0.5))
    
    return [(p_left, p_right)] * int(n_trials)

def draw_bandit_reward(p_left: float, p_right: float, choice_side: str, rng: Optional[random.Random] = None) -> bool:
    """
    Stochastically draw a reward based on the chosen side.
    """
    p = float(p_left) if choice_side == "left" else float(p_right)
    p = max(0.0, min(1.0, p))
    draw = rng.random() if rng else random.random()
    return draw < p

def get_fallback_choice(policy: str, left_key: str, right_key: str, rng: Optional[random.Random] = None) -> str:
    """
    Impute a choice in case of timeout.
    """
    policy = str(policy).lower().strip()
    if policy == "left":
        return left_key
    if policy == "right":
        return right_key
    
    _rng = rng or random.Random()
    return left_key if _rng.random() < 0.5 else right_key
