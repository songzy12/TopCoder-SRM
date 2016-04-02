#include<bits/stdc++.h>
using namespace std;
const int maxn = 550;
int a[maxn];
int t[maxn];
const double ONECMP = log(0.5);
int times;

void merge_sort(int* a,int l,int r) {
    if(r-l<=1) return ;
    int mid = (l+r)>>1;
    merge_sort(a,l,mid);
    merge_sort(a,mid,r);
    
    int i = l, j = mid, k =l,p;
    while(i < mid && j < r){
        times++;
        if(a[i]>=a[j]) 
            t[k] = a[j++];
        else 
            t[k] = a[i++];
        k++;
    }
    if(i == mid) 
        for(p = j; p < r; p++) 
            t[k++] = a[p];
    else 
        for(p = i; p < mid; p++) 
            t[k++] = a[p];
    for(k = l;k < r; k++) 
        a[k] = t[k];
}


class BearSortsDiv2{
public:
    double getProbability(vector <int> seq){
        for(int i = 0; i < seq.size(); i++){
            a[seq[i]-1] = i; // like we define a new order
        }
        times = 0;
        merge_sort(a,0,seq.size()); // times of comparison
        return times*ONECMP;
    }
};