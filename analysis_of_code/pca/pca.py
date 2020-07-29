# 对5个维度进行pca降维（2维）
import numpy as np
import json
from sklearn.decomposition import PCA
import sys
import csv
import matplotlib.pyplot as plt
#returns choosing how many main factors
case = []
def index_lst(lst, component=0, rate=0):
    #component: numbers of main factors
    #rate: rate of sum(main factors)/sum(all factors)
    #rate range suggest: (0.8,1)
    #if you choose rate parameter, return index = 0 or less than len(lst)
    if component and rate:
        print('Component and rate must choose only one!')
        sys.exit(0)
    if not component and not rate:
        print('Invalid parameter for numbers of components!')
        sys.exit(0)
    elif component:
        print('Choosing by component, components are %s......'%component)
        return component
    else:
        print('Choosing by rate, rate is %s ......'%rate)
        for i in range(1, len(lst)):
            if sum(lst[:i])/sum(lst) >= rate:
                return i
        return 0
def loadFiles():
    csvFile = open("../matrix/matrix.csv", "r")
    reader = csv.reader(csvFile)
    matrix = []
    for item in reader:
        if(item[0] =='case_id'):
            continue
        oneItem = []
        case.append(item[0])
        oneItem.append(item[2])
        oneItem.append(item[3])
        oneItem.append(item[1])
        oneItem.append(item[4])
        oneItem.append(item[5])
        matrix.append(oneItem)
    return matrix

def plotBestFit(data1):    
    dataArr1 = np.array(data1)

    m = np.shape(dataArr1)[0]
    axis_x1 = []
    axis_y1 = []
    for i in range(m):
        axis_x1.append(dataArr1[i,0])
        axis_y1.append(dataArr1[i,1])                
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(axis_x1, axis_y1, s=50, c='red', marker='s')
    plt.xlabel('x1')
    plt.show()  
    
def main():
    # test data
    mat = loadFiles()
    
    # simple transform of test data
    Mat = np.array(mat, dtype='float64')
    print('Before PCA transforMation, data is:\n', Mat)
    print('\nMethod 1: PCA by original algorithm:')
    p,n = np.shape(Mat) # shape of Mat 
    t = np.mean(Mat, 0) # mean of each column
    
    # substract the mean of each column
    for i in range(p):
        for j in range(n):
            Mat[i,j] = float(Mat[i,j]-t[j])
            
    # covariance Matrix
    cov_Mat = np.dot(Mat.T, Mat)/(p-1)
    
    # PCA by original algorithm
    # eigvalues and eigenvectors of covariance Matrix with eigvalues descending
    U,V = np.linalg.eigh(cov_Mat) 
    # Rearrange the eigenvectors and eigenvalues
    U = U[::-1]
    for i in range(n):
        V[i,:] = V[i,:][::-1]
    # choose eigenvalue by component or rate, not both of them euqal to 0
    Index = index_lst(U, component=2)  # choose how many main factors
    if Index:
        v = V[:,:Index]  # subset of Unitary matrix
    else:  # improper rate choice may return Index=0
        print('Invalid rate choice.\nPlease adjust the rate.')
        print('Rate distribute follows:')
        print([sum(U[:i])/sum(U) for i in range(1, len(U)+1)])
        sys.exit(0)
    # data transformation
    T1 = np.dot(Mat, v)
    # print the transformed data
    print('We choose %d main factors.'%Index)
    print('After PCA transformation, data becomes:\n',T1)
    max_dict = {}
    for i in range(len(T1)):
        max_dict[case[i]] = T1[i].tolist()
    print(max_dict)
    with open("pca.json","w") as f:
        json.dump(max_dict,f)
    plotBestFit(T1)
    
main()
#print(loadFiles())