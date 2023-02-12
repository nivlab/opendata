import os
import numpy as np
from os.path import dirname
ROOT_DIR = dirname(dirname(os.path.realpath(__file__)))
POST_DIR = os.path.join(ROOT_DIR, 'source', '_posts')

## Preallocate space.
titles = []
subtitles = []
paper_urls = []
abstracts = []

## Locate posts.
posts = sorted([f for f in os.listdir(POST_DIR) if f.endswith('.md')])

## Main loop.
for post in posts:
    
    ## Read post.
    with open(os.path.join(POST_DIR, post)) as f:
        lines = f.readlines()
        
    ## Identify / append lines.
    for line in lines:
        if line.startswith('title:'): titles.append(line.strip().replace('title: ',''))
        elif line.startswith('subtitle:'): subtitles.append(line.strip().replace('subtitle: ',''))
        elif line.startswith('paper_url:'): paper_urls.append(line.strip().replace('paper_url: ',''))
    abstracts.append(lines[-1].strip())
    
## Check for duplicates.
for arr in [titles, subtitles, paper_urls, abstracts]:
    
    ## Count entries.
    arr, counts = np.unique(arr, return_counts=True)
    
    ## Return info.
    if np.any(counts > 1):
        print(arr[counts > 1])