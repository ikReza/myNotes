#include <bits/stdc++.h>

#define f(i, a, b) for(int i = a; i < b; i++)
#define F(i, a, b) for(int i = a; i <= b; i++)

using namespace std;

int main()
{
    int T;
    cin >> T;
    
    vector< vector<int> > v;
    
    f(i, 0, T) {
        int W;
        cin >> W;
        int arr[W];
        f(w, 0, W) {
            cin >> arr[w];
        }
        int R1, R2;
        cin >> R1 >> R2;
        
        F(k, R1, R2) {
            if(arr[k] >= 10) {
                v.emplace_back(vector<int> ());
                v[i].emplace_back(k);
            }
        }
    }
    
    f(i, 0, T) {
        f(j, 0, v[i].size()) {
            cout << v[i][j] << " ";
        }
        cout << "\n";
    }

    return 0;
}
