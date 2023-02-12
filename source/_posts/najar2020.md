---
title: Najar et al. (2020)
subtitle: The actions of others act as a pseudo-reward to drive imitation in the context of social reinforcement learning
date: 2020/12/08
authors:
- Najar, Anis
- Bonnet, Emmanuelle
- Bahrami, Bahador
- Palminteri, Stefano
journal: PLoS Biol.
paper_url: https://doi.org/10.1371/journal.pbio.3001028
data_url: https://github.com/hrl-team/mfree_imitation
tags:
- 2-arm bandit
- social decision making
sample_size: 370
---

While there is no doubt that social signals affect human reinforcement learning, there is still no consensus about how this process is computationally implemented. To address this issue, we compared three psychologically plausible hypotheses about the algorithmic implementation of imitation in reinforcement learning. The first hypothesis, decision biasing (DB), postulates that imitation consists in transiently biasing the learners action selection without affecting their value function. According to the second hypothesis, model-based imitation (MB), the learner infers the demonstrators value function through inverse reinforcement learning and uses it to bias action selection. Finally, according to the third hypothesis, value shaping (VS), the demonstrators actions directly affect the learners value function. We tested these three hypotheses in 2 experiments (N = 24 and N = 44) featuring a new variant of a social reinforcement learning task. We show through model comparison and model simulation that VS provides the best explanation of learners behavior. Results replicated in a third independent experiment featuring a larger cohort and a different design (N = 302). In our experiments, we also manipulated the quality of the demonstrators choices and found that learners were able to adapt their imitation rate, so that only skilled demonstrators were imitated. We proposed and tested an efficient meta-learning process to account for this effect, where imitation is regulated by the agreement between the learner and the demonstrator. In sum, our findings provide new insights and perspectives on the computational mechanisms underlying adaptive imitation in human reinforcement learning.
