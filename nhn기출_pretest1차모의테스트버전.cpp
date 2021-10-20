#include <iostream>
#include <sstream>
#include <vector>
#include <algorithm>
using namespace std;

struct input_data {
    int sizeOfMatrix;
    int** matrix;
};
struct input_data inputData;
int cnt = 1;

bool dfs(int x, int y) {
    if (x < 0 || x >= inputData.sizeOfMatrix || y < 0 || y >= inputData.sizeOfMatrix) {
        return false;
    }
    if (inputData.matrix[x][y] == 1) {
        inputData.matrix[x][y] = 0;
        if (dfs(x, y - 1)) cnt += 1;
        if (dfs(x, y + 1)) cnt += 1;
        if (dfs(x - 1, y)) cnt += 1;
        if (dfs(x + 1, y)) cnt += 1;

        return true;
    }
    return false;
}

void solution(int sizeOfMatrix, int** matrix) {
    int result = 0;
    vector <int> v;
    for (int i = 0; i < sizeOfMatrix; i++) {
        for (int j = 0; j < sizeOfMatrix; j++) {
            if (dfs(i, j)) {
                result += 1;
                v.push_back(cnt);
                cnt = 1;
            }
        }
    }
    sort(v.begin(), v.end());

    cout << result << "\n";
    for (int i = 0; i < v.size(); i++) {
        cout << v[i] << " ";
    }
}

void process_stdin(struct input_data& inputData) {
    string line;
    istringstream iss;

    getline(cin, line);
    iss.str(line);
    iss >> inputData.sizeOfMatrix;

    inputData.matrix = new int* [inputData.sizeOfMatrix];
    for (int i = 0; i < inputData.sizeOfMatrix; i++) {
        getline(cin, line);
        iss.clear();
        iss.str(line);
        inputData.matrix[i] = new int[inputData.sizeOfMatrix];
        for (int j = 0; j < inputData.sizeOfMatrix; j++) {
            iss >> inputData.matrix[i][j];
        }
    }
}

int main() {
    process_stdin(inputData);

    solution(inputData.sizeOfMatrix, inputData.matrix);
    return 0;
}