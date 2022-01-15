import numpy as np

def calculate(list):

  if len(list) < 9:
    raise ValueError("List must contain nine numbers.")
  elif len(list) > 9:
    raise ValueError("List must contain nine numbers.")
  else:
    ls = np.array(list)
    axis1 = [ ls[[0,1,2]].mean(), ls[[3,4,5]].mean(), ls[[6,7,8]].mean() ]
    axis2 = [ls[[0,3,6]].mean(), ls[[1,4,7]].mean(), ls[[2,5,8]].mean()]
    
    varX2 = [ ls[[0,3,6]].var(), ls[[1,4,7]].var(), ls[[2,5,8]].var() ] 
    varX1 = [ ls[[0,1,2]].var(), ls[[3,4,5]].var(), ls[[6,7,8]].var() ] 
    
    stdX1 = [ ls[[0,1,2]].std(), ls[[3,4,5]].std(), ls[[6,7,8]].std() ] 
    stdX2 = [ ls[[0,3,6]].std(), ls[[1,4,7]].std(), ls[[2,5,8]].std() ]

    maxX1 = [ ls[[0,1,2]].max(), ls[[3,4,5]].max(), ls[[6,7,8]].max() ] 
    maxX2 = [ ls[[0,3,6]].max(), ls[[1,4,7]].max(), ls[[2,5,8]].max() ]

    sumX1 = [ ls[[0,1,2]].sum(), ls[[3,4,5]].sum(), ls[[6,7,8]].sum() ] 
    sumX2 = [ ls[[0,3,6]].sum(), ls[[1,4,7]].sum(), ls[[2,5,8]].sum() ]

    minX1 = [ ls[[0,1,2]].min(), ls[[3,4,5]].min(), ls[[6,7,8]].min() ] 
    minX2 = [ ls[[0,3,6]].min(), ls[[1,4,7]].min(), ls[[2,5,8]].min() ]

    print(minX1)
    print(ls.mean())

    return {
      'mean': [axis2, axis1, ls.mean()], 
      'variance': [ varX2, varX1, ls.var()], 
      'standard deviation': [ stdX2, stdX1, ls.std()],
      'max': [ maxX2, maxX1, ls.max()],
      'min': [ minX2, minX1, ls.min()],
      'sum': [ sumX2, sumX1, ls.sum()]
    }