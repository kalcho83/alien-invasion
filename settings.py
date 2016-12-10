# Author: Bojan G. Kalicanin
# Date: 09-Dec-2016
# Settings module stores all the game settings

class Settings(object):
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen Settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # Ship settings.
        self.ship_speed_factor = 1.5