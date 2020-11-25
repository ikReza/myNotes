## Reverse a sentence

> Reverse a string

**C++**

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

**Python**

```py
def reverseMe(text):
	print(text[::-1])

if __name__ == '__main__':
	text = input()
	reverseMe(text)
```

**Javascript**

Javascipt strings are immutable.

_N.B:_ `test.split("")` and `[...test]` works same.

```js
const reverseMe = (test) => {
  let step1 = test.split(""); // ["I", " ", "a", "m", " ", "g", "o", "o", "d"]
  let step2 = step1.reverse();
  let step3 = step2.join("");
  return step3;

  // In a single line
  // return test.split("").reverse().join("");

  // Alternate approach with spread operator
  // return [...test].reverse().join("");
};

let str = "I am good";

reverseMe(str);
```

---

> Reverse a sentence without reversing the words. e.g. `I'm playing football` to `football playing I'm`.

**C++**

```c++
#include <iostream>
#include <stack>

void reverseMe(std::string &str) {
    int low = 0, high = 0;

    std::stack<std::string> stk;

    for(int i = 0; i < str.length(); i++) {
        if(str[i] == ' ') {
            stk.push(str.substr(low, (high - low) + 1));
            low = high = i + 1;
        } else {
            high = i;
        }
    }

    // push the last word
    stk.push(str.substr(low));


    str.clear();

    while(!stk.empty()) {
        str.append(stk.top());
        if(stk.size() != 1) str.append(" ");
        stk.pop();
    }
}

// Alternate reverseMe() function with stringstream
void reverseString(std::string &str) {
    std::stack<std::string> stk;
    std::stringstream ss(str);
    std::string word;

    while(ss >> word) {
        stk.push(word);
    }

    str.clear();
    while(!stk.empty()) {
        str.append(stk.top());
        if(stk.size() >= 1) str.append(" ");
        stk.pop();
    }
}

// Alternate using vector
void reverseMe(string str) {
    vector<string> vec;
    stringstream ss(str);
    string word;

    while(ss >> word) {
        vec.push_back(word);
    }

    for(auto it = vec.rbegin(); it != vec.rend(); it++) {
        cout << *it << " ";
    }
}

int main()
{
    std::string str;
    getline(std::cin, str);

    reverseMe(str);
    std::cout << str;
}
```

**Python**

```py
def reverseMe(text):
	splitText = text.split(" ")
	reverseText = splitText[::-1]
    joinText = " ".join(reverseText)
    print(joinText)

if __name__ == '__main__':
	line = input()
	reverseMe(line)
```

**Javascript**

```js
const reverseLine = (test) => {
  return test.split(" ").reverse().join(" ");
};

reverseLine("He is good");
```
