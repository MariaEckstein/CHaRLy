import numpy as np


def get_n_unique_items(dat):

    n_unique_items = 3 * np.ones(dat.shape[0])
    n_unique_items[dat['goal_star'].isin([0, 1]) & (dat['trial_type'] == 'learning')] = 4
    n_unique_items[(dat['goal_star'] == 1) & (dat['trial_type'] == 'transfer') & (dat['phase'] == 'low')] = 4
    n_unique_items[(dat['goal_star'] == 2) & (dat['trial_type'] == 'transfer') & (dat['phase'] == 'high')] = 4

    return n_unique_items

# # Example use
# get_n_unique_items(all_data)