## player.py

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self._score = 0  # 私有变量，用于存储玩家得分

    def update_score(self, points: int) -> None:
        """更新玩家的得分。

        Args:
            points (int): 要增加的分数。
        """
        self._score += points

    def get_score(self) -> int:
        """获取玩家当前的得分。

        Returns:
            int: 玩家的得分。
        """
        return self._score
