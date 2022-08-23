#include <bits/stdc++.h>

#define f(i, a, b) for(int i = a; i < b; i++)
#define F(i, a, b) for(int i = a; i <= b; i++)

using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    // cout.tie(NULL);
    
    int n, q;
    cin >> n >> q;
    int arr[n];
    
    f(i, 0, n) {
        cin >> arr[i];
    }
    
    while(q--) {
        int p;
        cin >> p;
        int i, j, v;
        switch(p) {
            case 1:
                cin >> i;
                cout << arr[i] << "\n";
                arr[i] = 0;
                break;
            case 2:
                cin >> i >> v;
                arr[i] += v;
                break;
            case 3:
            {
                cin >> i >> j;
                int sum = 0;
                F(m, i, j) {
                    sum += arr[m];
                }
                cout << sum << "\n";;
                break;
            }
            default:
                break;
        }
    }
    
    f(i, 0, n) {
        cout << arr[i] << " ";
    }

    return 0;
}
