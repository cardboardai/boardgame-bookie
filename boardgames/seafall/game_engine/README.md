# SeaFallGoZero
In Google's AlphaGo Zero, each potential move available to the program was enumerated and considered by a Monte-Carlo tree search (MCTS). The move probabilities in this search were guided by the neural network. The game engine is being coded with the intent to solve two problems:
1. To clear up ambiguous rules and legal moves.
2. To test for dominant strategies through training a neural network to play SeaFall.

Towards these ends, the game engine will encode the rules of SeaFall, store the state of a game, and enumerate the possible moves required to evaluate an MTCS search.

# Encoding the rules of SeaFall
A defining quality of legacy boardgames is that the rules and components will change over the course of a campaign. A campaign is a series of games played by the same group of players until an ultimate winner is decided. The SeaFall campaign progresses as players reach milestones. When encoding the rules of SeaFall the program should recognize, which milestones have been reached and therefore which rules are currently being applied to the game.

## Randomizing secret society membership
In SeaFall, a secret society is revealed and the search for society members among the advisors becomes an important game mechanic, espeically those with knowledge of the island at the end of the world. However, in the published version of the game the society members are the same in every copy of the game. An AI will these identities through repeated play, but we do not want strategies that take advantage of this knowledge from simulated campaign to simulated campaign. Therefore, the society member identities, and those advisors with chart symbols, will be randomly assigned before each simulation, except for advisors with public membership.

# Storing the state of the game
The state of the game will record the location of islands and players' ships on the hex grid that defines the world of SeaFall. Furthermore, the state of the game records all components relevant to players including province stats, structures, ship upgrades, currency, etc.

# Enumerating the possibilities in an MTCS search
Given the state of the game, the turn order of players, and the last turn made by a player, the game engine will produce all the possibilities available to the current player. Any turn that involves an endeavor will not include its outcome in the possibility, only the fact that an endeavor will take place. If a possibility with an endeavor is chosen, then rolling a dice pool will be simulated and the result will update the state of the game before the next iteration of the MTCS search.

The number of possibilities is greatly expanded by the option to acquire and play an advisor on any given turn. When a dice pool is being resolved, the option to use fortune tokens, exhaust upgrades, and take damage will be resolved by having that player "take another turn" by iterating the MTCS search again.

## Pruning the leaves of an MTCS search tree
It will be interesting to see how many TitanXp GPU hours it will take to train the network and explore all possible moves. Perhaps it would take 1000 years to train! Should the length of training be too long, it may be helpful to eliminate possible moves by labeling a subset as "ineffective". This would require imposing a human bias on the outcome, but is a means to reduce the possibility space if necessary. For example, an ineffective move might be choosing the Soldier's Guild and sailing only, not attempting a raid endeavor, nor taxing.

Another approach to reduce training time would be to focus on a smaller portion of the game, such as the prologue. Training an AI to solve a "toy" version of a game, i.e. smaller board and fewer components, or a specific scenario in a game could still prove to be informative to the larger design.

# Answering rules questions
## Answering if a move is valid
To answer rules questions a test file will be written. The test file will define a before-state and an after-state. The MTCS tree builder will enumerate the possibilities primed by the before-state. A valid move will appear in this enumeration, so a valid move can be phrased as ,*"Is the after-state one of the possibilities output by the game engine when enumerating possible moves from the before-state?"*

## Answering if a rule is correct
Some questions will be answered by pointing to a particular line or block of code, where the logic of the rules has been coded directly.

## Looking at the impact of a rule
Looking at the possible moves from a given before-state could be informative for interpreting a rule.

# Sailing into the unknown
Here are some questions I'd like to answer:
1. What is the average length of a game? Given a desired game length, how can glory and coin costs be adjusted to reach that game length?

    A common critique of SeaFall is that the game seems like it was designed to last 2 rounds, i.e. 2 full years and sometimes past 3 winters. However, game length as reported on the forum tend to average a little over 1 round, about 7-9 turns. This game is unsatisfying for 2 primary reasons: 1) Reaching winter is fun! An influx of coin and a refreshed advisor pool opens up many possible moves and feels like the investment of time into that game starts paying off. Fewer winters means less fun. 2) The end of the game comes suddenly, because of large glory payouts that push someone past the glory threshold for that game. The suddenness often does not allow a player to react at all if they've already taken their turn, and even if you get to take a turn after knowing the game will end, often there aren't great options available, especially during the colony phase of the game where it takes several turns to found a colony.

    Becq and others on the forum have suggested reducing glory for milestones and tomb endeavors. They've also suggested reducing the turns in a round to increase the frequency of winters. To answer the second question, after the AI strategies have been established, another network could optimize the glory and coin cost values with a cost function that optimizes an ideal length of gameplay.

1. How are ships being upgraded after each game?

    I've seen someone in the forums suggest the optimal strategy of upgrading ships to be keeping the two ships together and upgrading the *big* ship only, keeping the small ship only as a support ship. What will the neural network decide? If the permanent support ship idea is indeed dominant, would it be more fun to have incentives to diversify your ship? For example, any upgrade could come at a cost making it impossible to have an uber-ship, e.g. upgrading raid could come at the cost of reducing exploration. Another example of power balance could be adding a coin activation cost to endeavors with a ship, i.e. the number of upgrades given to a ship increases the cost to use it; thematically this could be explained by having a larger more expensive crew, or a larger upkeep cost to maintain the skill of the ship.

1. Which guild is the most powerful? When is each guild its most powerful?

    The explorers guild is suggested to be the most powerful guild considering the advantages a player who has invested in exploring receives as the campaign enters into the later stages of SeaFall. Will winning strategies emerge that emphasize each guild? A well balanced 4X game might make each "X" a viable option for victory. Does one guild really rule over the others? If one guild dominates, perhaps it should be nerfed. Answering this question might would help justify the use of machine learning in playtesting a game. Are the winning strategies in the game aligned with the designers' original intent?

1. What happens to the winning strategies if there is no enmity?

    The enmity rules are innovative. Some players love enmity and others not so much. What happens if we train our network to play SeaFall with the rules of enmity removed? Does the game become unbalanced? This question will demonstrate how rules changes can be explored through machine learning. If the rate of learning is fast enough, I can image trying a rules change

1. Is there a "hard mode" or "SeaFall+" mode that is more challenging?

    What happens to strategies if we crank up the difficulty for endeavors? Do the same strategies still work? Does the merchant and builder become more essential?

1. Who is on the advisor most wanted list?

    For any dominant strategy, when a province is raided to take an advisor, who are those advisors? What is the length of this list? Can a threshold of value be determined? Which of the retired advisor upgrades appear most often?

1. Where are the islands placed?

    I get the sense that the placement of island stickers is on average in the center of each row. What is the distribution of island placement revealed through simulation? Is it more fun to have islands with a greater distribution across the board?

1. Are there interesting treasure strategies?

    Treasures on the surface appear to be a last resort for any supplies and goods that cannot be spent on other means. There are several disadvantages to treasure: they are dead-ends and serve no purpose other than to convert gold and supplies to glory (as opposed to a structure or upgrade that have additional abilities); they aren't useful in the early game, especially since buying treasure blocks the purchase of advisors; and large treasures are difficult, because of their high gold cost. How often are treasures purchased? When are they purchased?

# Playtesting with machines
Human playtesting will never be replaced, because how a human feels and responds to playing the game is the whole reason behind designing a game. In other words, the game has to be fun, and the ultimate test is having people play the game and getting their feedback. However, no one likes playing an unfinished game. Machine learning may help bridge the gap between designing the game and getting meaningful playtesting done with a refined version of the game.

# Design Notes
1. Make the components first. All nouns, so to speak.
