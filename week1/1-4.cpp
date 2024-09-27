/* [21년 재직자 대회 예선] 회의실 예약 */

#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

vector<string> room;
vector<pair<string, pair<int,int>>> meeting;

int main(){
    int N, M;
    cin >> N >> M;

    for(int i = 0; i < N; i++){
        string roomName;
        cin >> roomName;
        room.push_back(roomName);
    }

    for(int i = 0; i < M; i++){
        string roomName;
        int startTime, endTime;
        cin >> roomName >> startTime >> endTime;
        meeting.push_back({roomName, {startTime,endTime}});
    }

    sort(room.begin(), room.end());

    for(int i = 0; i < N; i++){
        cout << "Room " << room[i] << ":" << endl;
        vector<int> time = {9, 10, 11, 12, 13, 14, 15, 16, 17, 18};
        queue<pair<int,int>> availableTime;
        
        for(int j = 0; j < M; j++){
            if(room[i] == meeting[j].first){
                int startTime = meeting[j].second.first;
                int endTime = meeting[j].second.second;

                for(int k = startTime; k < endTime; k++){
                    time[k-9] = -1;
                }
            }
        }

        bool available = false;
        int start = 0;
        for(int j = 0; j < 10; j++){
            if(0 < start && time[j] < 18){
                available = true;
            }

            if(0 < start && time[j] == -1){
                availableTime.push({start, j+9});
                start = 0;
            }
            else if(start == 0 && -1 < time[j]){
                start = j+9;
            }
        }

        if(0 < start && start < 18){
            availableTime.push({start, 18});
            available = true;
        }

        if(available){
            cout << availableTime.size() << " available:" << endl;
            while(!availableTime.empty()){
                pair<int,int> time = availableTime.front();

                if(time.first == 9){
                    cout << "09-" << time.second << endl;
                }
                else{
                    cout << time.first << "-" << time.second << endl;
                }

                availableTime.pop();
            }
        }
        else{
            cout << "Not available" << endl;
        }
        
        if(i < N-1){
            cout << "-----" << endl;
        }
    }

    return 0;
}