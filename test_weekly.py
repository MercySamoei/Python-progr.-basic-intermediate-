import unittest
import random

class TestSnake_ladders(unittest.TestCase):

    def test_numberoption(self):
        self.options = range(1, 7)
        for i in self.options:
            return i
        self.result = random.i
        self.assertIn(self.result, i) 


    def test_swallowed(self):
        digits = {17:7, 54:34, 62:19, 64:29, 87:36, 93:73, 95:65, 98:49}
        start_point = digits.keys()
        end_point = digits.values()
        self.assertEqual(start_point, end_point)

    def test_lifted(self):
        ladder = {1:38, 4:14, 9:31, 21:42, 28:84, 51:67, 72:91, 80:99}
        self.options = ladder.keys()      
        self.result = ladder.values()
        self.assertEqual(self.options, self.result)

if __name__=='__main__':
    unittest.main()



    def test_swallowed(self):
        # Set up a snake at position 17 with end position 7
        snakes = {17: 7}
        # Set the player's current position to 17
        current_position = 17
        # Call the move_player method with a roll of 6
        new_position = current_position + 6
        if new_position in snakes:
            # If the new position is the head of a snake, move the player to the end of the snake
            current_position = snakes[new_position]
        else:
            # Otherwise, move the player to the new position
            current_position = new_position
        # Assert that the player's position is now 7 (the end of the snake)
        self.assertEqual(current_position, 7)

    