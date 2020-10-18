> Why we need to use `cin.ignore()`?

Ans: [stack overflow](https://stackoverflow.com/questions/25475384/when-and-why-do-i-need-to-use-cin-ignore-in-c#:~:text=Essentially%2C%20for%20std%3A%3Acin,of%20the%20string%20you%20want.)

in short: If we want to use `getline()` after `cin`, we can't.

```c++
int i;
string s;

cin >> i;
getline(cin, s);
```

The output will be shown without taking the string s. That's why we need to add an extra line between them.

```c++
cin >> i;
cin.ignore(numeric_limits<streamsize>::max(),'\n');
getline(cin, s);
```

> `printf` and `scanf` are faster than `cin` and `cout`. How can we get the speed like `printf` and `scanf` in `c++`?

We need to add these two lines of code in our main function.

```c++
ios_base::sync_with_stdio(false);
cin.tie(NULL); cout.tie(NULL);
```

More info: https://www.geeksforgeeks.org/fast-io-for-competitive-programming/

> What is type casting?

To chnage from one type to another.

```c++
int a = 5;

cout << a/2;    // 2
//if we want to get the floating point
cout << (double)a/2    // 2.5
```

> How to set precision for float/double number?

```c++
#include <iomanip>

int main() {
    double a = 25/8;    // 3.125
    cout << fixed << setprecision(2) << a;  // 3.13
    cout << fixed << setprecision(5) << a;  // 3.12500
}
```
