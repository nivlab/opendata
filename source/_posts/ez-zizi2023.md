---
title: Ez-zizi et al. (2023)
subtitle: 'Reinforcement learning under uncertainty: expected versus unexpected uncertainty and state versus reward uncertainty'
date: 2023/03/20
authors:
- Ez-zizi, Adnane
- Farrell, Simon
- Leslie, David
- Malhotra, Gaurav
- Ludwig, Casimir Johannes Hendrikus
journal: Comput Brain Behav
paper_url: https://doi.org/10.1007/s42113-022-00165-y
data_url: https://osf.io/43jx8/?view_only=8ccae6aaabd74faeb61be1a82989174f
tags:
- 2-arm bandit
sample_size: 85
---

Two prominent types of uncertainty that have been studied extensively are expected and unexpected uncertainty. Studies suggest that humans are capable of learning from reward under both expected and unexpected uncertainty when the source of variability is the reward. How do people learn when the source of uncertainty is the environments state and rewards themselves are deterministic? How does their learning compare with the case of reward uncertainty? The present study addressed these questions using behavioural experimentation and computational modelling. Experiment 1 showed that human subjects were generally able to use reward feedback to successfully learn the task rules under state uncertainty, and were able to detect a non-signalled reversal of stimulus-response contingencies. Experiment 2, which combined all four types of uncertainties—expected versus unexpected uncertainty, and state versus reward uncertainty—highlighted key similarities and differences in learning between state and reward uncertainties. We found that subjects performed significantly better in the state uncertainty condition, primarily because they explored less and improved their state disambiguation. We also show that a simple reinforcement learning mechanism that ignores state uncertainty and updates the state-action value of only the identified state accounted for the behavioural data better than both a Bayesian reinforcement learning model that keeps track of belief states and a model that acts based on sampling from past experiences. Our findings suggest a common mechanism supports reward-based learning under state and reward uncertainty.
