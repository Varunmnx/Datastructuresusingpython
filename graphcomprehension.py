class graph:
    def __init__(self,edges):
        self.edges = edges
        self.graphdict = {}
        for key,elem in self.edges:
            if key not in self.graphdict:
                self.graphdict[key] = [elem]

            else:
                self.graphdict[key].append(elem)

        print(self.graphdict)

if __name__ =="__main__":
    routes = [("mumbai","paris"),("mumbai","kochi"),("bengaluru","jaipur"),("indus","kochi"),("indus","ii")]
    g = graph(routes)