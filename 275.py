def hIndex_bi(citations):
    xitations.reverse()
    low, high = 1, len(citations)
    while low <= high:
        mid = (low + high) / 2
        if mid == citations[mid-1]:
            return mid
        elif mid < citations[mid-1]:
            low = mid + 1
        else:
            high = mid - 1
    return low-1
# C++
# class Solution {
# public:
#     int hIndex(vector<int>& citations) {
#         int n = citations.size();
#         int left = 0;
#         int right = n-1;
        
#         while(left <= right){
#             int mid = left + (right - left)/2 ;
#             if (citations[mid] >= n-mid){
#                 right = mid - 1;
#             }
#             else{
#                 left = mid + 1;
#             }
#         }
#         return n-left;
#     }
# };
