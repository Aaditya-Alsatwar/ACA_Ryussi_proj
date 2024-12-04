#include <iostream>
#include <vector>
#include <queue>
#include <unordered_map>
#include <limits>
#include <algorithm>

using namespace std;

class Graph {
    unordered_map<int, vector<pair<int, int>>> adjList;

public:
    void addEdge(int u, int v, int weight) {
        adjList[u].emplace_back(v, weight);
        adjList[v].emplace_back(u, weight); // For undirected graph
    }

    void removeEdge(int u, int v) {
        adjList[u].erase(remove_if(adjList[u].begin(), adjList[u].end(),
            [v](pair<int, int> edge) { return edge.first == v; }), adjList[u].end());

        adjList[v].erase(remove_if(adjList[v].begin(), adjList[v].end(),
            [u](pair<int, int> edge) { return edge.first == u; }), adjList[v].end());
    }

    void dijkstra(int source) {
        unordered_map<int, int> distances;
        for (auto &node : adjList) {
            distances[node.first] = numeric_limits<int>::max();
        }
        distances[source] = 0;

        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> pq;
        pq.push({0, source});

        while (!pq.empty()) {
            int dist = pq.top().first;
            int node = pq.top().second;
            pq.pop();

            for (auto &neighbor : adjList[node]) {
                int nextNode = neighbor.first;
                int edgeWeight = neighbor.second;
                if (dist + edgeWeight < distances[nextNode]) {
                    distances[nextNode] = dist + edgeWeight;
                    pq.push({distances[nextNode], nextNode});
                }
            }
        }

        for (auto &dist : distances) {
            cout << "Distance from " << source << " to " << dist.first << " is " << dist.second << endl;
        }
    }
};

int main() {
    Graph g;
    int choice;

    do {
        cout << "\nGraph Menu:\n";
        cout << "1. Add Edge\n";
        cout << "2. Remove Edge\n";
        cout << "3. Find Shortest Path (Dijkstra's Algorithm)\n";
        cout << "4. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
            case 1: {
                int u, v, weight;
                cout << "Enter edge (u v weight): ";
                cin >> u >> v >> weight;
                g.addEdge(u, v, weight);
                cout << "Edge added.\n";
                break;
            }
            case 2: {
                int u, v;
                cout << "Enter edge to remove (u v): ";
                cin >> u >> v;
                g.removeEdge(u, v);
                cout << "Edge removed.\n";
                break;
            }
            case 3: {
                int source;
                cout << "Enter source node: ";
                cin >> source;
                cout << "Shortest paths from node " << source << ":\n";
                g.dijkstra(source);
                break;
            }
            case 4:
                cout << "Exiting program.\n";
                break;
            default:
                cout << "Invalid choice! Please try again.\n";
        }
    } while (choice != 4);

    return 0;
}
