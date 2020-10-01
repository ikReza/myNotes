```c++
#include <iostream>

// Base class
class Shape {
    protected:
        int width;
        int height;

    public:
        void setWidth(int w) {
            width = w;
        }

        void setHeight(int h) {
            height = h;
        }
};

// Derived class
class Rectangle: public Shape {
    public:
        int getArea() {
            return width * height;
        }
};

int main()
{
    Rectangle rect;

    rect.setWidth(5);
    rect.setHeight(10);

    std::cout << "Area: " << rect.getArea();

    return 0;
}

```

> Why we kept class member (height, width) in the `protected` section?

- Because we don't want to access this information and modify directly like `rect.height = 10`. This is a good practice to use a setter method in the public section to update the height/width.

- I didn't defined this in the `private` section because I want access this in the _inherited classes_.

---

Let's see some example of **function overriding**

```c++
class Animal {
    public:
        void makeSound() {
            std::cout << "Animals sound";
        }
};

class Dog: public Animal {
    public:
        void makeSound() {
            std::cout << "Dog is barking";
        }
};

class Cat: public Animal {
    public:
        void makeSound() {
            std::cout << "Cat is meowing";
        }
};
```
