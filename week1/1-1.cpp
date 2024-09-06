/* [21년 재직자 대회 예선] 비밀 메뉴 */

#include <iostream>
#include <vector>

using namespace std;

int main(){
    int M, N, K;
    cin >> M >> N >> K;

    vector<int> secretMenu(M, 0);
    for(int i = 0; i < M; i++){
        cin >> secretMenu[i];
    }
    
    vector<int> order(N, 0);
    for(int i = 0; i < N; i++){
        cin >> order[i];
    }

    bool result = true;

    if(N < M){
        result = false;
    }
    else{
        for(int i = 0; i < N; i++){
            result = true;
            int k = 0;

            for(int j = i; j < i+M; j++){
                if(order[j] != secretMenu[k]){
                    result = false;
                    break;
                }
                k++;
            }
            
            if(result){
                break;
            }
        }
    }

    if(result){
        cout << "secret" << endl;
    }
    else{
        cout << "normal" << endl;
    }

    return 0;
}