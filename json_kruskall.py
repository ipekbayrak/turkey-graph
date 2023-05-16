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

# Apply Kruskal's algorithm
mst = nx.minimum_spanning_tree(G, algorithm='kruskal')

# Load the positions from the JSON file
with open('turkiye_pos.json', 'r', encoding='utf-8') as json_file:
    pos_data = json.load(json_file)


# Prepare the positions for networkx
pos = {upper_tr(city): (int(info['Boylam']*100000), int(info['Enlem']*100000)) for city, info in pos_data.items()}

# Draw the graph
nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_labels(G, pos)

nx.draw_networkx_edges(G, pos, edgelist=mst.edges(), edge_color='r')  # Draw the edges in the minimum spanning tree in red

total_weight = sum([data['weight'] for _, _, data in mst.edges(data=True)])
print("Toplam yol uzunluğu", total_weight)


# Show the plot
plt.show()

 