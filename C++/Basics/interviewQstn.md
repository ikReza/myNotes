> Write a function to print `1 2 3 4 5 6 7 8 9 8 7 6 5 4 3 2 1` with only one for loop

```c++
void print(int limit) {
    for(int i = 1; i < 2*limit; i++) {
        (i > 9) ? std::cout << (2*limit - i) : std::cout << i;
        std::cout << " ";
    }
}

int main() {
    int limit = 9;
    print(limit);
}
```

> Reverse a sentence without reversing the words. e.g. `I'm playing football` to `football playing I'm`.

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

int main()
{
    std::string str;
    getline(std::cin, str);

    reverseMe(str);
    std::cout << str;
}
```

> Find the duplicates and print them out

```c++
#include <iostream>
#include <vector>
#include <set>
#include <map>

int main()
{
    int n, e;
    std::cin >> n;

    std::vector<int> v;
    std::set<int> s;

    for(int i = 0; i < n; i++) {
        std::cin >> e;
        v.emplace_back(e);
        s.insert(e);
    }

    std::map<int, int> m;
    std::map<int, int>::iterator it;

    int count;

    for(int i: s) {
        count = 0;
        for(int j: v) {
            if(i == j) count++;
        }
        m.insert(std::pair<int, int>(i, count));
        // m.insert({i, count});
    }

    for(it = m.begin(); it != m.end(); it++) {
        if(it->second > 1) std::cout << it->first << " ";
    }
}
```
