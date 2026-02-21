
class Solution(object):
    def getHint(self, secret, guess):
        bulls = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
        total_matches = 0
        for d in "0123456789":
            total_matches += min(secret.count(d), guess.count(d))
        cows = total_matches - bulls
        return str(bulls) + "A" + str(cows) + "B"

if __name__ == "__main__":
    s = Solution()
    print(s.getHint("1123", "0111")) 