
def primetest(potentialprime):
    divisor = 2
    while divisor <= potentialprime:
        if potentialprime == 2:
            return True
        elif potentialprime % divisor == 0:
            return False
        while potentialprime % divisor != 0:
            if potentialprime - divisor > 1:
                divisor += 1
            else:
                return True

def primes_main():
        
    
    numprimes = 1000
    count = 0
    potentialprime = 2
    while count < int(numprimes):
        if primetest(potentialprime) == True:
            # print ('Prime #' + str(count + 1), 'is', potentialprime)
            count += 1
        potentialprime += 1
    

if __name__ == "__main__":
    primes_main()
