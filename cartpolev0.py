import gym
import random

class Agent:
    def __init__(self, env):
        self.action_size = env.action_space.n
    
    def get_action(self, state):
        pole_angle = state[2]
        action = 0 if pole_angle < 0 else 1
        return action

env = gym.make('CartPole-v1')

agent = Agent(env)
state = env.reset()

for _ in range(200):
    action = agent.get_action(state)
    state, reward, done, info = env.step(action)
    env.render()
