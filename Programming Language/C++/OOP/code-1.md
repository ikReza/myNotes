It's a good practice to define variables in the private access specifier and then modify in the setter methods in public specifier.

```c++
#include <iostream>
#include <sstream>

using namespace std;

class Student
{
    private:
        int age, standard;
        string first_name, last_name;

    public:
        void set_age(int num) {
            age = num;
        }
        void set_standard(int num) {
            standard = num;
        }
        void set_first_name(string name) {
            first_name = name;
        }
        void set_last_name(string name) {
            last_name = name;
        }

        int get_age() { return age; }
        int get_standard() { return standard; }
        string get_first_name() { return first_name; }
        string get_last_name() { return last_name; }

        string to_string() {
            stringstream ss1, ss2;
            string s1, s2;
            ss1 << age;
            ss1 >> s1;
            ss2 << standard;
            ss2 >> s2;
            return s1 + "," + first_name + "," + last_name + "," + s2;
        }
};

int main()
{
    int age, standard;
    string first_name, last_name;

    cin >> age >> first_name >> last_name >> standard;

    Student st;
    st.set_age(age);
    st.set_standard(standard);
    st.set_first_name(first_name);
    st.set_last_name(last_name);

    cout << st.get_age() << "\n";
    cout << st.get_last_name() << ", " << st.get_first_name() << "\n";
    cout << st.get_standard() << "\n";
    cout << "\n";
    cout << st.to_string();
}
```

Here, `sstream` is used to convert integer to string.

Let's understand this with simple example.

```c++
#include <iostream>
#include <sstream>
#include <typeinfo>

using namespace std;

int main()
{
    int number;
    cin >> number;

    // step-1: define
    stringstream ss;
    string str;

    // step-2: insert the value into the stream
    ss << number;

    // step-3
    ss >> str;

    cout << typeid(number).name() << "\n" << typeid(str).name();
}
```

**step-2:** the `<<` insertion operator inserts the `number` into the string.

**step-3:** the `>>` extraction operator extracts the data out of the stream and stores it in `str` variable.