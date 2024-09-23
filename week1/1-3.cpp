/* [21년 재직자 대회 예선] 좌석 관리 */

#include <iostream>
#include <vector>
#include <map>
#include <limits>
#include <cmath>

using namespace std;

vector<vector<bool>> isSeatOccupied; // false : not in use, true : in use
map<int, int> idStatus; // 0 : not eat, 1 : eating, 2 : finished eating
map<int, vector<int>> idLocation;

float getNearestDistance(int x, int y){
    float minDistance = numeric_limits<float>::max();

    int iterLen = idLocation.size();
    for(const auto& pair : idLocation){
        const std::vector<int>& location = pair.second;

        float distance = sqrt(pow(x-location[0], 2) + pow(y-location[1], 2));
        if(distance < minDistance){
            minDistance = distance;
        }
    }

    return minDistance;
}

bool assignSeat(int id, int N, int M){
    float targetDistance = 0.0;
    int target_x = 0;
    int target_y = 0;

    for(int i = 1; i <= N; i++){
        for(int j = 1; j <= M; j++){
            // continue if the seat or adjacent seats are occupied
            if(isSeatOccupied[i][j] || isSeatOccupied[i][j-1] || isSeatOccupied[i][j+1] || isSeatOccupied[i-1][j] || isSeatOccupied[i+1][j]){
                continue;
            }

            float currentDistance = getNearestDistance(i, j);
            if(targetDistance < currentDistance){
                targetDistance = currentDistance;
                target_x = i;
                target_y = j;
            }
        }
    }

    // if there are no available seats
    if(!idLocation.empty() && targetDistance == 0.0){
        return false;
    }

    idStatus[id] = 1;
    idLocation[id] = {target_x, target_y};
    isSeatOccupied[target_x][target_y] = true;

    return true;
}

void leaveSeat(int id){
    int x = idLocation[id][0];
    int y = idLocation[id][1];

    idStatus[id] = 2;
    isSeatOccupied[x][y] = false;
    idLocation.erase(id);
    cout << id << " leaves from the seat (" << x << ", " << y << ")." << endl;

    return;
}

int main(){
    int N, M, Q;
    cin >> N >> M >> Q;

    isSeatOccupied.resize(N+2, vector<bool>(M+2, false)); // with margins

    for(int i = 0; i < Q; i++){
        string operation;
        int id;
        cin >> operation >> id;

        if(operation == "In"){
            if(idStatus[id] == 0){ // assign a seat
                if(assignSeat(id, N, M)){
                    cout << id << " gets the seat (" << idLocation[id][0] << ", " << idLocation[id][1] << ")." << endl;
                }
                else{
                    cout << "There are no more seats." << endl;
                }
            }
            else if(idStatus[id] == 1){ // already seated
                cout << id << " already seated." << endl;
            }
            else{ // already ate lunch
                cout << id << " already ate lunch." << endl;
            }
        }
        else{
            if((idStatus.find(id) == idStatus.end()) || (idStatus[id] == 0)){ // didn't eat lunch
                cout << id << " didn't eat lunch." << endl;
            }
            else if(idStatus[id] == 1){ // leaves from the seat
                leaveSeat(id);
            }
            else{ // already left seat
                cout << id << " already left seat." << endl;
            }
        }
    }

    return 0;
}