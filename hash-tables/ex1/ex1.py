def get_indices_of_item_weights(weights, limit):
  
  
  ht = {}
  
  for i in range(len(weights)):
    ht[weights[i]] = i
  for i in range(len(weights)):
    dif = limit - weights[i]
    if ht.get(dif):
      return (ht.get(dif),i)
  return ()
if __name__ == '__main__':
  # You can write code here to test your implementation using the Python repl
  get_indices_of_item_weights([1,2,3,4,5,6],10) 

# weights[i] + weights[j] = limits
# w = weights[i]
# w2 = limit - weights[i]
 
# (w,w2) w>w2

# colors = ["red", "green", "blue", "purple"]
# for i in range(len(colors)):
#     print(colors[i])

# colors = ["red", "green", "blue", "purple"]
# i = 0
# while i < len(colors):
#     print(colors[i])
#     i += 1