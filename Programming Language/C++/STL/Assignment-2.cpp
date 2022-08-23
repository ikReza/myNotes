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
        int D;
        cin >> D;
        int earn[D], spent[D];
        f(e, 0, D) {
            cin >> earn[e];
        }
        f(s, 0, D) {
            cin >> spent[s];
        }
        int Q;
        cin >> Q;
        
        v.emplace_back(vector<int> ());
        
        f(j, 0, Q) {
            int q;
            cin >> q;
            int sum = 0;
            F(k, 0, q) {
                sum += earn[k] - spent[k];
            }
            sum >= 0 ? v[i].emplace_back(1) : v[i].emplace_back(0);
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
