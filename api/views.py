from rest_framework.views import APIView
from rest_framework.response import Response

from typing import List, Tuple
from datetime import datetime
from api.models import RequestLog

def next_element(heights, n):
    st = [-1]
    ans = [0] * n
    for i in range(n - 1, -1, -1):
        curr = heights[i]
        while st[-1] != -1 and heights[st[-1]] >= curr:
            st.pop()
        ans[i] = n if st[-1] == -1 else st[-1]
        st.append(i)
    return ans

def prev_element(heights, n):
    st = [-1]
    ans = [0] * n
    for i in range(n):
        curr = heights[i]
        while st[-1] != -1 and heights[st[-1]] >= curr:
            st.pop()
        ans[i] = st[-1]
        st.append(i)
    return ans

def largest_rectangle_area(heights):
    n = len(heights)
    area = float('-inf')
    next_elem = next_element(heights, n)
    prev_elem = prev_element(heights, n)
    for i in range(n):
        l = heights[i]
        b = next_elem[i] - prev_elem[i] - 1
        new_area = 0 if l == b else l * b
        area = max(area, new_area)
    return area

def solve(matrix):
    row = len(matrix)
    st = set()
    max_col = float('-inf')
    for i in range(row):
        col = len(matrix[i])
        max_col = max(max_col, col)
        for j in range(col):
            st.add(matrix[i][j])

    maxi = float('-inf')
    max_num = 0
    for num in st:
        histogram = [0] * max_col
        for i in range(row):
            col = len(matrix[i])
            j = 0
            while j < col:
                if matrix[i][j] == num:
                    histogram[j] += 1
                else:
                    histogram[j] = 0
                j += 1
            while j < max_col:
                histogram[j] = 0
                j += 1
            if largest_rectangle_area(histogram) > maxi:
                maxi = largest_rectangle_area(histogram)
                max_num = num
    return maxi, max_num



class find_largest(APIView): 
    def post(self, request):
        start_time = datetime.now()

        matrix = request.data.get('matrix', [])

        if not matrix:
          return Response({"error": "Matrix is required in the request."}, status=400)

        try:
          result = solve(matrix)
          response_data = {"area": result[0], "number": result[1]}
          response = Response(response_data)
        except Exception as e:
          response_data = {"error": str(e)}
          response = Response(response_data, status=500)

        end_time = datetime.now()
        turnaround_time = (end_time - start_time).total_seconds()

    # Log the request and response
        log_entry = RequestLog(
          request_data=request.data,
          response_data=response_data,
          turnaround_time=turnaround_time
        )
        log_entry.save()
        return response