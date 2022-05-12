
def get_freq(d_num, d_max, d_sum):
    if d_num * d_max < d_sum: return 0
    if d_num > d_sum: return 0
    if d_num == 1: return 1

    return sum(
        get_freq(d_num-1, d_max, d_sum-d_res)
        for d_res in range( 1,d_max+1 )
    )

def get_sum_freq_list(d_num, d_max):
    num_outcomes = d_max**d_num
    return [
        ( S, round(100*get_freq(d_num, d_max, S)/num_outcomes,2) )
        for S in range( d_num, d_max*d_num + 1 )
    ]

if __name__ == "__main__":
    num, sides = 2, 6
    for (d_sum, pct) in get_sum_freq_list(num, sides):
        print(f"Sum of {d_sum}: {pct}%")
