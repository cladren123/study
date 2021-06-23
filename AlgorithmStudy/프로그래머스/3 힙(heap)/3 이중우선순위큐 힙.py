"""
["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
[0, 0]

["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
[333, -45]

heapq.nlargest(1, heap)
"""
import heapq

# operations = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
operations = ["I 45", "I 47",  "I 46"]

def solution(operations):
    answer = [0,0]
    heap = []

    for i in operations :
        semi = list(i.split())
        print(semi)
        print(heap)
        if semi[0] == 'I' :
            heapq.heappush(heap, int(semi[1]))
        if len(heap) > 0 :
            if semi[0] == 'D' :
                if semi[1] == '-1' :
                    heap.pop(0)
                elif semi[1] == '1' :
                    heap.pop(-1)

    if len(heap) > 0 :
        maxnum = max(heap)
        minnum = min(heap)
        answer[0] = maxnum
        answer[1] = minnum

    print(answer)
    return answer

solution(operations)