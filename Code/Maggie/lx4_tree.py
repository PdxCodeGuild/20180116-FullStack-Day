import random

names = ['virginia', 'christine', 'carl', 'lillian']


def generate_tree(depth):
    n_children = int(6/depth) #random.random()*
    if n_children == 0:
        return {'type': 'leaf', 'name': random.choice(names)}
    branch = {'type': 'branch', 'children': []}
    for i in range(n_children):
        child = generate_tree(depth+1)
        branch['children'].append(child)
    print(branch)
    return branch


def print_node(node, indentation):
    if node['type'] == 'leaf':
        print(indentation + node['name'])
    else:
        print(indentation + '-')
        for i in range(len(node['children'])):
            print_node(node['children'][i], indentation + '\t')

# count all trees and branches
def count_nodes(node):
    if node['type'] == 'leaf':
        return 1
    r = 1
    for i in range(len(node['children'])):
        r += count_nodes(node['children'][i])
    return r

l = 0
def count_leaves(node):
    global l
    if node['type'] == 'leaf':
        l += 1
        return 1
    for i in range(len(node['children'])):
       count_leaves(node['children'][i])
    return l

def rename(node, name, newname):
    if node['type'] == 'leaf':
        return 1
    r = 1
    for i in range(len(node['children'])):
       r += count_leaves(node['children'][i])
    return

root = generate_tree(1)
print_node(root, '')
print(count_nodes(root))
print(count_leaves(root))
#print(rename(root, 'christine', 'roger'))

