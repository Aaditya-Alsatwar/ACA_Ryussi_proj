class MemoryAllocationSimulator:
    def __init__(self, blocks):
        self.blocks = blocks

    def first_fit(self, processes):
        allocation = [-1] * len(processes)
        internal_frag = [0] * len(self.blocks)

        for i in range(len(processes)):
            for j in range(len(self.blocks)):
                if self.blocks[j] >= processes[i]:
                    allocation[i] = j
                    internal_frag[j] = self.blocks[j] - processes[i]
                    self.blocks[j] -= processes[i]
                    break
        return allocation, internal_frag

    def best_fit(self, processes):
        allocation = [-1] * len(processes)
        internal_frag = [0] * len(self.blocks)

        for i in range(len(processes)):
            best_index = -1
            for j in range(len(self.blocks)):
                if self.blocks[j] >= processes[i]:
                    if best_index == -1 or self.blocks[j] < self.blocks[best_index]:
                        best_index = j
            if best_index != -1:
                allocation[i] = best_index
                internal_frag[best_index] = self.blocks[best_index] - processes[i]
                self.blocks[best_index] -= processes[i]
        return allocation, internal_frag

    def worst_fit(self, processes):
        allocation = [-1] * len(processes)
        internal_frag = [0] * len(self.blocks)

        for i in range(len(processes)):
            worst_index = -1
            for j in range(len(self.blocks)):
                if self.blocks[j] >= processes[i]:
                    if worst_index == -1 or self.blocks[j] > self.blocks[worst_index]:
                        worst_index = j
            if worst_index != -1:
                allocation[i] = worst_index
                internal_frag[worst_index] = self.blocks[worst_index] - processes[i]
                self.blocks[worst_index] -= processes[i]
        return allocation, internal_frag

def display_allocation(method, allocation, processes, internal_frag):
    print(f"\n{method} Allocation:")
    print("Process No.\tProcess Size\tBlock No.\tInternal Fragmentation")
    for i in range(len(processes)):
        if allocation[i] != -1:
            print(f"{i+1}\t\t{processes[i]}\t\t{allocation[i]+1}\t\t{internal_frag[allocation[i]]}")
        else:
            print(f"{i+1}\t\t{processes[i]}\t\tNot Allocated\t\t-")

if __name__ == "__main__":
    blocks = list(map(int, input("Enter memory blocks (space-separated): ").split()))
    processes = list(map(int, input("Enter process sizes (space-separated): ").split()))

    print("\n--- Memory Allocation Simulation ---")
    
    simulator = MemoryAllocationSimulator(blocks.copy())
    
    # First-Fit
    allocation, internal_frag = simulator.first_fit(processes)
    display_allocation("First-Fit", allocation, processes, internal_frag)

    # Resetting memory blocks for the next fit method
    simulator.blocks = blocks.copy()

    # Best-Fit
    allocation, internal_frag = simulator.best_fit(processes)
    display_allocation("Best-Fit", allocation, processes, internal_frag)

    # Resetting memory blocks for the next fit method
    simulator.blocks = blocks.copy()

    # Worst-Fit
    allocation, internal_frag = simulator.worst_fit(processes)
    display_allocation("Worst-Fit", allocation, processes, internal_frag)
