from b_tree.btree import BTree
import random
import json
import time

for n_elements in [10, 100, 1000, 10000, 100000, 1000000, 10000000]:
    print("Running {} elements".format(n_elements))
    btree = BTree(3)
    elements = []

    tree_info = {}

    random.seed(5)

    for i in range(0, n_elements):
        elements.append(random.randint(0, n_elements+1))

    for element in elements:
        insert_init_time = time.time()
        btree.insert(element)

    for test in range(1, 31):
        init_time = time.time()
        btree.search(random.randint(0, n_elements+1))

        tree_info["search_avg"] = time.time() - init_time

        json.dump(tree_info, open("{}_elements/search_time_test_{}.txt".format(len(elements), test), 'w'))
