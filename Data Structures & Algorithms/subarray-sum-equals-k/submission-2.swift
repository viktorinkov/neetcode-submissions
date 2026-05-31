class Solution {
    func subarraySum(_ nums: [Int], _ k: Int) -> Int {
        var prefix = [Int: Int]()
        var res = 0
        var curSum = 0
        for num in nums{
            curSum += num
            if(curSum == k){
                res += 1
            }
            res += prefix[curSum-k, default: 0]
            prefix[curSum, default: 0] += 1
        }
        return res
    }
}
