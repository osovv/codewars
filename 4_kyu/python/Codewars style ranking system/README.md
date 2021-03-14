# Codewars style ranking system
### Small task description
Write a class called User that is used to calculate the amount that a user will progress through a ranking system similar to the one Codewars uses.

### Link to Kata:
[link](https://www.codewars.com/kata/51fda2d95d6efda45e00004e)

### Comment
It's not a difficult task at all, you just have to be aware of all the possible scenarios.

### Top voted soltuion:
```
class User ():    
    def __init__ (self):
        self.RANKS = [-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8]
        self.rank = -8
        self.rank_index = 0
        self.progress = 0
        
    def inc_progress (self, rank):
        rank_index = self.RANKS.index(rank)
        
        if rank_index == self.rank_index:
            self.progress += 3
        elif rank_index == self.rank_index - 1:
            self.progress += 1
        elif rank_index > self.rank_index:
            difference = rank_index - self.rank_index
            self.progress += 10 * difference * difference
            
        while self.progress >= 100:
            self.rank_index += 1
            self.rank = self.RANKS[self.rank_index]
            self.progress -= 100    
        
        if self.rank == 8:
            self.progress = 0
            return
```
