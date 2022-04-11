#include<bits/stdc++.h>
using namespace std;

void subseq(int ind,int n,vector<int>&ds,int arr[])
{
	if(ind==n)
	{
		for(int i=0;i<ds.size();i++)
		{
			cout<<ds[i]<<" ";
		}
		cout<<"\n";
		return ;
	}
	ds.push_back(arr[ind]);
	subseq(ind+1,n,ds,arr);
	ds.pop_back();
	
	subseq(ind+1,n,ds,arr);
}

int main()
{
	int n;
	cin>>n;
	vector<int> ds;
	int arr[n];
	cout<<"enter arr elements";
	
	for(int i=0;i<n;i++)
	{
		cin>>arr[i];
	}
	
	subseq(0,n,ds,arr);
	return 0;
	
}
