import os
import gymnasium as gym
from stable_baselines3 import PPO
from stable_baselines3.common.evaluation import evaluate_policy

MODEL_PATH = "ppo_model.zip"

if not os.path.exists(MODEL_PATH):
    print("Model not found! Run train.py first.")
    exit()

env = gym.make("LunarLander-v3")

model = PPO.load(MODEL_PATH)

print("Evaluating model...")

mean_reward, std_reward = evaluate_policy(
    model,
    env,
    n_eval_episodes=100,
    deterministic=True
)

report = f"""
AUTONOMOUS LUNAR LANDING USING PPO
==================================

Environment : LunarLander-v3
Episodes    : 100
Mean Reward : {mean_reward:.2f}
Std Reward  : {std_reward:.2f}

Evaluation Complete
"""

print(report)

with open("evaluation_report.txt", "w") as f:
    f.write(report)

print("Evaluation report saved.")