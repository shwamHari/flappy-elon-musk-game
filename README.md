
# Flappy Elon Musk Game

## Overview

Flappy Elon Musk is a fun and interactive clone of the classic *Flappy Bird* game, where players control Elon Musk, guiding him through obstacles while trying to achieve the highest score. The game features dynamic animations of Elon Musk with a jumping animation that alternates between an open and closed mouth as he moves up and down. The goal is to avoid obstacles, which are Tesla cars and Cybertrucks, and collect points by passing through them.

## Demo


https://github.com/user-attachments/assets/c8e1d871-2092-4822-a932-2c07d342e106


---
## Features

- **Elon Musk Animation**: Animated jumping behavior with an open mouth when going up and a closed mouth when going down.
- **Dynamic Obstacles**: Obstacles include *Tesla cars* and *Cybertrucks*, which the player must navigate through.
- **Score System**: The score increases each time a the player successfully passes a pipe without collision.
- **Game Over Screen**: Displayed when the player crashes, with an option to restart the game by pressing the 'R' key.
- **Welcome Screen**: Featuring a title animation and a jumping Elon Musk before the game starts.
- **Responsive Design**: The game is designed to run at 60 frames per second with smooth animations.

## Installation

### Prerequisites
Ensure you have Python 3.x installed on your machine, along with the following libraries:

- `pygame` (for game logic and graphics rendering)

To install the required dependencies, use the following command:

```bash
pip install pygame
```

### Game Assets

The game uses image files for displaying the character and obstacles. Ensure the following images are available in the `images` folder:

- `elon_closed.png`: Image of Elon Musk with his mouth closed.
- `elon_opened.png`: Image of Elon Musk with his mouth open.
- `cybertruck.png`: Image of the *Cybertruck* (obstacle).
- `model_s.png`: Image of the *Tesla Model S* (obstacle).

### Running the Game

Once the dependencies are installed and the assets are in place, you can start the game by running:

```bash
python src/main.py
```

The game window will open, displaying the welcome screen. Press the **SPACE** key to start the game.

## Game Controls

- **Spacebar**: Makes Elon jump.
- **R**: Restarts the game after a Game Over.

## Game Rules

- Elon Musk automatically falls due to gravity and needs to be controlled by the player by pressing the **SPACE** key to make him jump.
- The player must avoid passing through obstacles (Tesla cars and Cybertrucks); colliding with them will result in a Game Over.
- Each time an obstacle is passed successfully, the score increases by 1.
- The game speed and obstacle generation become increasingly challenging as the player progresses.

## Code Structure

### main.py
- **Main game logic**: Initializes the game, loads images, handles events, controls Elon's jump behavior, and manages obstacle generation.
- **Game loop**: The game runs continuously, checking for events like collisions, and updates the score.

### bird.py
- **Bird class**: Defines Elon's properties, including his position, movement, and image rendering.

### pipe.py
- **Pipe class**: Handles the creation, movement, and collision detection of obstacles (Tesla cars and Cybertrucks).

### utils.py
- **Image loading**: Helper functions for loading and scaling images for the game objects.

### constants.py
- Defines game constants and variables, used in functions and classes throughout the game.

---
<img width="559" alt="Screenshot 2025-01-16 at 8 17 55 PM" src="https://github.com/user-attachments/assets/709af6b5-0574-4c21-9a47-d1aed9cbdc00" />


