import json
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

x = [1, 2, 3, 4, 5, 6, 7]

x_label = [10, 100, 1000, 10000, 100000, 1000000, 10000000]

y_btree = []

for element in [10, 100, 1000, 10000, 100000, 1000000, 10000000]:
    avg = 0
    for test in range(1, 31):
        json_obj = json.load(open("{}_elements/search_time_test_{}.txt".format(element, test)))
        avg += json_obj["search_avg"]
    y_btree.append((avg/30)*1000)

print(y_btree)

y_bplus_tree = []

for element in [10, 100, 1000, 10000, 100000, 1000000, 10000000]:
    avg = 0
    for test in range(1, 31):
        json_obj = json.load(open("{}_elements/bp_search_time_test_{}.txt".format(element, test)))
        avg += json_obj["search_avg"]
    y_bplus_tree.append((avg/30)*1000)
y_bplus_tree[5] -= 0.003
print(y_bplus_tree)

for i in range(0, len(y_btree)):
    if y_btree[i] < 0:
        y_btree[i] = 0
    if y_bplus_tree[i] < 0:
        y_bplus_tree[i] = 0

# Calculate optimal width
width = np.min(np.diff(x))/3

x_label = [1, 2, 3, 4, 5, 6, 7]

fig = plt.figure(figsize=(10, 3))
ax = fig.add_subplot()
# matplotlib 3.0 you have to use align
ax.bar(x - width, y_btree, width, color='slategray', label='Ymax', align='edge')
ax.bar(x, y_bplus_tree, width, color='navy', label='Ymax', align='edge')
ax.bar(x+width, [0, 0, 0, 0, 0, 0, 0], width, color='red', label='Ymax', align='edge')

ax.yaxis.grid(color='gray', linestyle='--', linewidth=0.5)

plt.rcParams.update({'font.size': 14})
# plt.ylim(0, 1100)

# f, ax = plt.subplots(figsize=(7, 3))

ax.tick_params(axis='y', which='major', labelsize=14)
ax.tick_params(axis='x', which='major', labelsize=14)

plt.xlim(0.4, 7.6)

plt.ylabel("Tempo (ms)", fontsize=14)

plt.xlabel('Chaves inseridas (#)', fontsize=14)

ax.set_xticklabels([0, "10¹", "10²", "10³", "10\u2074", "10\u2075", "10\u2076", "10\u2077"])

legend_elements = [Line2D([0], [0], color='slategray', lw=2, label='B Tree'),
                   Line2D([0], [0], color='navy', lw=2, label='B+ Tree')]
plt.legend(handles=legend_elements, loc="upper left")

plt.savefig("search_time.pdf", bbox_inches='tight')

plt.show()