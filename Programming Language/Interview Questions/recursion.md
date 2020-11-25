## 1. Fibonacci number e.g. _0 1 1 2 3 5 8 13 ..._

**C++**

> This code will return the nth term of fibonacci series

```c++
int fib(int n) {
    if(n <= 1) return n;

    return fib(n-1) + fib(n-2);
}
```

`Time Complexity`: `O(2^n)`⚠

> This code will print the fibonacci series up to n

```c++
void fib(int n) {
    int first = 0, sec = 1, next;
    for(int i = 0; i <= n; i++) {
        cout << first << " ";
        next = first + sec;
        first = sec;
        sec = next;
    }
}
```

✅ (Dynamic Programming)

👉 We can use `memoization` to improve time complexity -> `Top Down Approach`

```c++
#define MAX_N 20
#define EMPTY_VALUE -1

int memo[MAX_N + 1];

int f(int n) {
    if (n <= 1) return n;

    if (memo[n] != -1) {
        return memo[n];
    }

    memo[n] = f(n - 1) + f(n - 2);
    return memo[n];
}

void init() {
  for (int i = 0; i <= MAX_N; i++) {
      memo[i] = EMPTY_VALUE;
  }
}
```

👉 `Tabulation` or `Bottom Up approcah`

```c++
class DP
{
    public:
        int fib(int n) {
            int memo[n+1];
            memo[0] = 0;
            memo[1] = 1;

            for(int i = 2; i <= n; i++) {
                memo[i] = memo[i-1] + memo[i-2];
            }
            return memo[n];
            // for printing the series
            // for(int el: memo) cout << el << " ";
        }
};

int main()
{
    int n;
    cin >> n;

    DP dp;
    cout << dp.fib(n);
}
```

**🐍 Python**

```py
def fib(n):
  f = [0, 1]

  for i in range(2, n+1):
    f.append(f[i-1] + f[i-2])

  return f[n]

if __name__ == "__main__":
  n = 7
  print(fib(n))
```

Using class 👇

```py
class DP:
  def __init__(self, num):
    self.num = num

  def fib(self):
    memo = [0, 1]

    for i in range(2, self.num+1):
      memo.append(memo[i-1] + memo[i-2])

    return memo[self.num]

if __name__ == "__main__":
  n = 7
  dp = DP(n)
  print(dp.fib())
```

---

## Combination (nCr)

**C++**

```c++
int nCr(int n, int r) {
    if(n == r) return 1;

    return n * nCr(n-1, r);
}

int main()
{
    int n, r;
    cin >> n >> r;

    cout << nCr(n, r)/nCr(n-r, 1);
}
```

**🐍 Python**

```py
def nCr(n, r):
  if(n == r):
    return 1
  return n * nCr(n-1, r)

if __name__ == "__main__":
  n = int(input())
  r = int(input())
  print(int(nCr(n, r) / nCr(n-r, 1)))
```
