#include <bits/stdc++.h>

using namespace std;

int main(){

    int n,m=0;
    cout << "Enter the total number of items:";
    cin >> n;
    cout << "Enter the maximum weight possible:";
    cin >> m;


    float weight[n];
    float profit[n];
    float p_w[n];
    for (int i=0 ; i<=n-1 ; i++){
        cout << "Enter the weight of item:";
        cin >> weight[i];
        cout << "Enter the profit of item:";
        cin >> profit[i];

        p_w[i] = profit[i] / weight[i];
    }
    
   
    float p=0;
    for (int i= 0; i<n ; i++){
        float x= *max_element(p_w,p_w +n);
        for (int j=0; j<n ; j++){
            if (x == p_w[j]){
                if(m >= weight[j]){
                    p_w[j]=0;
                    arr[j]=1;
                    m = m - weight[j];
                    p = p + profit[j];
                }
                else{
                    float z = weight[j]/m;
                    m = 0;
                    p = p + profit[j]/z;
                    arr[j] = weight[j]/m;
                }
            }
        }
    }

    cout << "Profit is :" << p <<endl;
    cout << "Items selected are: ";
    for(int i=0 ; i<n ; i++){
        cout << arr[i] << " ";
    }
    cout << endl;




    return 0;
}
