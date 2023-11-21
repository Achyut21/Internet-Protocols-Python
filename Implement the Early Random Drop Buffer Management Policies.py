import random

class EarlyRandomDropQueue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.queue = []

    def is_full(self):
        return len(self.queue) >= self.max_size

    def enqueue(self, packet):
        if not self.is_full():
            self.queue.append(packet)
        else:
            # Randomly decide whether to drop the packet upon arrival
            if random.random() >= 0.5:
                print("Early Randomly dropped a packet upon arrival:", packet)
            else:
                self.queue.append(packet)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            print("Queue is empty. No packets to dequeue.")
            return None

    def is_empty(self):
        return len(self.queue) == 0

# Example usage:
max_queue_size = 5
queue = EarlyRandomDropQueue(max_queue_size)

# Enqueue packets
for packet_id in range(1, 8):
    packet = f"Packet-{packet_id}"
    queue.enqueue(packet)

# Dequeue packets
while not queue.is_empty():
    packet = queue.dequeue()
    print("Dequeued:", packet)
