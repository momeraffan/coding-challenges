class Solution:
    def convert(self, s: str, numRows: int) -> str:
        temp_val1 = list(s)
        temp_val2 = ""
        marker = 0
        for x in range(numRows):
            counter = numRows-x-1
            if 0 in temp_val1:
                while True:
                    try:
                        while True:
                            temp_val1.remove(0)
                    except ValueError:
                        pass
            else:
                for y in range(len(temp_val1)):
                    if marker < len(s):
                        temp_val2+=str(temp_val1[marker])
                        temp_val1[marker] = 0
                        marker+=counter+counter
                    else:
                        marker = 0
        print(temp_val2)
