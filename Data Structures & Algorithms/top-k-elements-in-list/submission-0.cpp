class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        
       //have a map of the frequencies of the nums
       unordered_map<int, int> frequencies; 

        //go through the array
        for(int i = 0; i < nums.size(); i++)
        {
            frequencies[nums[i]]++;
        }

        vector<pair<int,int>> vec(frequencies.begin(), frequencies.end());

        sort(vec.begin(), vec.end(), [](pair<int,int> a, pair<int,int>b){
            return a.second > b.second;
        });


        vector<int> result;

        for(int i = 0; i < k; i++)
        {
            result.push_back(vec[i].first);
        }

        return result;

    }
};
