class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        neg, zero, pos = [], [], []
        for a in A:
            if a > 0:pos.append(a)
            elif a<0:neg.append(-a)
            else:zero.append(a)
        if len(zero)%2!=0:return False
        def check(a):
            if not a:return True
            if len(a)%2!=0:return False
            cnt = collections.Counter(a)
            for k in sorted(cnt.keys()):
                if cnt[k]>0:
                    cnt[2*k] -= cnt[k]
                    if cnt[2*k]<0:return False
            return True        
        return check(neg) and check(pos)
