/* [21년 재직자 대회 예선] 전광판 */

#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main(){
    /*
        . 0 .
        1   2
        | 3 |
        4   5
        . 6 .
    */
    vector<vector<int>> lights;
    lights.push_back({1,1,1,0,1,1,1}); // 0
    lights.push_back({0,0,1,0,0,1,0}); // 1
    lights.push_back({1,0,1,1,1,0,1}); // 2
    lights.push_back({1,0,1,1,0,1,1}); // 3
    lights.push_back({0,1,1,1,0,1,0}); // 4
    lights.push_back({1,1,0,1,0,1,1}); // 5
    lights.push_back({1,1,0,1,1,1,1}); // 6
    lights.push_back({1,1,1,0,0,1,0}); // 7
    lights.push_back({1,1,1,1,1,1,1}); // 8
    lights.push_back({1,1,1,1,0,1,1}); // 9

    int onOffTransition[10] = {6,2,5,5,4,5,6,4,7,6};

    int T = 0;
    cin >> T;

    for(int i = 0; i < T; i++){
        string A, B;
        cin >> A >> B;
        int lenA = A.size();
        int lenB = B.size();

        int result = 0;

        if(lenA != lenB){
            if(lenA < lenB){
                for(int j = 0; j < lenB-lenA; j++){
                    result += onOffTransition[B[j]-'0'];
                }
                B = B.substr(lenB-lenA, lenB);
                lenB = B.size();
            }
            else{
                for(int j = 0; j < lenA-lenB; j++){
                    result += onOffTransition[A[j]-'0'];
                }
                A = A.substr(lenA-lenB, lenA);
                lenA = A.size();
            }
        }

        for(int j = 0; j < lenA; j++){
            for(int k = 0; k < 8; k++){
                if(lights[A[j]-'0'][k] != lights[B[j]-'0'][k]){
                    result++;
                }
            }
        }

        cout << result << endl;
    }

    return 0;
}