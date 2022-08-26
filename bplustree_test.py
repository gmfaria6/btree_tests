from b_tree.bplustree import BPlusTree
import random
import json
import time

for n_elements in [10, 100, 1000, 10000, 100000, 1000000, 10000000]:
    for test in range(1, 31):
        print("Running {} elements test {}".format(n_elements, test))
        btree = BPlusTree(3)
        
        elements = []

        tree_info = {}

        random.seed(5)

        for i in range(0, n_elements):
            elements.append(random.randint(0, n_elements+1))
        
        init_time = time.time()

        avg_insert_time = 0

        for element in elements:
            insert_init_time = time.time()
            btree.insert(element)
            avg_insert_time += time.time() - insert_init_time
            # print(btree.height)
            # print(btree)
        avg_insert_time = avg_insert_time/len(elements)

        end_time_all_insert = time.time() - init_time
        # print("btree")
        # print(btree)

        # print(btree.search(39))
        # print(btree.search(43))

        tree_info["height"] = btree.height
        tree_info["insert_avg_time"] = avg_insert_time
        tree_info["total_insert_time"] = end_time_all_insert

        json.dump(tree_info, open("{}_elements/bplus_tree_test_{}.txt".format(len(elements), test), 'w'))