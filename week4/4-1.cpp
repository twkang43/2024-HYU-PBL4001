/* [21년 재직자 대회] 코딩 테스트 세트 */

#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

vector<int> clist;
vector<int> dlist;
int N, T;

bool test(int mid){
    vector<int> slist(N,0);
    slist[0] = clist[0];

    for(int i = 0; i < N-1; i++){
        if(mid <= slist[i]){
            slist[i+1] = clist[i+1] + dlist[i];
        }
        else if(mid <= slist[i] + dlist[i]){
            slist[i+1] = clist[i+1] + (slist[i] + dlist[i] - mid);
        }
        else{
            return false;
        }
    }

    return (mid <= slist[N-1]) ? true : false;
}

int binarySearch(int start, int end){
    if(start == end){
        return start;
    }

    int mid = (start+end+1) / 2;
    if(test(mid)){
        return binarySearch(mid, end);
    }   
    else{
        return binarySearch(start, mid-1);
    }
}

int main(){
    cin >> N >> T;

    for(int i = 0; i < T; i++){
        int result = 0;

        for(int j = 0; j < (2*N-1); j++){
            if(j%2 == 0){
                int c;
                cin >> c;
                clist.push_back(c);
            }
            else{
                int d;
                cin >> d;
                dlist.push_back(d);
            }
        }

        cout << binarySearch(0, 2*pow(10,12)) << '\n';
        clist.clear();
        dlist.clear();
    }

    return 0;
}