import arcade
import pathlib

class Platformer(arcade.Window): # Class used to run game
    def __init__(self): # initializes the game object, add code for actions when game starts
        pass

    def setup(self): # Sets up game to begin, add code to this method if repeats (initialize new levels on success or reset on failure)
        """Sets up the game for the current level"""
        pass

    def on_key_press(self, key: int, modifiers: int): # Arcade processes key press and release seperatley, helps avoid auto=repeat
        """Processes key presses

        Arguments:
            key {int} -- Which key was pressed
            modifiers {int} -- Which modifiers were down at the time
        """

    def on_key_release(self, key: int, modifiers: int):
        """Processes key releases

        Arguments:
            key {int} -- Which key was released
            modifiers {int} -- Which modifiers were down at the time
        """

    def on_update(self, delta_time: float): #where update state of game and all objects, collissions between objects, sound effects played, scores updated, sprites animated etc,
        """Updates the position of all game objects

        Arguments:
            delta_time {float} -- How much time since the last call
        """
        pass

    def on_draw(self): #where everything displayed in your game is drawn
        pass

#if __name__ == "__main__": #define main entry point for game
    #window = Platformer()
    #window.setup()
    #arcade.run()
    #start game loop