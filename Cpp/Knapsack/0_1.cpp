#include <bits/stdc++.h>

using namespace std;

int main(){
    int n,m=0;
    cout << "Enter the total number of items:";
    cin >> n;
    cout << "Enter the maximum weight possible:";
    cin >> m;


    int weight[n];
    int profit[n];

    for (int i=0 ; i<=n-1 ; i++){
        cout << "Enter the weight of item:";
        cin >> weight[i];
        cout << "Enter the profit of item:";
        cin >> profit[i];
    }

    int arr[n+1][m+1];


    for (int i=0; i < n+1 ; i++ ){
        for(int w=0; w<m+1 ; w++){
            if (i==0 || w==0){
                arr[i][w] = 0;
            }
            else if(w >= weight[i]){
                arr[i][w] = max(arr[i-1][w],arr[i-1][w-weight[i]]+profit[i]) ;
            }
            else{
                arr[i][w] = arr[i-1][w];
            }
        }
    }
    for (int i=0; i < n+1 ; i++ ){
        for(int w=0; w<m+1 ; w++){

            cout << arr[i][w] << " ";
        }
        cout << endl;
    }

    cout << arr[n][m] << endl;

    return 0;
}
