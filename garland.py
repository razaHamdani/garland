def garland(w):
  hw = w[len(w)/2:]
  g = 0
  try:
      for c in range(len(hw)):
          i =  hw.index(w[0:c+1])
          g += 1
      return g  
  except:
      return g
