class Solution:
    def convert(self, s: str, numRows: int) -> str:
        _map = ["" for _ in range(numRows)]
        if numRows == 1:
            return s 

        i = 0
        tour = "D"
        y = 0
        while i < len(s):
            _map[y] += s[i]
            if tour == "D":
                if y == numRows - 1:
                    tour = "U"
                    y -= 1
                else:
                    y += 1
            else:
                if y == 0:
                    tour = "D"
                    y += 1
                else :
                    y -= 1
            
            i += 1
        sol = ""
        for sub_sol in _map:
            sol += sub_sol
        return sol