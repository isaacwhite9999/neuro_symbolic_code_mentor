# neuro_symbolic_code_mentor/reinforcement.py

class RLAgent:
    """
    A simple reinforcement learning agent that adjusts suggestion weights based on user feedback.
    """
    def __init__(self, num_patterns: int):
        # Initialize weights for each pattern (all start at 1.0)
        self.weights = [1.0 for _ in range(num_patterns)]
        self.alpha = 0.1  # Learning rate

    def update(self, pattern_index: int, reward: float):
        """
        Update the weight for a given pattern based on the reward.
        
        Parameters:
            pattern_index (int): The index of the pattern.
            reward (float): Feedback from user (1 = good, 0 = bad).
        """
        self.weights[pattern_index] = self.weights[pattern_index] + self.alpha * (reward - self.weights[pattern_index])

    def get_weight(self, pattern_index: int) -> float:
        """
        Retrieve the current weight for a given pattern.
        """
        return self.weights[pattern_index]
