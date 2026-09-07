#include <bits/stdc++.h>
using namespace std;
int main() {
    int ans=1;
    std::ifstream file("day3.ip");
    if (!file.is_open()) {
        std::cerr << "Error opening file!" << std::endl;
        return 1;
    }

    // Outer vector = lines | Inner vector = numbers on that line
    // std::vector<std::vector<int>> data; 
    std::string line;
    map<vector<int>,int> mp;
    // Read the file line by line
    while (std::getline(file, line)) {
        
        std::stringstream ss(line);
        char c;
        
        int x=0,y=0,rx=x,ry=y;
        bool santa=false;
        mp[{x,y}]++;
        // Parse each number separated by whitespace from the current line
        while (ss >> c) {
            if(santa)
            {
                if(c=='^')y++;
                else if(c=='v')y--;
                else if(c=='>')x++;
                else if(c=='<')x--;
                if(!mp[{x,y}])
                    {mp[{x,y}]++;ans++;}
            }
            else
            {
                if(c=='^')ry++;
                else if(c=='v')ry--;
                else if(c=='>')rx++;
                else if(c=='<')rx--;
                if(!mp[{rx,ry}])
                    {mp[{rx,ry}]++;ans++;}
            }
            santa=!santa;
        }
    }

    file.close();

    
    cout<<ans<<"\tans\n";
    return 0;
}