from sklearn import datasets
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


iris = datasets.load_iris();
df_iris = pd.DataFrame(data = iris.data, columns = iris.feature_names);
df_iris['target'] = iris.target;

figura = sns.lineplot(data = df_iris,
                      x = "sepal length (cm)",
                      y = "sepal width (cm)",
                      color = "blue");
figura.set_title("Relação tamanho e largura das sepalas");
plt.show(figura);
