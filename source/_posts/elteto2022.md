---
title: Éltető et al. (2022)
subtitle: Tracking human skill learning with a hierarchical Bayesian sequence model
date: 2022/11/30
authors:
- Éltető, Noémi
- Nemeth, Dezső
- Janacsek, Karolina
- Dayan, Peter
journal: PLoS Comput. Biol.
paper_url: https://doi.org/10.1371/journal.pcbi.1009866
data_url: https://github.com/noemielteto/HCRP_sequence_learning
tags:
- sequence learning
- serial reaction time
abstract: 'Humans can implicitly learn complex perceptuo-motor skills over the course of large numbers of trials. This likely depends on our becoming better able to take advantage of ever richer and temporally deeper predictive relationships in the environment. Here, we offer a novel characterization of this process, fitting a non-parametric, hierarchical Bayesian sequence model to the reaction times of human participants responses over ten sessions, each comprising thousands of trials, in a serial reaction time task involving higher-order dependencies. The model, adapted from the domain of language, forgetfully updates trial-by-trial, and seamlessly combines predictive information from shorter and longer windows onto past events, weighing the windows proportionally to their predictive power. As the model implies a posterior over window depths, we were able to determine how, and how many, previous sequence elements influenced individual participants internal predictions, and how this changed with practice. Already in the first session, the model showed that participants had begun to rely on two previous elements (i.e., trigrams), thereby successfully adapting to the most prominent higher-order structure in the task. The extent to which local statistical fluctuations in trigram frequency influenced participants responses waned over subsequent sessions, as participants forgot the trigrams less and evidenced skilled performance. By the eighth session, a subset of participants shifted their prior further to consider a context deeper than two previous elements. Finally, participants showed resistance to interference and slow forgetting of the old sequence when it was changed in the final sessions. Model parameters for individual participants covaried appropriately with independent measures of working memory and error characteristics. In sum, the model offers the first principled account of the adaptive complexity and nuanced dynamics of humans internal sequence representations during long-term implicit skill learning.'
---

Data from a study in which N=32 participants completed a serial reaction time task with second-order dependence, i.e. the Alternating Serial Reaction Time task (ASRT). Participants completed nine sessions of 2125 trials each, and a tenth session of 1700 trials, each separated by a week.
