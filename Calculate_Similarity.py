from queue import PriorityQueue
class CalcSim:
    doc_rank = PriorityQueue()
    def __init__(self,corpus,inp):
        for doc_name in corpus:    
            s = 0
            orig = corpus[doc_name]
            for tri in inp:
                if tri in orig:
                    s+=1
            self.doc_rank.put((s/len(inp)*100,doc_name))
        
