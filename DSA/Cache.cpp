#include <iostream>
#include <list>
#include <unordered_map>

using namespace std;

class LRUCache {
    int capacity;
    list<int> keys;
    unordered_map<int, pair<int, list<int>::iterator>> cache;

public:
    LRUCache(int cap) : capacity(cap) {}

    int get(int key) {
        if (cache.find(key) == cache.end()) {
            return -1;
        }
        keys.erase(cache[key].second);
        keys.push_front(key);
        cache[key].second = keys.begin();
        return cache[key].first;
    }

    void put(int key, int value) {
        if (cache.find(key) != cache.end()) {
            keys.erase(cache[key].second);
        } else if (keys.size() >= capacity) {
            int lru = keys.back();
            keys.pop_back();
            cache.erase(lru);
        }
        keys.push_front(key);
        cache[key] = {value, keys.begin()};
    }

    void displayCache() {
        cout << "Cache state: ";
        for (int key : keys) {
            cout << key << " : " << cache[key].first << " | ";
        }
        cout << endl;
    }
};

int main() {
    int capacity;
    cout << "Enter the cache capacity: ";
    cin >> capacity;

    LRUCache lru(capacity);
    int choice;

    do {
        cout << "\nLRU Cache Menu:\n";
        cout << "1. Put (Add/Update a key-value pair)\n";
        cout << "2. Get (Retrieve a value by key)\n";
        cout << "3. Display Cache\n";
        cout << "4. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
            case 1: {
                int key, value;
                cout << "Enter key and value: ";
                cin >> key >> value;
                lru.put(key, value);
                cout << "Key-Value pair added/updated.\n";
                break;
            }
            case 2: {
                int key;
                cout << "Enter key to retrieve: ";
                cin >> key;
                int result = lru.get(key);
                if (result == -1) {
                    cout << "Key not found.\n";
                } else {
                    cout << "Value: " << result << endl;
                }
                break;
            }
            case 3:
                lru.displayCache();
                break;
            case 4:
                cout << "Exiting program.\n";
                break;
            default:
                cout << "Invalid choice! Please try again.\n";
        }
    } while (choice != 4);

    return 0;
}
