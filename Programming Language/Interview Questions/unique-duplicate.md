## Find Unique/Duplicate values in an array

**C++**

```c++
#include <bits/stdc++.h>

using namespace std;

void findUnique(vector<int> vec) {
    //if we don't care about sorting, we can use set.
    vector<int> myV;
    for(int elem: vec) {
        auto it = find(myV.begin(), myV.end(), elem);
        if(it != myV.end()) continue;
        else myV.emplace_back(elem);
    }

    for(int elem: myV) {
        cout << elem << " ";
    }
}

void findDuplicate(vector<int> vec) {
    unordered_set<int> s1, s2;

    for(int elem: vec) {
        if(s1.find(elem) != s1.end()) {
            if(s2.find(elem) != s2.end()) continue;
            else s2.insert(elem);
        }
        else s1.insert(elem);
    }

    for(int elem: s2) {
        cout << elem << " ";
    }
}

int main()
{
    vector<int> vec = {1, 3, 4, 2, 1, 3, 1};
    //findUnique(vec);
    findDuplicate(vec);
}
```

**Python**

```py
def printUnique(li):
	unique = []
	for elem in li:
		if elem not in unique:
			unique.append(elem)

	for elem in unique:
		print(elem, end=" ")

def printDuplicate(li):
	unique = []
	duplicate = []
	for elem in li:
		if elem in unique and elem not in duplicate:
			duplicate.append(elem)
		if elem not in unique:
			unique.append(elem)

	for elem in duplicate:
		print(elem, end=" ")

if __name__ == '__main__':
	li = [1, 3, 4, 2, 1, 3, 1]
	printDuplicate(li)
```
