from Graph import Graph
from Queue import MyQueue
# You can check the input graph in console tab

# Create Queue => queue = MyQueue()
# Functions of Queue => enqueue(int), dequeue(), size(), front(), is_empty()
# Create Stack => stack = MyStack()
# Functions of Stack => push(int), pop(), top(), is_empty() 
# Create Graph => graph = Graph(vertices)
# Create LinkedList => link_list = LinkedList()
# Functions of LinkedList => insert_at_head(Node), is_empty(), delete(),
#                            delete_at_head(list), search(), print_list()
# class Node => data, next_element
# Breadth First Traversal of Graph g from source vertex

'''
O(V * E)  where V -> Number of Vertices, E -> Number of Edges
'''
# def bfs_traversal(g, source):
#     result = ""
#     num_of_vertices = g.vertices
#     # Write - Your - Code
#     for i in range(num_of_vertices):
#         if str(i) not in result:
#             result += str(i)
#         temp_node = g.array[i].get_head()
#         while temp_node:
#             if str(temp_node.data) not in result:
#                 result += str(temp_node.data)
#             temp_node = temp_node.next_element
#     # For the above graph, it should return "01234" or "02143" etc
#     return result

'''
O(V + E)
'''
def bfs_traversal_helper(visited, result, g, source):
    queue = MyQueue()

    queue.enqueue(source)
    visited[source] = True

    while queue.is_empty() is False:
        current_node = queue.dequeue()
        result += str(current_node)

        temp_node = g.array[current_node].head_node
        while temp_node:
            if visited[temp_node.data] is False:
                queue.enqueue(temp_node.data)
                visited[temp_node.data] = True
            temp_node = temp_node.next_element
    
    return result, visited

def bfs_traversal(g, source):
    result = ""
    num_of_vertices = g.vertices
    # Write - Your - Code
    visited = [False] * num_of_vertices
    
    # starts from the source read from params and visits as much as it can
    result, visited = bfs_traversal_helper(visited, result, g, source)

    # visit remaining nodes
    for i in range(num_of_vertices):
        if visited[i] is False:
            result, visited = bfs_traversal_helper(visited, result, g, i)

    # For the above graph, it should return "01234" or "02143" etc
    return result


g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.print_graph()

print(bfs_traversal(g, 0))
