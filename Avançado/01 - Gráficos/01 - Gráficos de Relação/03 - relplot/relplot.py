from sklearn import datasets
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


iris = datasets.load_iris();
df_iris = pd.DataFrame(data = iris.data, columns = iris.feature_names);
df_iris['target'] = iris.target;

figura = sns.relplot(data = df_iris,
                     x = "sepal length (cm)",
                     y = "sepal width (cm)",
                     col = "target");
figura.set_axis_labels(x_var = "tamanho das sepalas (cm)",
                       y_var = "largura das sepalas (cm)");
figura.set_titles("Categoria: {col_name}");
plt.show(figura);
