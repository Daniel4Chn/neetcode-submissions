class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        

        # take last digit and then add 1 and while that digit == 10, make that digit 0 and go to the next digit and add 1 to it and if it goes to the very last digit, turn it 0 and add a new digit 
        carryValue = 0
        for r in range(len(digits)-1,-1,-1):

            if r == len(digits)-1:
                digits[r] +=1
                if digits[r] == 10:
                    carryValue = 1
                    digits[r] = 0
                    continue
                else:
                    return digits

            if carryValue == 1:
                digits[r] = digits[r] + carryValue
                carryValue = 0
                if digits[r] == 10:
                    carryValue = 1
                    digits[r] = 0
                    continue
                else:
                    return digits

        if digits[0] == 0:
            digits[0] = 0
            digits.insert(0,1)
        return digits