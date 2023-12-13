# Classic Pong Game in Python

## Description
This project is a Python implementation of the classic arcade game Pong, one of the earliest arcade video games and a pioneer in the video game industry. The game is a simple simulation of table tennis, featuring simple 2D graphics. It was originally created in the 1970s but continues to be popular due to its foundational role in video gaming history.

In this Python version, the game maintains the essence of the original Pong with a minimalist design using the Turtle graphics library. The game includes two paddles on each side of the screen controlled by players, and a ball that bounces back and forth between these paddles. Each time the ball passes a paddle, the opposing player scores a point. The game is simple yet challenging, requiring quick reflexes and strategic movement.

The project is structured into four main components:
- `main.py`: Initializes the game environment, including the screen, paddles, ball, and scoreboards. This script also contains the main game loop where the game's logic is executed.
- `paddle.py`: Defines the `Paddle` class, responsible for creating paddle objects. This class manages the paddle's appearance and movements.
- `pong_class.py`: Contains the `PONG` class, handling the ball's behavior, including movement, collision detection with walls and paddles, and resetting after scoring.
- `score_board.py`: Implements the `ScoreBoard` class, which is used for displaying and updating the game score.

## Setup
Ensure you have Python installed on your computer (preferably Python 3.x). The Turtle graphics library, which is standard in Python, is used for creating the game's graphical interface.

## Running the Game
To play the game, navigate to the directory containing the game files and run:

```bash
python main.py
```
## Gameplay
- The objective is to hit the ball with your paddle while preventing it from passing by.
- The ball speeds up incrementally, making each successive volley more challenging.
- A point is scored when a player misses the ball.
- The first player to reach 10 points wins the game.

## Controls
- Right paddle: Use the Up and Down arrow keys for vertical movement.
- Left paddle: Use the 'W' and 'S' keys for vertical movement.

## Enjoy the Game!
Relive the nostalgia of the golden age of arcade games with this Python rendition of Pong. It's a great way to understand the basics of game development and enjoy some competitive play.