
import heapq

heap = [30,10,20];

heapq.heapify(heap);

print(heap);

while heap :
    now = heapq.heappop(heap);
    print(now);