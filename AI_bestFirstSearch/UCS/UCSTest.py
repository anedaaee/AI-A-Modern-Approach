from UCS import UniformCasrSearch

ucs = UniformCasrSearch('arad','bucharest')
node = ucs.search()

ucs.printPath(node)