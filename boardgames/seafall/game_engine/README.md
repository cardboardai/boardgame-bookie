# SeaFallGo
In Google's AlphaGo, each potential move available to the program was enumerated and considered by a Monte-Carlo tree search (MCTS). The move probabilities in this search were guided by the neural network. The game engine is being coded with the intent to solve two problems:
1. To clear up ambiguous rules and legal moves.
2. To test for dominant strategies through training a neural network to play SeaFall.

Towards these ends, the game engine will encode the rules of SeaFall, store the state of a game, and enumerate the possible moves required to evaluate an MTCS search.

# Encoding the rules of SeaFall
A defining quality of legacy boardgames is that the rules and components will change over the course of a campaign. A campaign is a series of games played by the same group of players until an ultimate winner is decided. The SeaFall campaign progresses as players reach milestones. When encoding the rules of SeaFall the program should recognize, which milestones have been reached and therefore which rules are currently being applied to the game.

# Storing the state of the game
The state of the game will record the location of islands and players' ships on the hex grid that defines the world of SeaFall. Furthermore, the state of the game records all components relevant to players including province stats, structures, ship upgrades, currency, etc.

# Enumerating the possibilities in an MTCS search
Given the state of the game, the turn order of players, and the last turn made by a player, the game engine will produce all the possibilities available to the current player. Any turn that involves an endeavor will not include its outcome in the possibility, only the fact that an endeavor will take place. If a possibility with an endeavor is chosen, then rolling a dice pool will be simulated and the result will update the state of the game before the next iteration of the MTCS search.

The number of possibilities is greatly expanded by the option to acquire and play an advisor on any given turn. When a dice pool is being resolved, the option to use fortune tokens, exhaust upgrades, and take damage will be resolved by having that player "take another turn" by iterating the MTCS search again.

# Answering rules questions

## Answering if a move is valid
To answer rules questions a test file will be written. The test file will define a before-state and an after-state. The MTCS tree builder will enumerate the possibilities primed by the before-state. A valid move will appear in this enumeration, so a valid move can be phrased as *Is the after-state one of the possibilities output by the game engine when enumerating possible moves from the before-state*

## Answering if a rule is correct
Some questions will be answered by pointing to a particular line or block of code, where the logic of the rules has been coded directly.
