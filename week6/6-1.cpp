/* [HSAT 인증평가 2회] 사물인식 최소 면적 산출 프로그램 */
#include <iostream>
#include <limits.h>
#include <vector>

using namespace std;

int N, K;
int surface = INT_MAX;
vector<vector<pair<int,int>>> color;

void dfs(int colorIdx, int xMax, int yMax, int xMin, int yMin){
    if(K < colorIdx){
        surface = min(surface, abs((xMax-xMin) * (yMax-yMin)));
        return;
    }

    int size = color[colorIdx].size();
    for(int i = 0; i < size; i++){
        int xNew = color[colorIdx][i].first;
        int yNew = color[colorIdx][i].second;

        int xMaxNew = max(xMax, xNew);
        int yMaxNew = max(yMax, yNew);
        int xMinNew = min(xMin, xNew);
        int yMinNew = min(yMin, yNew);

        int s = abs((xMaxNew-xMinNew) * (yMaxNew-yMinNew));
        if((s < surface) || (colorIdx == 1)){
            dfs(colorIdx+1, xMaxNew, yMaxNew, xMinNew, yMinNew);
        }
    }
}

int main(){
    cin >> N >> K;
    color.resize(K+1);

    for(int i = 0; i < N; i++){
        int x, y, k;
        cin >> x >> y >> k;
        color[k].push_back({x,y});
    }
    
    dfs(1, -1001, -1001, 1001, 1001);
    cout << surface << '\n';

    return 0;
}