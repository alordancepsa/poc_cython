import time

from functions.fibo import fibo_numbers
from functions.primes import primes_main


if __name__ == "__main__":

    start = time.time()
    print("Start main test")
    for x in range(25):
        primes_main()
        fibo_numbers()
    
    end = time.time()
    print("Elapsed main test ", end - start)