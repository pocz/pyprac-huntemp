import concurrent.futures
import math
import matplotlib.pyplot as plt
import pandas as pd
import time
from itertools import chain
from matplotlib import ticker

def sieve_from_1(end):
    primes = list(range(2, end + 1))
    i = 0
    sqrt = math.isqrt(end)
    while primes[i] < sqrt:
        primes = [x for x in primes if x % primes[i] !=0 or x == primes[i]]
        i += 1
    return primes

def segmented_sieve(interval):
    check_primes = sieve_from_1(math.isqrt(interval[1]))

    primes = list(range(interval[0], interval[1] + 1))
    for i in check_primes:
        for j in primes:
            if j != i and j % i == 0:
                primes.remove(j)

    return primes

def intervals(high, threads):
    mylist = []
    c = 0
    start = 1
    while c < threads:
        end = start+high//threads-1
        mylist.append((start,end))
        c += 1
        start = end+1
    return mylist

def generate_primes(end, threads):
    param_list = intervals(end, threads)
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(segmented_sieve, param) for param in param_list]
    
    return list(chain(*[f.result() for f in futures]))

def timer(end, threads): 
    start = time.perf_counter_ns()
    generate_primes(end, threads)
    return time.perf_counter_ns()-start
    
def graph():
    thread_n = list(range(1,16))
    times = []
    for i in thread_n:
       times.append(timer(100000, i))

    pd.Series(data=times, index=thread_n).plot()
    plt.gca().set(
        title='Time Taken to Generate Primes up to 100,000', 
        xlabel='Number of Threads', 
        ylabel='Time (ns)'
    )
    plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(1.00))
 
    plt.show()
