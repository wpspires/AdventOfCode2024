text = filter(None, open('input.txt').read().split('\n'))

graph = {}
sum_of_middle_pages = 0

for line in text:
    if line.__contains__("|"):
        kvp = line.split("|")
        dict_values = graph.get(kvp[0])
        if dict_values is None:
            graph[kvp[0]] = [kvp[1]]
        else:
            dict_values.append(kvp[1])
            graph[kvp[0]] = dict_values
    else:
        updates = line.split(",")
        ordered = True
        for x in range(len(updates)-1,-1,-1):
            if ordered:
                keys = graph.get(updates[x])
                if keys is not None:
                    out_of_order = [number for number in updates[0:x] if number in keys]
                    if out_of_order:
                        ordered = False
        if ordered:
            sum_of_middle_pages += int(updates[len(updates)//2])

print(sum_of_middle_pages)