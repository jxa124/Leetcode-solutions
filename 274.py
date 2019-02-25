def hIndex(citaions):
    if citaions == [] or citations ==[0]:
        return 0
    citaions.sort()
    citaions.reverse()
    for h,c in enumerate(citaions):
        if h+1 > c:
            return h
    return len(citaions)

# C++解法
# class Solution {
# public:
#     int hIndex(vector<int>& citations) {
#         std:sort(citations.begin(), citations.end());
#         int n  = citations.size();
#         int index = 0;
#         for(int i = n-1;i>=0;i--){
#             index++;
#             if(index > citations[i]){
#                 return index-1;
#             }
#         }
#         return n;
        
#     }
# };
