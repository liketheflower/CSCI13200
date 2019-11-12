class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        cnt = collections.Counter(A)
        if cnt[0]%2!=0:return False
        for k in sorted(cnt.keys(), key=abs):
            if cnt[k] > 0:
                cnt[2*k] = cnt[2*k] - cnt[k]
                if cnt[2*k]<0:return False
        return True
