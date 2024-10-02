/* [21년 재직자 대회 예선] 로드 밸런서 트래픽 예측 */
/* 오답; 다시 풀기 */

#include <iostream>
#include <vector>
#include <stack>

using namespace std;

vector<vector<int>> dag;

vector<int> topological_sort(int N){
    vector<int> indegree(N+1,0);
    for(int i = 1; i <= N; i++){
        int elementLen = dag[i].size();
        for(int j = 0; j < elementLen; j++){
            indegree[dag[i][j]]++;
        }
    }

    stack<int> s;
    for(int i = 1; i < N+1; i++){
        if(indegree[i] == 0){
            s.push(i);
        }
    }

    vector<int> order;
    while(!s.empty()){
        int node = s.top();
        order.push_back(node);
        s.pop();

        int elementLen = dag[node].size();
        for(int i = 0; i < elementLen; i++){
            indegree[dag[node][i]]--;

            if(indegree[dag[node][i]] == 0){
                s.push(dag[node][i]);
            }
        }
    }

    return order;
}

int main(){
    int N, K;
    cin >> N >> K;

    dag.resize(N+1);

    for(int i = 1; i < N+1; i++){
        int r;
        cin >> r;

        vector<int> element(r);
        for(int j = 0; j < r; j++){
            cin >> element[j];
        }
        dag[i] = element;
    }

    vector<int> order = topological_sort(N);

    vector<int> result(N+1,0);
    result[1] = K;

    for(int i = 0; i < N; i++){
        int currentNode = order[i];
        int request = result[currentNode];
        int childNum = dag[currentNode].size();

        if(0 < childNum){
            int quotient = request / childNum;
            int remainder = request % childNum;

            for(int j = 0; j < childNum; j++){
                int child = dag[currentNode][j];
                result[child] += quotient;
            }

            for(int j = 0; j < remainder; j++){
                int child = dag[currentNode][j];
                result[child]++;
            }
        }
    }

    for(vector<int>::iterator iter = result.begin()+1; iter != result.end(); iter++){
        cout << *iter << " ";
    }
    cout << endl;

    return 0;
}