#include <iostream>
using namespace std;

int main() {
	int H, W;
	cin >> H >> W;
	int arr[W];
	int table[H][W] = {0, };
	for(int i=0; i<W; i++) {
		scanf("%d", &arr[i]);
	}

	for(int i=0; i<H; i++) {
		for(int j=0; j<W; j++) {
			cout << table[i][j] << " ";
		}
		cout << "\n";
	}

}