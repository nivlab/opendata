import os
import numpy as np
from os.path import dirname
ROOT_DIR = dirname(dirname(os.path.realpath(__file__)))
POST_DIR = os.path.join(ROOT_DIR, 'source', '_posts')

## Locate posts.
posts = sorted([f for f in os.listdir(POST_DIR) if f.endswith('.md')])

## Main loop.
for post in posts:
    
    ## Read post.
    with open(os.path.join(POST_DIR, post)) as f:
        lines = f.readlines()
        
    ## Identify if sample size metadata present.
    is_sample_size = any([line.startswith('sample_size') for line in lines])
    
    ## Check if database entry.
    is_database = any(['database' in line.lower() for line in lines])
    
    ## Return info.
    if not is_sample_size and not is_database:
        print(post)