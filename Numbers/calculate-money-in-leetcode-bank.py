


# Problem: calculate-money-in-leetcode-bank
# Link: https://leetcode.com/problems/calculate-money-in-leetcode-bank/
# Difficulty: Easy
# Approach:  Simulate the saving process by calculating the total money saved in complete weeks and the remaining days.









class Solution:
    def totalMoney(self, n: int) -> int:
        def giveCost(start,end):
            naturalNumberSum1=(end*(end+1))//2
            naturalNumberSum2=((start-1)*(start))//2
            return naturalNumberSum1-naturalNumberSum2

        def totalWeekCost(weeks):
            totalCost=0
            for x in range(1,weeks+1):
                totalCost+=giveCost(x,x+6)
            return totalCost

        week=n//7
        days=n%7

        money=totalWeekCost(week)
        week+=1
        while days!=0:
            money+=week
            days-=1
            week+=1
        return money
        