from config import MAXN
from fec import get_w
from data.read import init

import numpy as np


sentence = input()
word_set = ['#start']+sentence.split(' ')
data = init(sentence.split(' '))
word_map = {}
maped_word_set = []
for i in range(len(word_set)):
    maped_word_set.append(i)
    word_map[i] = word_set[i]

adj = np.ones((MAXN, MAXN))
for i in range(MAXN):
    for j in range(MAXN):
        adj[i][j] = -1

for u in maped_word_set:
    for v in maped_word_set:
        if v == 0 or u == v:
            continue
        # print(u, v, get_w(data, word_map[u], word_map[v]))
        try:
            if get_w(data, word_map[u], word_map[v]) != 0:
                adj[u][v] = get_w(data, word_map[u], word_map[v])
        except BaseException:
            pass

for i in range(6):
    for j in range(6):
        print(adj[i][j], end=' ')
    print('')

nis = np.ones(20)
path = []
max_p = 0
max_path = np.ones(20)
for i in range(20):
    max_path = -1


def dfs(u, p):
    global max_p, max_path, word_set
    if p < max_p:
        return
    path.append(u)
    if(len(path) == len(word_set)):
        if p > max_p:
            max_p = p
            max_path = []
            for i in path:
                max_path.append(i)
            print(max_path)
    nis[u] = 0

    # print(u,p,path)
    for k in range(len(adj[u])):
        if(adj[u][k] < 0):
            continue
        if nis[k]:
            dfs(k, p*adj[u][k])
    nis[u] = 1
    path.pop()


dfs(0, 1)
for i in max_path:
    print(word_map[i], end=' ')
print('')

# adj_p, path = floyd(adj, len(maped_word_set)-1)

# # for i in range(6):
# #     for j in range(6):
# #         print(adj_p[i][j], end=' ')
# #     print('')

# get_p(word_map, path, 0, len(maped_word_set)-1)
