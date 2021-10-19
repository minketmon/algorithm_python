#include <iostream>
#include <vector>
#include <algorithm>
/*
6
0 1 1 0 0 0
0 1 1 0 1 1
0 0 0 0 1 1
0 0 0 0 1 1
1 1 0 0 1 0
1 1 1 0 0 0
*/
using namespace std;
int n;
int cnt = 1;
int graph[1001][1001];
vector<int> v;
bool dfs (int x, int y) {
	if (x < 0 || x >= n || y < 0 || y >= n)
		return false;
	if (graph[x][y] == 1) {
		graph[x][y]=0;

		if(dfs(x-1, y)) cnt+=1;
		if(dfs(x+1, y)) cnt+=1;
		if(dfs(x, y-1)) cnt+=1;
		if(dfs(x, y+1)) cnt+=1;
		return true;
	}
	return false;
}

int main() {
    cin >> n;

    for (int i=0; i<n; i++) {
        for(int j=0; j<n; j++) {
			scanf("%d", &graph[i][j]);
        }
    }
    int result = 0;
	for(int i=0; i<n; i++) {
		for (int j=0; j<n; j++) {
			if(dfs(i, j)) {
				result += 1;
				v.push_back(cnt);
				cnt = 1;
			}
		}
	}
	sort(v.begin(), v.end());

	cout << result << endl;
	for(int i=0; i<v.size(); i++) {
		cout << v[i] << " ";
	}
}