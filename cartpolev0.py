import gym
import random

class Agent:
    def __init__(self, env):
        self.action_size = env.action_space.n
        self.initialize_gen()

    def initialize_gen(self):
        self.dna = []
        
        for _ in range(200):
            self.dna.append(random.randint(0, 1))

        print('DNA: ')
        print(self.dna)

    def save_gene(self):
        f = open('genes.txt', 'a+')
        f.write(self.dna)
        f.close()
    
    def get_action(self, state, steps):
        return self.dna[steps]

    def mutation(self, steps):
        if steps < 10:
            print('Score too low. Resseting dna.')
            self.initialize_gen()
        else:
            print('Applying mutation on gene ' + str(steps))

            if self.dna[steps] == 0:
                self.dna[steps] = 1
            else:
                self.dna[steps] = 0

            if random.randint(0, 100) == 50:
                r = random.randint(0, steps)
                print('Applying random mutation on gene ' + str(r))

                if self.dna[r] == 0:
                    self.dna[r] = 1
                else:
                    self.dna[r] = 0

def main():
    env = gym.make('CartPole-v1')

    agent = Agent(env)

    for i_episode in range(10000):
        state = env.reset()
        total_reward = 0
        steps = 0

        while True:
            env.render()
            action = agent.get_action(state, steps)
            _state, reward, done, _ = env.step(action)

            total_reward += reward

            if done:
                print('Episode ' + str(i_episode) + ':score=' + str(total_reward))

                if total_reward >= 195:
                    print('Sucess!')
                    agent.save_gene()

                agent.mutation(steps - 1)
                break

            state = _state
            steps += 1

if __name__ == '__main__':
    main()