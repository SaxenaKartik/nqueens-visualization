#include <bits/stdc++.h>
using namespace std;

#define fast_io() ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0)
#define all(x) x.begin(), x.end()
#ifndef ONLINE_JUDGE
// #include "prettyprint.hpp"
#define debug(...) cout << "debug: " << #__VA_ARGS__ " = " << make_tuple(__VA_ARGS__) << endl
#else
#define debug(...) 0
#endif
typedef long long int ll;
#define int ll
typedef vector<int> vi;
typedef pair<int, int> pii;



int board[1000][1000];
int size;
int flag=0;

bool issafe(int r, int c)
{
	for (int i = 0; i < r; i++)
		if (board[i][c] == 1)
			return false;

	for (int i = r, j = c; i >= 0 && j >= 0; i--, j--)
		if (board[i][j] == 1)
			return false;

	for (int i = r, j = c; i >= 0 && j < size; i--, j++)
		if (board[i][j] == 1)
			return false;

	return true;
}

void nQueen(int r)
{
	
	if (r == size)
	{
		flag=1;
		
		for (int i = 0; i < size; i++) 
		{
			for (int j = 0; j < size; j++)
				cout << board[i][j] << " ";
			cout << endl;
		}
		cout << endl;
		return ;
	}

	for (int i = 0; i < size; i++) 
	{
		for (int j = 0; j < size; j++)
			cout << board[i][j] << " ";
		cout << endl;
	}
	cout << endl;



	
	for (int i = 0; i < size; i++) 
	{
		
		if (issafe(r, i)) 
		{
			
			board[r][i] = 1;

			
			nQueen(r + 1);

			board[r][i] = 0;
		}
	}
}

int32_t main()
{
	int N;
	scanf("%lld",&N);
	size=N;
	// memset(board, '0', sizeof board);
	nQueen(0);
	if(flag==1)
	{
		printf("YES\n");
	}
	else
	{
		printf("NO\n");
	}
	return 0;
}