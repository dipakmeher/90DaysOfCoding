#include<bits/stdc++.h>
using namespace std;

int n;

int solution(int segments[]){
    unordered_map<int, int> mp;
    for(int i=0;i<n;i++)
        mp[segments[i]]++;
    vector<int> vec;
    for(auto itr = mp.begin(); itr!=mp.end(); itr++){
        if(itr->second>3)
            return 0;
        if(itr->second>1)
            vec.push_back(itr->first);
    }
    if(vec.size()<2)
        return -1;
    sort(vec.begin(), vec.end());
    
    int res = INT_MAX;
    for(int i=1;i<vec.size();i++){
        res = min(res, vec[i]-vec[i-1]);
    }
    
    return res;
}

int main(){
    cin>>n;
    int arr[n];
    for(int i=0;i<n;i++)
        cin>>arr[i];
    cout<<solution(arr)<<endl;
    return 0;
}

