def get_indices_of_item_weights(weights, limit):
  i=0
  
  ht = {weights[i]:i}
  
  w = weights[i]
  w2 = limit - weights[i]
  while i < len(weights):
    print(weights[i])
    i += 1
  return (weights[0],limit-weights[0])
  # for w in range(len(weights)):
  #   print(w)


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