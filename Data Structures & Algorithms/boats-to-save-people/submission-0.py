class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
       people.sort()
       l = 0
       r = len(people)-1
       numberOfBoats = 0
       while l <= r:
            if l == r:
                numberOfBoats+=1
                break
            if people[r] == limit or people[l] + people[r] > limit:
                numberOfBoats+=1
                r-=1
                continue
            elif people[l] + people[r] <= limit:
                numberOfBoats+=1
                l+=1
                r-=1
                continue
       return numberOfBoats
