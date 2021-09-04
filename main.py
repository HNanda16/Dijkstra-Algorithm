from dijkstra import dijkstra


#valid
def run_test_one():
  #arrange
  graph = {'a':{'b':1, 'c':2},
          'b':{'a':1, 'c':2, 'd':3},
          'c':{'a':2, 'b':2, 'd':1},
          'd':{'b':3, 'c':1}}

  start = 'a'
  end = 'd'
  expected = ('acd', 3)

  #act
  result = dijkstra(graph, start, end)

  #assert
  if expected == result:
      print("Test passed")
      print(result)
  else:
      print("Test failed")
      print("Expected: " + str(expected))
      print("But Got: " + str(result))


#Boundary - large graph
def run_test_two():
  #arrange
  graph = {'a':{'b':1, 'c':2, 'e':6},
          'b':{'a':1, 'c':2, 'd':3, 'e':5},
          'c':{'a':2, 'b':2, 'd':1},
          'd':{'b':3, 'c':1, 'e':1},
          'e':{'a':6, 'b':5, 'd':1, 'k':1}, 
          'f':{'g':1, 'h':2, 'k':6},
          'g':{'f':1, 'h':2, 'i':3, 'k':5},
          'h':{'f':2, 'g':2, 'i':1},
          'i':{'g':3, 'h':1, 'k':1},
          'k':{'f':6, 'g':5, 'i':1, 'e':1}}

  start = 'a'
  end = 'f'
  expected = ('acdekihf', 9)

  #act
  result = dijkstra(graph, start, end)

  #assert
  if expected == result:
      print("Test passed")
      print(result)
  else:
      print("Test failed")
      print("Expected: " + str(expected))
      print("But Got: " + str(result))


#Erroneous - No path from start to end
def run_test_three():
  #arrange
  graph = {'a':{'b':1, 'c':2},
          'b':{'a':1, 'c':2},
          'c':{'a':2, 'b':2},
          'd':{}}

  start = 'a'
  end = 'd'
  expected = ("No path from start to end", float('inf'))

  #act
  result = dijkstra(graph, start, end)

  #assert
  if expected == result:
      print("Test passed")
      print(result)
  else:
      print("Test failed")
      print("Expected: " + str(expected))
      print("But Got: " + str(result))


run_test_one()
run_test_two()
run_test_three()



