import os
import gymnasium as gym
import matplotlib.pyplot as plt
import numpy as np

from stable_baselines3 import PPO
from stable_baselines3.common.monitor import Monitor
from stable_baselines3.common.results_plotter import load_results, ts2xy

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

env = gym.make("LunarLander-v3")
env = Monitor(env, LOG_DIR)

model = PPO(
    "MlpPolicy",
    env,
    verbose=1,
    learning_rate=3e-4,
    n_steps=2048,
    batch_size=64,
    gamma=0.99,
)

print("Training started...")
model.learn(total_timesteps=100000)

print("Training completed.")

model.save("ppo_model")

x, y = ts2xy(load_results(LOG_DIR), "timesteps")

window = 20

if len(y) >= window:
    y = np.convolve(y, np.ones(window)/window, mode="valid")
    x = x[window-1:]

plt.figure(figsize=(10,5))
plt.plot(x, y)
plt.xlabel("Timesteps")
plt.ylabel("Reward")
plt.title("LunarLander PPO Training")
plt.grid()

plt.savefig("learning_curve.png")

print("Model and graph saved.")