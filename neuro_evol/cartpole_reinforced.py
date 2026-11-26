"""Train a simple PPO agent to balance CartPole, then watch it play."""

import gymnasium as gym
from stable_baselines3 import PPO

import cartpole_env as env

# Train without opening a window. PPO learns from many short episodes.
training_env = gym.make(env.ENV_ID)
try:
    model = PPO("MlpPolicy", training_env, verbose=1, seed=0)
    model.learn(total_timesteps=20_000)
finally:
    training_env.close()


def best_policy(observation):
    action, _state = model.predict(observation, deterministic=True)
    return int(action)


# Run one deterministic episode with the environment displayed.
env.run_best_policy(best_policy, seed=0)
