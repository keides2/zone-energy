#include<bits/stdc++.h>

using namespace std;

const uint64_t m1  = 0x5555555555555555;
const uint64_t m2  = 0x3333333333333333;
const uint64_t m4  = 0x0f0f0f0f0f0f0f0f;
const uint64_t m8  = 0x00ff00ff00ff00ff;
const uint64_t m16 = 0x0000ffff0000ffff;
const uint64_t m32 = 0x00000000ffffffff;

int popcount(uint64_t x){
  x = (x & m1 ) + ((x >>  1) & m1 );
  x = (x & m2 ) + ((x >>  2) & m2 );
  x = (x & m4 ) + ((x >>  4) & m4 );
  x = (x & m8 ) + ((x >>  8) & m8 );
  x = (x & m16) + ((x >> 16) & m16);
  x = (x & m32) + ((x >> 32) & m32);
  return x;
}

typedef struct{
  int p;
  int q;
  int r;
}sol;

int main(){
  int n,m;
  cin >> n >> m;
  vector<uint64_t> g(n,0);
  for(int i=0;i<n;i++){g[i]|=(1ul<<i);}
  for(int i=0;i<m;i++){
    int a,b;
    cin >> a >> b;
    g[a]|=(1ul<<b);
    g[b]|=(1ul<<a);
  }

  int rval=0;
  vector<sol> res;
  for(int i=0;i<n;i++){
    for(int j=i+1;j<n;j++){
      for(int k=j+1;k<n;k++){
        int cur=popcount(g[i]|g[j]|g[k]);
        if(rval<cur){
          res.clear();
          rval=cur;
        }
        if(rval==cur){
          res.push_back({i,j,k});
        }
      }
    }
  }
  
  for(auto &nx : res){
    cout << nx.p << ' ';
    cout << nx.q << ' ';
    cout << nx.r << '\n';
  }
  return 0;
}