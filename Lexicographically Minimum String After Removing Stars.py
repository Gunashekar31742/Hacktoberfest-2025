class Solution:
    def clearStars(self, s):
        from collections import defaultdict

        stacks = defaultdict(list)
        result = []

        for i, ch in enumerate(s):
            if ch != '*':
                result.append(ch)
                stacks[ch].append(len(result) - 1)
            else:
                for c in map(chr, range(ord('a'), ord('z') + 1)):
                    if stacks[c]:
                        idx = stacks[c].pop()
                        result[idx] = None
                        break
        return ''.join(ch for ch in result if ch is not None)
