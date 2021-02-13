def get_bins(lower_limit, upper_limit, step_size):
    bins = list(range(lower_limit, upper_limit+1, step_size))
    if (upper_limit - lower_limit) % step_size != 0:
        bins.append(upper_limit)
    return bins