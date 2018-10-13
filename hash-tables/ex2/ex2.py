def reconstruct_trip(tickets):
  ht = {}
  route = [''] * (len(tickets) - 1) #ah this is how we will get it to output to the array in a string format *len being the size of the input
  #route =[]
  for t in tickets:
    if t[0] is None:
    # if not t[0]:  
      route[0] = t[1] 
    ht[t[0]] = t[1] # start location key and destination is value

  for i in range(1, len(tickets) - 1): # from 1 since 0 is none to end of list
    try:
      route[i] = ht[route[i-1]]
    except KeyError:
      return []  
  return route
  
  # try:
  #   current = ht[None]
  #   route.append(current)
  #   next = ht[None] 
  #   while (next != None):
  #     try:
  #       next = ht[next]
  #       if (next):
  #         route.append(next)
  #     except:
  #       return []
  #   return route
  # except:
  #   return []

  # for i in range(len(tickets)):
  #   tix = ht[tickets[i]]
  #   tix = (ht[tickets[i][0]],ht[tickets[i][1]])
    #  des = ht[tickets[i][1]]
    # if (ht.get(tix) = None:
    #   return (ht.get(tix))
          
  


if __name__ == '__main__':
 pass

  # You can write code here to test your implementation using the Python repl
  
