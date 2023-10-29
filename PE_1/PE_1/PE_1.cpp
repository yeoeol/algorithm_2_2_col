#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int N;
    cin >> N;
    vector<vector<int>> v;
    
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            int n;
            cin >> n;
            v[i].push_back(n);
        }
    }

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cout << v[i][j];
        }
    }
}