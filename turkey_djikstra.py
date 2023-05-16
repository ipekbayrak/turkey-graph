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

# Apply Dijkstra's algorithm
start_city = 'ADANA'  # Replace with the name of the start city
end_city = 'SİNOP'  # Replace with the name of the end city
shortest_path = nx.dijkstra_path(G, start_city, end_city, weight='weight')

# Print the shortest path
print('Shortest path from {} to {}:'.format(start_city, end_city))
print(' -> '.join(shortest_path))

# Draw the graph
nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_labels(G, pos)

# Draw the shortest path
shortest_path_edges = list(nx.utils.pairwise(shortest_path))
nx.draw_networkx_edges(G, pos, edgelist=shortest_path_edges, edge_color='r')  # Draw the shortest path in red

# Show the plot
plt.show()
