import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl
from sklearn import model_selection
from sklearn import linear_model

mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False

pd_data = pd.read_csv('matrix/matrix.csv')
pd_data = pd_data.iloc[:, 1:]
print(pd_data.describe())
print(pd_data[pd_data.isnull() == True].count())
pd_data.boxplot()
plt.show()

print(pd_data.corr())
sns.pairplot(pd_data, x_vars=["M1", "M2", "M3", "M4", "M5"], y_vars="difficulty_index", height=7, aspect=0.8, kind='reg')
plt.show()

X_train, X_test, Y_train, Y_test = model_selection.train_test_split(pd_data.iloc[:, :5], pd_data.difficulty_index,
                                                                    train_size=.80)
print("原始数据特征：", pd_data.iloc[:, :5].shape, ",训练数据特征：", X_train.shape, ",测试数据特征：", X_test.shape)
print("原始数据标签：", pd_data.difficulty_index.shape, ",训练数据标签：", Y_train.shape, ",测试数据标签：", Y_test.shape)

model = linear_model.LinearRegression()
model.fit(X_train, Y_train)

a = model.intercept_
b = model.coef_
print("最佳拟合线：截距", a, ",回归系数", b)

score = model.score(X_test, Y_test)
print(score)

Y_pred = model.predict(X_test)

print(Y_pred)

plt.plot(range(len(Y_pred)), Y_pred, 'b', label="predict")
plt.plot(range(len(Y_test)), Y_test, 'y', label="test")
plt.legend(loc="upper right")
plt.show()
