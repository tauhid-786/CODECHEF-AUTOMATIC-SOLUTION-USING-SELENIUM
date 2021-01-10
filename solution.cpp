#include<bits/stdc++.h>
using namespace std;
#define ll long long unsigned
int main()
{
int t;
cin>>t;
while(t--)
{int n,s;
cin>>n>>s;
int a[n];
for(int i=0;i<n;i++)
{cin>>a[i];
}
int p[n];
for(int i=0;i<n;i++)
{
cin>>p[i];}
int p1=1234;
int p2=1234;
for(int i=0;i<n;i++)
{
if(p[i]==0) 
{
p1=min(p1,a[i]);
}
else
{
p2=min(p2,a[i]);
}
}
if(p1+p2+s<=100) cout<<"yes"<<endl;
else    cout<<"no"<<endl;
}
}
