/* [21년 재직자 대회 예선] 비밀 메뉴 2 */

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> firstInput;
vector<int> secondInput;
vector<vector<int>> LCS;

int main(){
    int N, M, K;
    cin >> N >> M >> K;

    firstInput.resize(N,0);
    secondInput.resize(M,0);
    LCS.resize(N+1, vector<int>(M+1,0));

    for(int i = 0; i < N; i++){
        cin >> firstInput[i];
    }

    for(int i = 0; i < M; i++){
        cin >> secondInput[i];
    }

    int result = 0;

    for(int i = 1; i < N+1; i++){
        for(int j = 1; j < M+1; j++){
            if(firstInput[i-1] == secondInput[j-1]){
                LCS[i][j] = LCS[i-1][j-1] + 1;
            }
            result = max(result, LCS[i][j]);
        }
    }

    cout << result << endl;

    return 0;
}