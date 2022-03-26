#include<bits/stdc++.h>
using namespace std;
int N=1000001;
int primes[1000001];
void Gen_Seive(){
	for(int i=0;i<N;i++){
		primes[i]=1;
	}
	for(int i=2;i*i<N;i++){
		if(primes[i]==1){
			for(int j = i*i; j < N ; j+=i){
				primes[j]=0;
			}
		}
	}

}
vector<int>Gen_primes(int num){
	vector<int>ds;
	for(int i=2;i<=num;i++){
		if(primes[i]==1)ds.push_back(i);
	}
	return ds;
}
int main()
{
	Gen_Seive();
	int t;
	cin>>t;
	while(t--){
		int l,r;
		cin>>l>>r;
		vector<int> dj=Gen_primes(sqrt(r)+1);
		vector<int>dummy(r-l+1,1);

		for(int i=0;i<dj.size();i++){
			int firstmul=(l/i)*i<l?((l/i)+1)*i:(l/i)*i;
			for(int j = max(firstmul,i*i); j <= r ;j += i){
				dummy[j-l]=0;
			}
		}
		for(int i=0;i<r-l+1;i++){
			if(dummy[i]==1){
				cout<<l+i<<" ";
			}
		}

	}
	return 0;
}
