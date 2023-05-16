import json
import networkx as nx
import matplotlib.pyplot as plt

def upper_tr(text):
    tr_map = {
        'ı': 'I',
        'i': 'İ',
        'ğ': 'Ğ',
        'ü': 'Ü',
        'ş': 'Ş',
        'ö': 'Ö',
        'ç': 'Ç'
    }
    return ''.join([tr_map.get(c, c.upper()) for c in text])

# Load the data from the JSON file with UTF-8 encoding
with open('road_lengths.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

# Create a graph
G = nx.Graph()

# Add edges to the graph
for city1, connections in data.items():
    for city2, distance in connections.items():
        if distance is not None:  # Ignore the distances to the city itself (which are None)
            G.add_edge(city1, city2, weight=distance)

# Load the positions from the JSON file
with open('turkiye_pos.json', 'r', encoding='utf-8') as json_file:
    pos_data = json.load(json_file)

# Prepare the positions for networkx
pos = {upper_tr(city): (int(info['Boylam']*100000), int(info['Enlem']*100000)) for city, info in pos_data.items()}

# Apply the TSP
tsp_path = nx.approximation.greedy_tsp(G, weight='weight')

# Print the TSP path
print('TSP path:')
print(' -> '.join(tsp_path))

# Draw the graph
nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_labels(G, pos)

# Draw the edges
tsp_edges = [(tsp_path[i], tsp_path[i+1]) for i in range(len(tsp_path) - 1)]  # Create a list of edges from the TSP path

for i in range(len(tsp_edges)):
    print(tsp_path[i] + ' -> ' + str(G.edges[tsp_edges[i]]['weight']) + ' -> ' + tsp_path[i+1])

# Calculate the total length of the TSP path
total_length = sum(G.edges[tsp_edges[i]]['weight'] for i in range(len(tsp_edges)))

# Print the total length
print('Total length of the TSP path: {}'.format(total_length))

nx.draw_networkx_edges(G, pos, edgelist=tsp_edges, edge_color='r')  # Draw the TSP path in red

# Show the plot
plt.show()

