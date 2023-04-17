from DLS import DepthLimitedSearch

dls = DepthLimitedSearch('rimnicu vilcea','fagaras',2)
node = dls.search()
if node :
    dls.printPath(node)
if node == 'cut-off':
    print('cut-off')