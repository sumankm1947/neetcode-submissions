class Solution:

    def encode(self, strs: List[str]) -> str:
        final_string = ""
        for string in strs:
            length = len(string)
            final_string += str(length) + "#" + string
        print(final_string)
        return final_string

    def decode(self, s: str) -> List[str]:
        final_list = []
        index = 0
        while True:
            if index >= len(s):
                break
            startindex = index
            endindex = index
            
            while endindex < len(s) and s[endindex].isdigit():
                endindex += 1
            # if s[endindex + 1] == "#":
            # print(s[startindex: endindex])
            length = int(s[startindex: endindex])
            index = endindex + 1
            final_list.append(s[index: index+length])
            index += length



        print(final_list)
        return final_list
