from UCS import UniformCasrSearch

ucs = UniformCasrSearch('arad','pitesti')
node = ucs.search()

ucs.printPath(node)