#include <iostream>
//#include <bits/stdc++.h>
/*
4 5
00110
00011
11111
00000
*/
using namespace std;
int n, m;
int graph[1001][1001];
bool dfs (int x, int y) {
	if (x < 0 || x >= n || y < 0 || y >= m)
		return false;
	if (graph[x][y] == 0) {

		graph[x][y]=1;

		dfs(x-1, y);
		dfs(x+1, y);
		dfs(x, y-1);
		dfs(x, y+1);
		return true;
	}
	return false;
}

int main() {
    cin >> n >> m;

    for (int i=0; i<n; i++) {
        for(int j=0; j<m; j++) {
            scanf("%1d", &graph[i][j]);
        }
    }

    int result = 0;
	for(int i=0; i<n; i++) {
		for (int j=0; j<m; j++) {
			if(dfs(i, j)) {
				result += 1;
			}
		}
	}
	cout << result << endl;
}
