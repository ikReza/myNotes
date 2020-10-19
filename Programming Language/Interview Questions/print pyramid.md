> Write a function to print `1 2 3 4 5 6 7 8 9 8 7 6 5 4 3 2 1` with only one for loop

**C++**

```c++
void print(int limit) {
    for(int i = 1; i < 2*limit; i++) {
        (i > limit) ? std::cout << (2*limit - i) : std::cout << i;
        std::cout << " ";
    }
}

int main() {
    int limit = 9;
    print(limit);
}
```

**Python**

```py
def printPyramid(limit):
	for i in range(1, 2*limit):
		print(2*limit - i, end=" ") if(i > limit) else print(i, end=" ")

if __name__ == '__main__':
	limit = int(input())
	printPyramid(limit)
```
