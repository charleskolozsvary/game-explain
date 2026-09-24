import numpy as np
import matplotlib.pyplot as plt

RES_IMAGE_NAME = "payoff.png"

max_w = 11
max_d = 11
max_b = 11

# Case 1: b = 0
P1 = np.zeros((max_d, max_w))

for d in range(1, max_d):
    for w in range(max_w):
        if w == 0:
            P1[d, w] = 10*d
        else:
            P1[d, w] = -10*d

# Case 2: b >= 1
P2 = np.zeros((max_b-1, max_w-1))

for b in range(1, max_b):
    for w in range(1, max_w):
        if b == w:
            P2[b-1, w-1] = 20*b
        else:
            P2[b-1, w-1] = -10*abs(b-w)

# shared color scale
global_min = min(P1.min(), P2.min())
global_max = max(P1.max(), P2.max())

fig, axes = plt.subplots(1, 2, figsize=(12, 5))
plt.subplots_adjust(wspace=0.3)

im1 = axes[0].imshow(P1, origin='lower', cmap='coolwarm',
                     vmin=global_min, vmax=global_max)
axes[0].set_title("Betting 0")
axes[0].set_xlabel("tricks won")
axes[0].set_ylabel("cards dealt")

im2 = axes[1].imshow(P2, origin='lower', cmap='coolwarm',
                     vmin=global_min, vmax=global_max)
axes[1].set_title("Betting 1 or more")
axes[1].set_xlabel("tricks won")
axes[1].set_ylabel("tricks bid")

axes[1].set_xticks(range(max_w-1))
axes[1].set_xticklabels(range(1, max_w))
axes[1].set_yticks(range(max_b-1))
axes[1].set_yticklabels(range(1, max_b))

# Create a colorbar axis on the right
cbar = fig.colorbar(im1, ax=axes.ravel().tolist(), shrink=0.85)
cbar.set_label("Points")

plt.savefig(RES_IMAGE_NAME, dpi=350, bbox_inches="tight", pad_inches=0.05)

# \[
# P(b, d, w) = \begin{cases}
# 10d &\text{if $0 = b = w$},\\
# 20b & \text{if $1 \le b = w$},\\
# -10d &\text{if $0 = b \ne w$},\\
# -10|b-w| & \text{if $1 \le b \ne w$}
# \end{cases}
# \]
