/* [21년 재직자 대회 예선] 거리 합 구하기 */

#include <iostream>
#include <vector>

using namespace std;

vector<vector<vector<int>>> tree;
vector<int> subtreeSize;
vector<int> distFromNode;

void dfs1(int current, int parent){
    subtreeSize[current] = 1;
    int currentLen = tree[current].size();

    for(int i = 0; i < currentLen; i++){
        int child = tree[current][i][0];
        int weight = tree[current][i][1];

        if(child != parent){
            dfs1(child, current);
            distFromNode[current] += (distFromNode[child] + weight*subtreeSize[child]); // the value is only valid for a node 1
            subtreeSize[current] += subtreeSize[child];
        }
    }

    return;
}

void dfs2(int current, int parent, int N){
    int currentLen = tree[current].size();

    for(int i = 0; i < currentLen; i++){
        int child = tree[current][i][0];
        int weight = tree[current][i][1];

        if(child != parent){
            distFromNode[child] = distFromNode[current] + weight*(N-2*subtreeSize[child]);
            dfs2(child, current, N);
        }
    }

    return;
}

int main(){
    int N;
    cin >> N;

    tree.resize(N+1);
    subtreeSize.resize(N+1,0);
    distFromNode.resize(N+1,0);

    for(int i = 1; i < N; i++){
        int x, y, t;
        cin >> x >> y >> t;
        tree[x].push_back({y,t});
        tree[y].push_back({x,t});
    }

    dfs1(1,1);
    dfs2(1,1,N);

    int distLen = distFromNode.size()-1;
    for(int i = 1; i < distLen+1; i++){
        cout << distFromNode[i] << endl;
    }

    return 0;
}