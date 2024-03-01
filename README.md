<h1>Python Choose Your Own Adventure Game</h1>

<b>Date completed:</b> December 11, 2023 - January 26, 2024

<h2>Description</h2>
This project used Python to create an interactive text-based Choose Your Own Adventure game with three different endings.  The script utilised functions, dictionaries, loops, randomisation and recursive calls to implement the game's logic.
<br>
<br>
This was completed as part of my final year group project for the Linguistic Computations module, scoring 72% (First-class). 

<h2>Project Details</h2>
This game project allows players to make decisions that impact the progression of the story. The adventure includes multiple obstacles, each requiring players to make choices, including choosing weapons, that lead to different obstacles and outcomes.
<br>
<br>
<h3>Key components:</h3>
<br>

**1. Global variables**
  - `chosen_weapon`: A global variable to store the player's chosen weapon throughout the script.

**2. Typewriter effect functions**
  - `typingWrite(text)`: Simulates a typewriter effect for displaying text.
  - `typingInput(text)`: Combines the typewriter effect with user input.

**3. Screen clearing**
  - `clearScreen()`: Clears the console screen when game has ended.

**4. General restart function**
  - `General_Restart()`: A recursive call asking the player if they want to restart the game after a failure or a specific point. Handles variation of responses.

**5. Adventure logic**
  - `start_adventure(playerName)`: Initiates the adventure, presenting the player with choices to enter the castle's armory and select a weapon.
  - randomised elements: The script includes random elements, such as the troll's number and the choice of how the troll reacts.

<h2>Remarks</h2>

- Organise the code into classes and methods for better structure and readability.
- Add comments to explain the purpose and functionality of each function and section of the code.
- Use input validation to handle unexpected user inputs.
