import gymnasium as gym

ENV_ID = "CartPole-v1"


def run_episode(policy, episode_len=500, render=False, environment=None, seed=None):
    """Run a single episode using a policy(observation) -> action callable."""
    owns_environment = environment is None
    if owns_environment:
        render_mode = "human" if render else None
        environment = gym.make(ENV_ID, render_mode=render_mode)

    total_reward = 0.0
    try:
        obs, _info = environment.reset(seed=seed)
        for _ in range(episode_len):
            if render:
                environment.render()
            action = policy(obs)
            obs, reward, terminated, truncated, _info = environment.step(action)
            total_reward += reward
            if terminated or truncated:
                break
        return total_reward
    finally:
        if owns_environment:
            environment.close()


def evaluate_policy(policy, n_episodes=5, episode_len=500, base_seed=None):
    """Evaluate a policy(observation) -> action over n_episodes.

    Returns a 1-tuple (mean_reward,) so it works directly as a DEAP fitness.
    """
    total_rewards = 0.0

    evaluation_env = gym.make(ENV_ID)
    try:
        for episode in range(n_episodes):
            seed = None if base_seed is None else base_seed + episode
            total_rewards += run_episode(
                policy,
                episode_len=episode_len,
                environment=evaluation_env,
                seed=seed,
            )
    finally:
        evaluation_env.close()
    return (total_rewards / n_episodes,)


def run_best_policy(policy, episode_len=500, seed=None):
    """Render one episode of the best policy and print its total reward."""
    print("Running the best policy...")
    reward = run_episode(policy, episode_len=episode_len, render=True, seed=seed)
    print("Reward:", reward)
    return reward

