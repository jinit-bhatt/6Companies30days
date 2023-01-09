class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bull=0
        cow=0
        ds= defaultdict(lambda:0)
        dg= defaultdict(lambda:0)
        for j in range(len(secret)):
            s=secret[j]
            g=guess[j]
            if(secret[j]==guess[j]):
                bull+=1
                continue
            ds[s]+=1
            dg[g]+=1
        for s in ds:
            if s in dg:
                cow += min(ds[s], dg[s])
        return f'{bull}A{cow}B'
