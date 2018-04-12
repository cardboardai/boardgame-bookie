# Stage 1
The prologue and the games the take place before opening the any boxes are considered stage 1.

# Ship Damage Probability
Should I roll the dice? This notebook introduces the probabilities that will help Seafall players make that decision.

## Counting the outcomes of dice rolls
Dice rolls can be [framed](http://math.stackexchange.com/questions/900672/how-many-combinations-from-rolling-5-identical-dice) as [stars and bars](http://math.stackexchange.com/questions/208377/combination-with-repetitions) problems. This is a clever way to frame the combinatorics of dice rolling. The combination formula is used to choose the location of the bars, whose position determines how many dice show a particular face. The stars between the bars represent the number of dice showing a particular face; the identity of that face is determined by how many bars are to the right (or left) of the star(s). If two bars are adjacent that means there aren't any dice showing the particular face defined by the position between those bars.

\begin{equation}\text{unique dice combinations} = \binom{n - 1 + k}{n - 1}\end{equation}

\begin{equation}n = \text{the number of faces on a die}\end{equation}

\begin{equation}k = \text{the size of the dice pool}\end{equation}

*Note that all dice in the pool must be identical. Unless otherwise stated, it is assumed that the dice pool consists of identical dice.*

### The combination formula is essential
The combination formula will again prove useful for counting outcomes when considering only two possibilities. In Seafall, often it only matters whether the face of a die is blank or not. In these cases, the combination formula can be used to count the outcomes by enumerating the ways a pool of dice can be divided into two sets. From a given dice pool choose a given number of dice to be part of the *blank* set; since there are only two sets this means the remaining dice are part of the *success* set.

\begin{equation}\text{unique dice combinations} = \binom{n}{k}\end{equation}

\begin{equation}n = \text{the size of the dice pool}\end{equation}

\begin{equation}k = \text{the number of blanks}\end{equation}

Looking ahead, when there are more than two outcomes we'll need the multinomial coefficient formula, which reduces to the combination formula when there is only two outcomes. The multinomial formula comes into play during more complex situations encountered in Seafall. For the most common encounters on the high seas we'll be using [combinations](https://en.wikipedia.org/wiki/Combination) to do the heavy lifting for our calculations.
