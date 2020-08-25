## Sorting Mechanism

Centre Column +4
Lines of Two +2
Lines of Three +5
Win! +100000000

Opp Line of Two -2
Opp Winnable line of Three -100

What about considering the possiblity when the next piece is placed above it?

# Minimax Algorithm
- Look at all 7 possibilities (then all 7 secondary possibilites from each of the primary moves) -- The computer evaluates them real quick!
- Look at opponent's potential moves as well!
- At a certain depth, we evaluate scores according to the sorting mechanism
- The greater the depth, the better the AI is

MAX

MIN

MAX

Othello
- Frontier disks vs interior disks (not touching exterior square)
  - Maximise interior disks and minimise frontier disks
  - Corners, Buffers (one block from corner), edges (check out video for score)
  - Stable disks (can never be flipped)

https://www.youtube.com/watch?v=y7AKtWGOPAE