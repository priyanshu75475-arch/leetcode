class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        triangle = []
        
        for i in range(numRows):
            # Create a row of '1's with a length equal to (i + 1)
            row = [1] * (i + 1)
            
            # Fill in the internal values (ignoring the first and last element)
            for j in range(1, i):
                # Sum the two elements directly above it from the previous row
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
                
            triangle.append(row)
            
        return triangle