# ZallerZN2021

Data associated with [Zaller et al. (2021)](https://www.biologicalpsychiatryjournal.com/article/S0006-3223(21)00654-5/abstract). Data from N=99 participants who completed a modified version of the [Horizons task](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5635655/). | If you use this data, please cite as:

> Zaller, I., Zorowitz, S., & Niv, Y. (2021). Information Seeking on the Horizons Task Does Not Predict Anxious Symptomatology. Biological Psychiatry, 89(9), S217-S218.

## Data Codebook

| Variable | Description |
|----------|-------------|
| Subject | The anonymized subject identifier |
| Block | Block (or game) number |
| Trial | Trial (or turn) in game |
| Horizon | Horizon length of block |
| Info | Information condition: 1 = [3,1], 0 = [2,2], -1 = [1,3] |
| mu_L | Latent reward average of left bandit |
| mu_R | Latent reward average of right bandit |
| delta | Difference of latent reward averages | 
| Choice | Subject choice: 1 = left, 0 = right | 
| RT | Response time |
| Accuracy | Subject accuracy: 1 = higher reward bandit, 0 = lower reward bandit |
| Outcome | Points earned | 

## Survey Codebook

| Variable | Description |
|----------|-------------|
| Subject | The anonymized subject identifier |
| pswq-q[0-9] | Response to item *n* of the Penn State Worry Questionnaire (the last item is an infrequency item and should be discarded) |
| ius12-q[0-9] | Response to item *n* of the Intolerance of Uncertainty Questionnaire (the last item is an infrequency item and should be discarded) |
| nfc-q[0-9] | Response to item *n* of the Need for Closure questionnaire (the last item is an infrequency item and should be discarded)|
| \*\*-rt | The total time spent (in seconds) on a particular survey |
| \*\*-radio | The total number of radio button events for a particular survey (should be equal to or less than mouse + key) |
| \*\*-key | The total number of key press events for a particular survey |
| \*\*-mouse | The total number of mouse press events for a particular survey |
| \*\*-ipi | The average time (in seconds) between page events for a particular survey |

## Metadata Codebook

| Variable | Description |
|----------|-------------|
| Subject | The anonymized subject identifier |
| Time | Total time (in minutes) spent on experiment (surveys + task) |
| Age | Self-reported age (in years) |
| Gender-categorical | Self-reported gender |
| Gender-free-response | Self-reported gender |
| Ethnicity / race | Self-report ethnicity/race |
| Language | If English is first language |
| Fluency | Self-reported English language fluency |
| Loops | Number of times the participant needed to complete the instructions before advancing |
| Difficulty | Self-reported task difficulty (1 = very difficult, 5 = very easy) |
| Fun | Self-reported task fun (1 = no fun, 5 = very fun) |
| Clarity | Self-reported instructions clarity (1 = unclear, 5 = very clear) |
| Strategy | Self-reported task strategy |
| Feedback | Any additional comments |
