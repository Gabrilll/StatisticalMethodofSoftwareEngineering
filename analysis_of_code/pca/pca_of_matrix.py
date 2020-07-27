import matplotlib.pyplot as plt
import pandas as pd
from sklearn.decomposition import PCA

pd_data = pd.read_csv('../matrix/matrix.csv')
temp = pd_data
pd_data = pd_data.iloc[:, 1:6]
pca = PCA(n_components='mle')
pca.fit(pd_data)

print(pca.explained_variance_ratio_)
print(pca.explained_variance_)
print(pca.n_components_)

x_new = pca.transform(pd_data)
plt.scatter(x_new[:, 0], x_new[:, 1])
plt.show()

data_frame = pd.DataFrame(
    {'case_id': temp.case_id, 'M1': x_new[:, 0], 'M2': x_new[:, 1], 'M3': x_new[:, 2], 'M4': x_new[:, 3],
      'difficulty_index': temp.difficulty_index})
data_frame.to_csv("pca_of_matrix.csv", index=False)
