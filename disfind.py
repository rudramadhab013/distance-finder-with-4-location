import networkx as nx
import matplotlib.pyplot as plt

def main():
    # Input location names
    locations = []
    print("Enter the names of 4 locations:")
    for i in range(4):
        loc = input(f"Location {i+1}: ")
        locations.append(loc)

    # Create a directed graph
    G = nx.Graph()

    # Add nodes (locations) to the graph
    for loc in locations:
        G.add_node(loc)

    # Input distances between locations
    print("\nEnter the distances between the locations:")

    edges = []
    for i in range(len(locations)):
        for j in range(i + 1, len(locations)):
            dist = float(input(f"Distance between {locations[i]} and {locations[j]}: "))
            G.add_edge(locations[i], locations[j], weight=dist)
            edges.append((locations[i], locations[j], dist))

    # Draw the graph
    pos = nx.spring_layout(G)  # Layout for the graph
    plt.figure(figsize=(10, 6))

    nx.draw(G, pos, with_labels=True, node_size=700, node_color='lightblue', font_size=12, font_weight='bold')
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    plt.title("Location Graph with Distances")
    plt.show()

    # Find the shortest path
    print("\nFind the shortest path between two locations.")
    start = input("Enter the starting location: ")
    end = input("Enter the ending location: ")

    try:
        shortest_path = nx.shortest_path(G, source=start, target=end, weight='weight')
        shortest_distance = nx.shortest_path_length(G, source=start, target=end, weight='weight')
        print(f"\nThe shortest path from {start} to {end} is: {' -> '.join(shortest_path)}")
        print(f"Total distance: {shortest_distance}")
    except nx.NetworkXNoPath:
        print("\nNo path exists between these locations.")

if __name__ == "__main__":
    main()
