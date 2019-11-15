class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        d = collections.defaultdict(lambda :collections.defaultdict(list))
        def get_length_center(i, j):
            x1, y1 = points[i]
            x2, y2 = points[j]
            length = ((x2-x1)**2+(y2-y1)**2)**0.5
            center_x, center_y = (x2+x1)/2, (y2+y1)/2
            return length, (center_x, center_y)
        
        def get_area(ii, jj, length):
            # a, b
            x1, y1 = points[ii[0]]
            x2, y2 = points[jj[0]]
            a = ((x2-x1)**2+(y2-y1)**2)**0.5
            b = (length**2-a**2)**0.5
            return a*b
        
        for idxes in itertools.combinations(range(len(points)), 2):
            i, j = idxes
            length, center = get_length_center(i, j)
            d[length][center].append((i, j))
        res = []
        for length in d:
            candidates = d[length]
            for center in candidates:
                if len(candidates[center])>=2:
                    for idxes in itertools.combinations(range(len(candidates[center])) ,2):
                        ii, jj = idxes
                        area = get_area(candidates[center][ii], candidates[center][jj], length)
                        res.append(area)
        if not res:return 0
        return min(res)
