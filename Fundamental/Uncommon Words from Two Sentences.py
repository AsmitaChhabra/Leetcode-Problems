class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        # Split both sentences into words
        words = (s1 + " " + s2).split()
        
        # Dictionary to count frequency
        count = {}
        for w in words:
            count[w] = count.get(w, 0) + 1 
        
        result = []
        # Using enumerate (though index i is not really needed here)
        for i, (w, c) in enumerate(count.items()):
            print("Index:", i, "Word:", w, "Count:", c)  # just to show
            if c == 1:
                result.append(w)
        
        return result
