1. Reverse a string

```c++
#include <iostream>

int main()
{
    std::string test, output="";
    getline(std::cin, test);

    for(int i = (test.length()-1); i >= 0; i--) {
        output += test[i];
    }

    std::cout << output;

    return 0;
}
```

`Time Complexity`: `O(n)`

```c++
#include <iostream>

int main()
{
    std::string test;
    getline(std::cin, test);

    int len = test.length();

    for(int i = 0; i < (len/2); i++) {
        std::swap(test[i], test[(len-1)-i]);
    }

    std::cout << test;

    return 0;
}
```

`Time Complexity`: `O(n/2) ~ O(n)`. This code is more efficient than the first one because we've to loop through only n/2 times.
