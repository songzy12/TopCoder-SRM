## RandomPancakeStack

SRM 656 - Div 1 Level 1

### Problem Statement Summary

You have $N$ pancakes numbered $0$ to $N-1$. Pancake $i$ has width $i + 1$ and a given deliciousness value `d[i]`.

All pancake widths are distinct, so every subsequent choice is either narrower or wider than the current top pancake.

You construct a stack of pancakes one by one:

1. In the first step, choose one of the $N$ pancakes uniformly at random and place it on the plate.
2. In each subsequent step, choose one of the **remaining** pancakes uniformly at random.
3. If the chosen pancake's width is **strictly smaller** than the width of the top pancake on the stack, place it on top of the stack and receive deliciousness equal to its `d[i]`.
4. If the chosen pancake's width is **larger** than the top pancake on the stack, the process **stops immediately** (the pancake is not placed, and no more pancakes are added).

**Goal:** Return the **expected value** of the total deliciousness of the stack.

### Constraints

* $N$ (number of pancakes) is between $1$ and $250$.
* `d` contains exactly $N$ elements, each between $1$ and $1,000$.

## Solutions

### 1. Permutation Traversal - O(N \times N!)

Since the pancake choices are made uniformly at random, every permutation of the $N$ pancakes represents a distinct, equally likely order in which pancakes are drawn from the bag.

For $N \le 10$, there are $10! = 3,628,800$ permutations, which is manageable for a brute-force check.

#### Algorithm

1. Generate all $N!$ permutations of the indices $\{0, 1, \dots, N-1\}$.
2. For each permutation, simulate the process sequentially:
	* Keep track of the current top pancake's width.
	* If the drawn pancake is smaller than the top pancake, add its deliciousness and update the top width.
	* If the drawn pancake is larger than the top pancake, stop processing that permutation.
3. Average the total deliciousness over all permutations.

This method is useful for small inputs or as a reference implementation for testing the more efficient solutions.

#### Complexity

* **Time Complexity:** $\mathcal{O}(N \times N!)$.
* **Space Complexity:** $\mathcal{O}(N)$.

### 2. Recursive Backtracking / DFS - O(N!)

Instead of explicitly generating full permutations, recursively choose the next unused pancake. A branch ends as soon as a pancake wider than the current top is selected.

#### Algorithm

1. Define a recursive function that tracks the unused pancakes and the current top pancake.
2. If $m$ pancakes remain, each possible next choice has probability $1/m$.
3. For each remaining pancake narrower than the current top, add its deliciousness and recurse.
4. A wider choice contributes zero and ends that branch immediately.

#### Complexity

* **Time Complexity:** $\mathcal{O}(N!)$ in the worst case.
* **Space Complexity:** $\mathcal{O}(N)$ for the recursion stack.

### 3. Dynamic Programming - O(N^3)

Since accepted pancakes must have strictly decreasing widths, dynamic programming can avoid exploring every permutation. The following state records the current top pancake and the number of pancakes already used.

#### DP State

Let $\text{dp}[i][j]$ be the expected total deliciousness gained from the remaining choices, given that:

* $i$ is the width index of the pancake currently on top of the stack (0-indexed, where width is $i+1$).
* $j$ is the number of pancakes already tried/used so far.

Since we start with an empty stack, $N$ pancakes are initially available.

#### State Transitions

When there are $j$ pancakes already used, there are $N - j$ remaining pancakes to choose from, each selected with probability $\frac{1}{N - j}$.

From the remaining available pancakes:

* **Valid choices:** Any remaining pancake with width index $k < i$. If chosen, we gain $d[k]$ and transition to state $\text{dp}[k][j + 1]$.
* **Invalid choices:** Any remaining pancake with width index $k > i$. Choosing one immediately terminates the process (adds $0$).

Therefore, the recurrence relation for $\text{dp}[i][j]$ is:

$$\text{dp}[i][j] = \frac{1}{N - j} \sum_{k = 0}^{i - 1} \Big( d[k] + \text{dp}[k][j + 1] \Big)$$

#### Base Cases

* If $j = N$, no pancakes remain, so $\text{dp}[i][N] = 0$.
* If $i = 0$, the top pancake has width $1$ (the smallest possible). Any remaining pancake chosen will be larger, terminating the process, so $\text{dp}[0][j] = 0$.

#### Initial Call / Final Result

Before any pancake is placed, we pick the first pancake uniformly at random out of $N$ choices. Any choice $k \in [0, N-1]$ is valid as the base of the stack:

$$\text{Expected Deliciousness} = \frac{1}{N} \sum_{k=0}^{N-1} \Big( d[k] + \text{dp}[k][1] \Big)$$

#### Complexity

* **Time Complexity:** $\mathcal{O}(N^3)$ — 3 nested loops ($j$, $i$, and $k$). Given $N \le 250$, $250^3 \approx 1.5 \times 10^7$ operations, easily running within the 2.0-second time limit.
* **Space Complexity:** $\mathcal{O}(N^2)$ for the DP table.

### 4. Optimized DP - O(N^2)

To optimize the DP solution from $\mathcal{O}(N^3)$ to $\mathcal{O}(N^2)$, we eliminate the innermost loop ($k$) by maintaining a **running sum**.

#### Key Insight

Recall the recurrence relation from the $\mathcal{O}(N^3)$ approach:

$$\text{dp}[i][j] = \frac{1}{N - j} \sum_{k = 0}^{i - 1} \Big( d[k] + \text{dp}[k][j + 1] \Big)$$

Notice what happens when we look at the sum inside for $i$ vs. $i + 1$:

* For index $i$: $\quad \text{Sum}(i) = \sum_{k=0}^{i-1} \Big( d[k] + \text{dp}[k][j+1] \Big)$
* For index $i+1$: $\text{Sum}(i+1) = \sum_{k=0}^{i} \Big( d[k] + \text{dp}[k][j+1] \Big) = \text{Sum}(i) + \Big( d[i] + \text{dp}[i][j+1] \Big)$

Instead of recomputing the sum from $k = 0$ to $i - 1$ every single time in $\mathcal{O}(N)$, we can maintain `sum` as we iterate $i$ from $0$ up to $N - 1$.

#### Complexity

* **Time Complexity:** $\mathcal{O}(N^2)$ — 2 nested loops ($j$ and $i$). Given $N \le 250$, $250^2 = 62500$ operations, easily running within the 2.0-second time limit.
* **Space Complexity:** $\mathcal{O}(N^2)$ for the DP table (or $\mathcal{O}(N)$ with a rolling array).


### 5. Linearity of Expectation - O(N^2)

Linearity of expectation lets us calculate the expected contribution of each pancake independently. The values in `d` do not need to be distinct; only the pancake widths determine whether the stack can continue.

Let $P_i$ be the probability that pancake $i$ is successfully placed. Then:

$$
\mathbb{E}[\text{Total Deliciousness}] =
\sum_{i=0}^{N-1} d[i] P_i
$$

#### Calculating $P_i$

The process accepts exactly the initial **strictly decreasing prefix** of the random permutation of pancake indices. Pancake $i$ is placed if and only if every pancake before it is larger than $i$, and those preceding pancakes appear in decreasing order.

Suppose exactly $r$ pancakes appear before pancake $i$. There are $N-i-1$ pancakes larger than $i$, so:

1. Choose the $r$ preceding pancakes in $\binom{N-i-1}{r}$ ways.
2. Their order is forced: they must appear in decreasing order.
3. Arrange the remaining $N-r-1$ pancakes after pancake $i$ in $(N-r-1)!$ ways.

Since all $N!$ permutations are equally likely:

$$
P_i =
\sum_{r=0}^{N-i-1}
\frac{\binom{N-i-1}{r}(N-r-1)!}{N!}
$$

Therefore:

$$
\mathbb{E}[\text{Total Deliciousness}] =
\sum_{i=0}^{N-1} d[i]
\sum_{r=0}^{N-i-1}
\frac{\binom{N-i-1}{r}(N-r-1)!}{N!}
$$

#### Complexity

Computing every $P_i$ directly from the summation takes $\mathcal{O}(N^2)$ time. The factorial and binomial values can be generated incrementally, avoiding expensive recomputation.

The calculation uses $\mathcal{O}(1)$ additional space when each probability is accumulated on the fly. The dynamic programming solution above is usually simpler to implement and is the better canonical solution for this problem.