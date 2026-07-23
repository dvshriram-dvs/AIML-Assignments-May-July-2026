from stable_baselines3 import PPO

print("Loading model...")
model = PPO.load("ppo_model", device="cpu")
print("Model loaded successfully!")