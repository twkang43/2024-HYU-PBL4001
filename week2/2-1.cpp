/* [21년 재직자 대회 예선] 이미지 프로세싱 */

#include <iostream>
#include <vector>
#include <queue>

using namespace std;

vector<vector<int>> matrix;
vector<vector<int>> command;
int direction[4][2] = {{1,0}, {0,1}, {-1,0}, {0,-1}};

void bfs(int i, int j, int c, int H, int W){
    int currentColor = matrix[i][j];
    matrix[i][j] = c;
    queue<pair<int,int>> q;
    q.push({i,j});

    while(!q.empty()){
        int x = q.front().first;
        int y = q.front().second;
        q.pop();

        for(int i = 0; i < 4; i++){
            int nx = x + direction[i][0];
            int ny = y + direction[i][1];

            if((nx < 1 || H < nx) || (ny < 1 || W < ny)){
                continue;
            }

            if(matrix[nx][ny] == currentColor){
                matrix[nx][ny] = c;
                q.push({nx,ny});
            }
        }
    }
}

int main(){
    int H, W;
    cin >> H >> W;
    matrix.resize((H+1), vector<int>((W+1)));
    
    for(int i = 1; i <= H; i++){
        for(int j = 1; j <= W; j++){
            cin >> matrix[i][j];
        }
    }

    int Q;
    cin >> Q;
    command.resize(Q, vector<int>(3));

    for(int k = 0; k < Q; k++){
        int i, j, c;
        cin >> i >> j >> c;

        if(matrix[i][j] != c){
            bfs(i, j, c, H, W);
        }
    }

    for(int i = 1; i <= H; i++){
        for(int j = 1; j <= W; j++){
            cout << matrix[i][j] << ' ';
        }
        cout << endl;
    }

    return 0;
}