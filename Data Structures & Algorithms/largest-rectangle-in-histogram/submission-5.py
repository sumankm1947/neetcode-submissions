class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []
        n = len(heights)

        for i in range(n):
            if i == 0 or not stack:
                stack.append([i, heights[i]])
                continue
            
            # if heights[i] == stack[-1][1]:
            #     continue
            elif heights[i] >= stack[-1][1]:
                stack.append([i, heights[i]])
            else:
                prev_index = 0
                while stack and heights[i] < stack[-1][1]:
                    prev_index, prev_height = stack.pop(-1)

                    new_area = prev_height * (i - prev_index)
                    max_area = max(max_area, new_area)
                    # print(f"height: {heights[prev_index]} area: {new_area}")

                stack.append([prev_index, heights[i]])
            
            # print(stack)

        # print("loop is done")
        for i in range(len(stack)):
            width = n - stack[i][0]

            height = stack[i][1]

            new_area = width * height
            
            max_area = max(max_area, new_area)
            # print(f"height: {height} area: {new_area}")

        
        return max_area
                

            

            
        