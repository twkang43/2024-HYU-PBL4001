/* [21년 재직자 대회 예선] 마이크로서버 */

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
    int T = 0;
    cin >> T;

    for(int i = 0; i < T; i++){
        int serverCnt = 0;
        int N;
        cin >> N;

        vector<int> microService(N);
        for(int j = 0; j < N; j++){
            cin >> microService[j];
        }
        sort(microService.begin(), microService.end());

        int start = 0;
        int end = N-1;

        // 600 < m
        while((start <= end) && (600 < microService[end])){
            serverCnt++;
            end--;
        }

        // m: 600 + m: 300
        while((start <= end) && (microService[start] == 300) && (microService[end] == 600)){
            serverCnt++;
            start++;
            end--;
        }

        int mem300 = 0;
        while((start <= end) && microService[start] == 300){
            mem300++;
            start++;
        }

        while(start < end){
            if(microService[start] + microService[end] <= 900){
                serverCnt++;
                start++;
                end--;
            }
            else if(0 < mem300){
                serverCnt++;
                end--;
                mem300--;
            }
            else{
                serverCnt++;
                end--;
            }
        }

        if(start == end){
            serverCnt++;

            if(0 < mem300){
                mem300--;
            }
        }

        serverCnt += (mem300+2) / 3;
        
        cout << serverCnt << endl;
    }

    return 0;
}