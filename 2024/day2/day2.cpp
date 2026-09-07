#include <bits/stdc++.h>
using namespace std;
int main() {
    int ans=0;
    std::ifstream file("day2.test");
    if (!file.is_open()) {
        std::cerr << "Error opening file!" << std::endl;
        return 1;
    }

    // Outer vector = lines | Inner vector = numbers on that line
    // std::vector<std::vector<int>> data; 
    std::string line;
    
    // Read the file line by line
    while (std::getline(file, line)) {
        std::vector<int> nums;
        int gap;
        bool isSafe=true;
        std::stringstream ss(line);
        int number;

        // Parse each number separated by whitespace from the current line
        while (ss >> number) {
            nums.push_back(number);
        }
        cout<<"=========\n";
        for(int i=1;i<nums.size();i++)
        {
            
            
            if(i>1 && abs(gap)<4 && abs(gap)>0) 
            {
                cout<<gap<<"\t"<<nums[i]<<"\n";
                if(((gap<0) && (nums[i]-nums[i-1])>0) ||
                    ((gap>0) && (nums[i]-nums[i-1])<0))   
                {
                    {isSafe=false;cout<<"up and down\n";}
                }

            }
            else if(i>1 && (abs(gap)>3 || abs(gap)==0)) {isSafe=false;cout<<"gap dist too big or small\n";}
            gap=nums[i]-nums[i-1];
            
        }

        // Add the row to our main grid
        // data.push_back(current_line_numbers);
        cout<<"isSafe\t"<<isSafe<<"\n";
        ans+=isSafe;
    }

    file.close();

    cout<<ans<<" ans\n";

    return 0;
}