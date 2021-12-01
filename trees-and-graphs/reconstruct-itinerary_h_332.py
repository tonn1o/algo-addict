class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        start = "JFK"
        graph = collections.defaultdict(list)
        sources = set() 
        n = len(tickets)
        res = None
        
        for ticket in tickets:
            graph[ticket[0]].append(ticket[1])
            sources.add(ticket[0])
            
        # do greedy sort
        # doing that valid itinerary with smallest lexical order will pop up first
        for source in sources:
            graph[source].sort()
        
        def dfs(node, path):
            nonlocal res
            
            if not graph[node]:
                if len(path) == n:
                    res = path + [node]
                    return True

                            
            for destIdx in range(len(graph[node])):
                dests = graph[node].copy()
                found = dfs(graph[node].pop(destIdx), path + [node])
                graph[node] = dests
                
                if found:
                    return True
                
            return
                
        dfs(start, [])
        return res
