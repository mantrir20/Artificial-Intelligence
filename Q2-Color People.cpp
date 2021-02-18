#include<bits/stdc++.h>

using namespace std;

vector<string> all_colors{"RED", "BLUE", "GREEN"};

bool solve(unordered_map<string, int> left, string p1, string p2, int count, string boat)
{
    cout<<"boat at:"<<boat<<" "<<"RED:"<<left["RED"]<<" "<<"BLUE:"<<left["BLUE"]<<" "<<"GREEN:"<<left["GREEN"]<<" "<<"P1:"<<p1<<" "<<"P2:"<<p2<<" "<<"Trip num:"<<count<<endl;
    
    if(left["RED"] == 0 && left["BLUE"] == 0 && left["GREEN"] == 0)
    {
        //cout<<count<<"|";
        return true;
    }
        
    
    if(boat == "east")
    {
        if(solve(left, p1, "NULL", count+1, "west"))
            return true;
        else
        {
            if(solve(left, "NULL", p2, count+1, "west"))
                return true;
        }    
    }

    if(boat == "west")
    {
        string p_boat = (p1 == "NULL") ? p2: p1;

        for(int i = 0; i < 3; i++)
        {
            string curr_p = all_colors[i];
            if(curr_p != p_boat && left[curr_p] != 0)
            {
                left[curr_p]--;
                if(p1 == "NULL")
                {
                    if(solve(left, curr_p, p2, count+1, "east"))
                        return true;
                }
                if(p2 == "NULL")
                {
                    if(solve(left, p1, curr_p, count+1, "east"))
                        return true;
                }
                left[curr_p]++;
            }
        }
    }

    return false;
}

int main()
{
    unordered_map<string, int> left, right;
    int count = 1;
    left["RED"] = 3;
    left["BLUE"] = 3;
    left["GREEN"] = 3;
    right["RED"] = 0;
    right["BLUE"] = 0;
    right["GREEN"] = 0;

    string p1, p2, boat;
    boat = "east";
    cin>>p1>>p2;
    
    left[p1] -= 1;
    left[p2] -= 1;
    
    bool ans = solve(left, p1, p2, count, boat);
    //cout<<count;
    return 0;

}