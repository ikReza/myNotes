## OOP

OOP has the following characteristics:

- name (BankAccount)
- attribute/variables (balance, accountNumber)
- behavior/function (open(), close(), deposit())

After defining class, we can create object based on that class.

- Each object is called an `instance`(example) of a class
- The process of creating object is called `instantiation`

---

1. Declare a class

```c++
class BankAccount {

};
```

Class has 3 access specifiers:

- public
- private
- protected

2. Create a class with public access specifiers

```c++
class BankAccount {
    public:
        void sayHi() {
            std::cout << "Hello!";
        }
};

int main() {
    BankAccount test;
    test.sayHi();

    return 0;
}
```

---

There are 4 priciples of OOP.

1. Encapsulation
2. Abstraction
3. Inheritence
4. Polymorphism

**Abstraction:** It is the concept of providing only the essential information to the outside of a class. It's a process of representing essential features without including implementaion details.

**Encapsulation:**

**Inheritance:** Reusability of code.

**Polymorphism:** One name, many forms.

---

**Constructor:**

- It is initialized when object is created.
- It has no return type
- Same name as the class

**Destructor:**

-

```c++
class Test {
    public:
        Test() {
            std::cout << "Constructor" << std::endl;
        }

        ~Test() {
            std::cout << "Destructor" << std::endl;
        }
};
```

---

**Function Overloading:**

Two or more functions have the same name but different parameters.
