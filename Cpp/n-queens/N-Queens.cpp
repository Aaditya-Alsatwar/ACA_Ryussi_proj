#include <bits/stdc++.h>
using namespace std;

int a[30], cnt;

int place(int pos)
{
    int i;
    for (i = 1; i < pos; i++) {
        if ((a[i] == a[pos])    ||    ((abs(a[i] - a[pos]) == abs(i - pos))))
            return 0;
    }
    return 1;
}

void print_sol(int N)
{
    
    cnt++;
    if (N<=8){
        cout << "\n\nSolution " << cnt << ":\n";
        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= N; j++) {
                if (a[i] == j)
                    cout << "(" << i << "," << j << ")";

            }
            cout << endl;
        }
    } 
}

void queen(int n)
{
    cnt = 0;
    int k = 1;
    a[k] = 0;
    while (k != 0) {
        a[k] = a[k] + 1;
        while ((a[k] <= n) && !place(k)){
            a[k]++;
        }    
        if (a[k] <= n) {
            if (k == n)
                print_sol(n);
            else {
                k++;
                a[k] = 0;
            }
        }
        else
            k--;
    }
}


int main()
{
    int N;
    cout << "Enter the size of the chess borad:";
    cin >> N;


    queen(N);
    cout << "\nTotal solutions=" << cnt;
    return 0;
}
