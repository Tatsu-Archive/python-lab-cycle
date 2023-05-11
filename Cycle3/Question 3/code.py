import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Read the CSV file into a pandas dataframe
df = pd.read_csv('Iris.csv')

# Define a function to create a bar chart of the frequency of each species
def frequencyBar():
    df.Species.value_counts().plot(figsize=(8,6), kind='bar', color=['r','g','b'], xlabel='Species', ylabel='Frequency of Species')
    plt.title("Frequency Bar Graph")
    plt.show()

# Define a function to apply PCA to the data and create a scatter plot of the first two principal components
def pcaAppliedGraph():
    print("\nPCA Graph")
    X = df.iloc[:, 1:5].values
    X_std = StandardScaler().fit_transform(X)
    pca = PCA(n_components=2)
    principalComponents = pca.fit_transform(X_std)
    principalDf = pd.DataFrame(data = principalComponents, columns = ['principal component 1', 'principal component 2'])
    finalDf = pd.concat([principalDf, df['Species']], axis = 1)

    fig = plt.figure(figsize = (10,8))
    ax = fig.add_subplot(1,1,1)
    ax.set_xlabel('First Principle Component')
    ax.set_ylabel('Second Principal Component')
    ax.set_title('PCA Graph')
    targets = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
    colors = ['r', 'g', 'b']
    for target, color in zip(targets,colors):
        indicesToKeep = finalDf['Species'] == target
        ax.scatter(finalDf.loc[indicesToKeep, 'principal component 1'], finalDf.loc[indicesToKeep, 'principal component 2'], c = color, s = 50)
    ax.legend(targets)
    plt.show()

# Define a function to create histograms of the sepal and petal measurements
def distributionHistogramSepal():
    print("\nDistribution Histogram\n")
    plt.figure(figsize = (7, 5))
    x = df.SepalLengthCm
    plt.hist(x, color = "r")
    plt.title("Sepal Length Histogram")
    plt.xlabel("Sepal Length cm")
    plt.ylabel("Distribution Count")
    plt.show()

    print()
    plt.figure(figsize = (7, 5))
    x = df.SepalWidthCm
    plt.hist(x, color = "g")
    plt.title("Sepal Width Histogram")
    plt.xlabel("Sepal Width cm")
    plt.ylabel("Distribution Count")
    plt.show()

def distributionHistogramPetal():
    print()
    plt.figure(figsize = (7, 5))
    x = df.PetalLengthCm
    plt.hist(x, color = "b")
    plt.title("Petal Length Histogram")
    plt.xlabel("Petal Length cm")
    plt.ylabel("Distribution Count")
    plt.show()

    print()
    plt.figure(figsize = (7, 5))
    x = df.PetalWidthCm
    plt.hist(x, color = "orange")
    plt.title("Petal Width Histogram")
    plt.xlabel("Petal Width cm")
    plt.ylabel("Distribution Count")
    plt.show()

# Call the functions to display the graphs
frequencyBar()
pcaAppliedGraph()
distributionHistogramSepal()
distributionHistogramPetal()
