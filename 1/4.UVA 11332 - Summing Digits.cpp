#include <iostream>
using namespace std;

long long a(long long n){
    while(n>=10){
        long long sum=0;
        while (n>0){
            sum+=n%10;
            n/=10;
        } 
        n=sum;

    }
    return n;
}

int main() {
    long long n;
    while(cin>>n || n!=0){
        cout<<a(n)<<endl;
    }
    return 0;
}