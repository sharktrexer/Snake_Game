# Mr Snake's Insatiable Appetite
A pixel based snake game set in a small window. You move a snake around using WASD or the arrow keys. Every fruit you eat grows your snake by 1 square and increases your score by 5.
After every 50 points scored, an additional fruit will spawn on the screen, up to 10. There are different types of fruit to consume, including:
- __Purple__: Basic, no special effect.
- __Blue__: Double Score, worth double points.
- __Pink__: Shrink, snake becomes 1 square smaller.
- __Cyan__: Speed Up, snake moves faster.
- __Orange__: Speed Down, snake moves a little slower.
- __Red__: Grow, snake grows twice as much.
- __Rainbow__: Party, temporarily gain a big speed boost, double score, and fun effects!
  - __NOTE__: Fun effects do NOT include flashing colors, simply a color palette swap.
  
Try to get the highest score possible!

### Instructions
1. To run you need to download python [here](https://www.python.org/downloads)
__AND__ pygame [here](https://www.pygame.org/wiki/GettingStarted)

2. Download _Mr_Snake_Game.py_ and snake.ico and place in an approriate folder.
3. Open a command prompt and change to the directory of the folder.
4. Use this command to start the game:
   
    `python Mr_Snake_Game.py`

### Screenshots:
![snake game](https://github.com/user-attachments/assets/fd411cab-6889-4d20-be45-422cc7df95e6)
![rainbowsnake](https://github.com/user-attachments/assets/bc3cbcc2-b5c9-440f-b79e-a98becaa9abc)


### Known Bugs:
- Pressing 2 keys at once can make the snake reverse it's direction, causing non-intended game overs.
- Sometimes fruits spawn on top of each other or on the snake
