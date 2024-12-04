class VirtualMemoryManager:
    def __init__(self, pages, num_frames):
        self.pages = pages
        self.num_frames = num_frames

    def fifo(self):
        frame = []
        page_faults = 0

        for page in self.pages:
            if page not in frame:
                if len(frame) < self.num_frames:
                    frame.append(page)
                else:
                    frame.pop(0)
                    frame.append(page)
                page_faults += 1

        return page_faults

    def lru(self):
        frame = []
        page_faults = 0

        for page in self.pages:
            if page not in frame:
                if len(frame) < self.num_frames:
                    frame.append(page)
                else:
                    frame.pop(0)
                    frame.append(page)
                page_faults += 1
            else:
                frame.remove(page)
                frame.append(page)

        return page_faults

    def optimal(self):
        frame = []
        page_faults = 0

        for i in range(len(self.pages)):
            if self.pages[i] not in frame:
                if len(frame) < self.num_frames:
                    frame.append(self.pages[i])
                else:
                    future_use = [
                        self.pages[i:].index(x) if x in self.pages[i:] else float('inf')
                        for x in frame
                    ]
                    frame.pop(future_use.index(max(future_use)))
                    frame.append(self.pages[i])
                page_faults += 1

        return page_faults

    def clock(self):
        frame = [-1] * self.num_frames
        use_bit = [0] * self.num_frames
        page_faults = 0
        pointer = 0

        for page in self.pages:
            if page not in frame:
                while use_bit[pointer] == 1:
                    use_bit[pointer] = 0
                    pointer = (pointer + 1) % self.num_frames
                frame[pointer] = page
                use_bit[pointer] = 1
                pointer = (pointer + 1) % self.num_frames
                page_faults += 1

        return page_faults


if __name__ == "__main__":
    pages = list(map(int, input("Enter page reference string (space-separated): ").split()))
    num_frames = int(input("Enter number of frames: "))

    vmm = VirtualMemoryManager(pages, num_frames)

    fifo_faults = vmm.fifo()
    print(f"FIFO Page Faults: {fifo_faults}")

    lru_faults = vmm.lru()
    print(f"LRU Page Faults: {lru_faults}")

    optimal_faults = vmm.optimal()
    print(f"Optimal Page Faults: {optimal_faults}")

    clock_faults = vmm.clock()
    print(f"Clock Page Faults: {clock_faults}")
