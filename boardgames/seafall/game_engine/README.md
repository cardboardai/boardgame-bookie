# SeaFallGoZero
In Google's AlphaGo Zero, each potential move available to the program was enumerated and considered by a Monte-Carlo tree search (MCTS). The move probabilities in this search were guided by the neural network. The game engine is being coded with the intent to solve two problems:
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

## Pruning the leaves of an MTCS search tree
It will be interesting to see how many TitanXp GPU hours it will take to train the network and explore all possible moves. However, should the length of training be too long, it may be helpful to eliminate possible moves by labeling a subset as "ineffective". This would require imposing a human bias on the outcome, but is a means to reduce the possibility space if necessary. For example, an ineffective move might be choosing the Soldier's Guild and sailing only, not attempting a raid endeavor, nor taxing.

# Answering rules questions
## Answering if a move is valid
To answer rules questions a test file will be written. The test file will define a before-state and an after-state. The MTCS tree builder will enumerate the possibilities primed by the before-state. A valid move will appear in this enumeration, so a valid move can be phrased as ,*"Is the after-state one of the possibilities output by the game engine when enumerating possible moves from the before-state?"*

## Answering if a rule is correct
Some questions will be answered by pointing to a particular line or block of code, where the logic of the rules has been coded directly.

## Looking at the impact of a rule
Looking at the possible moves from a given before-state could be informative for interpreting a rule.

# Sailing into the unknown
Here are some questions I'd like to answer:
1. How are ships being upgraded after each game?

    I've seen someone in the forums suggest the optimal strategy of upgrading ships to be keeping the two ships together and upgrading the *big* ship only, keeping the small ship only as a support ship. What will the neural network decide?

1. Which guild is the most powerful? When is each guild its most powerful?

    The explorers guild is suggested to be the most powerful guild considering the advantages a player who has invested in exploring receives as the campaign enters into the later stages of SeaFall. Will winning strategies emerge that emphasize each guild? A well balanced 4X game might make each "X" a viable option for victory. Does one guild really rule over the others? If one guild dominates, perhaps it should be nerfed. Answering this question might would help justify the use of machine learning in playtesting a game. Are the winning strategies in the game aligned with the designers' original intent?

1. What happens to the winning strategies if there is no enmity?

    The enmity rules are innovative. Some players love enmity and others not so much. What happens if we train our network to play SeaFall with the rules of enmity removed? Does the game become unbalanced? This question will demonstrate how rules changes can be explored through machine learning. If the rate of learning is fast enough, I can image trying a rules change

# Playtesting with machines
Human playtesting will never be replaced, because how a human feels and responds to playing the game is the whole reason behind designing a game. In other words, the game has to be fun, and the ultimate test is having people play the game and getting their feedback. However, no one likes playing an unfinished game. Machine learning may help bridge the gap between designing the game and getting meaningful playtesting done with a refined version of the game.
