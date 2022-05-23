class Solution:
    def convert(self, s: str, numRows: int) -> str:
        temp_val1 = list(s)
        temp_val2 = ""
        marker = 0
        for x in range(numRows):
            counter = numRows-x-1
            while 0 in temp_val1:
                temp_val1.remove(0)
            #print(temp_val1)
            #print(temp_val2.replace("0",""))
            for y in range(len(temp_val1)):
                if marker < len(temp_val1):
                    if x == 0:
                        temp_val2+=str(temp_val1[marker])
                        temp_val1[marker] = 0
                        marker+=counter+counter
                    else:
                        temp_val2+=str(temp_val1[marker])
                        temp_val1[marker] = 0
                        if marker==0:
                            marker+=counter+counter
                            continue
                        else:
                            if marker+1 < len(temp_val1):
                                temp_val2+=str(temp_val1[marker+1])
                                temp_val1[marker+1] = 0
                                marker+=counter+counter+1
                            else:
                                marker = 0
                else:
                    marker = 0
        for x in temp_val1:
            if x == 0:
                continue
            else:
                temp_val2+=x
        temp_val2 = temp_val2.replace("0","")
        return temp_val2

    
# 813 / 1157 test cases passed.

# Input:
# "Apalindromeisaword,phrase,number,orothersequenceofunitsthatcanbereadthesamewayineitherdirection,withgeneralallowancesforadjustmentstopunctuationandworddividers."
# 4

# Output:
# "Ads,eetqosaaaiecwnlcamouadenddirspnriadps,broheuefttcnedsmynhret,ieealnerdtetptanrdaioewrhanm,resecuihtbrteeaetdrintgrloasojsnsuctowvilmoruornnaehwiiohawfutnio."

# Expected: "Ads,eetqosaaaiecwnlcamouadepnriadps,broheuefttcnedsmynhret,ieealnerdtetptannrddraioewrhanm,resecuihtbrteeaetdrintgrloasojsnsuctodoiislmoruornnaehwiiohawfutniwv."
