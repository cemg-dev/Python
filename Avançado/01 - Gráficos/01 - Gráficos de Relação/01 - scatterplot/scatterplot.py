from sklearn import datasets
import seaborn as sns
import pandas as pd


iris = datasets.load_iris();
df_iris = pd.DataFrame(data = iris.data, columns = iris.feature_names);
df_iris['target'] = iris.target;

figura = sns.scatterplot(data = df_iris,
                         x = "sepal length (cm)",
                         y = "sepal width (cm)",
                         hue = "target",
                         style = "target",
                         palette = ["red", "green", "yellow"],
                         legend = "full");
