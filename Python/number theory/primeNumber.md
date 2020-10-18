```py
def sieve(n):
	primes = [True] * (n+1)

	primes[0] = primes[1] = 0

	# mark all the even numbers as not prime/0/false except 2
	for i in range(4, n+1, 2):
		primes[i] = 0


	# find the odd prime numbers and mark the numbers(not prime) which are multiples of this primes
	p = 3
	while(p*p <= n):
		if(primes[p]):
			for i in range(3*p, n+1, 2*p):
				primes[i] = 0

		p += 2

	# print the prime numbers up to n
	for i in range(n+1):
		if(primes[i]):
			print(i, end=" ")

if __name__ == "__main__":
	n = int(input())
	sieve(n)
```

---

### Prime Factorization

```py
def primeFactors(num):
	li = []

	while(num % 2 == 0):
		li.append(2)
		num /= 2

	i = 3
	while(i*i <= num):
		if(num % i == 0):
			li.append(i)
			num /= i
		i += 2

	if(num > 2):
		li.append(num)

	return li

if __name__ == "__main__":
	n = int(input())
	result = primeFactors(n)
	for elem in result:
		print(int(elem), end=" ")
```
