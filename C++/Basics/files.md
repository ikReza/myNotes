```c++
#include <fstream>
#include <vector>

#define eb emplace_back

int main()
{
    std::ofstream file ("test.txt");

    std::vector <std::string> names;
    names.eb("Kaiser");
    names.eb("Susan");
    names.eb("Amy");

    for(std::string name: names) {
        file << name << std::endl;
    }

    file.close();
    return 0;
}
```

Evertytime we run the app, the old data will be overridden by the new information.

We can change that by modifying some code:

```c++
std::ofstream file ("test.txt", std::ios::app);
```

We can expand the first line, but above code is popular because it's short.

```c++
std::ofstream file;
file.open("test.txt", std::ios::app);
```
