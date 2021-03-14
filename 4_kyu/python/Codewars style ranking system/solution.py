class User:
    def __init__(self):
        self.rank = -8
        self.progress = 0
    def inc_progress(self, level_rank):
        if level_rank < -8 or level_rank == 0 or level_rank > 8:
            raise ValueError
        d = level_rank - self.rank
        if level_rank > 0 and self.rank < 0:
            d -= 1
        points_made = 10 * d * d
        if d == 0:
            points_made = 3
        if d == -1:
            points_made = 1
        if d < -1:
            points_made = 0
        if level_rank == -1 and self.rank == 1:
            points_made = 1
        if level_rank == 1 and self.rank == -1:
            points_made = 10
        self.progress += points_made
        new_rank = self.rank + int(self.progress / 100)
        if new_rank > 0 and self.rank < 0:
            self.rank = new_rank + 1
        else:
            self.rank = new_rank
        self.progress = self.progress % 100
        self.rank = min(self.rank, 8)
        if self.rank == 0:
            self.rank = 1
        if self.rank == 8:
            self.progress = 0
