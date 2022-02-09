


def fibo_numbers():
    
    
    first=0
    second=1
    sum=0
    count=1
    n = 200000
    while(count<=n):    
        count+=1
        first=second
        second=sum
        sum=first+second


if __name__ == "__main__":
    fibo_numbers()


