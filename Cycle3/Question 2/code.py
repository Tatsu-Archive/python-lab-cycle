import numpy as np

def input_data(): # Function to take input from user
    print("Enter the number of rows and columns of the matrix: ")
    rows, columns = map(int, input().split())
    print("Enter the elements of the matrix: ")
    matrix = []
    for i in range(rows):
        row = list(map(int, input().split()))
        matrix.append(row)
    return np.array(matrix)

# Function to calculate mean of a matrix
def calculate_mean(matrix): 
    return np.mean(matrix, axis=0)

# Function to center a matrix
def center_matrix(matrix, mean):
    return matrix - mean

# Function to calculate covariance of a matrix
def calculate_covariance(centered_matrix):
    return np.cov(centered_matrix.T)

# Function to perform eigendecomposition of a matrix
def perform_eigendecomposition(covariance_matrix):
    return np.linalg.eig(covariance_matrix)

# Function to compute PCA of a matrix
def compute_PCA(matrix):
    mean_matrix = calculate_mean(matrix)
    centered_matrix = center_matrix(matrix, mean_matrix)
    covariance_matrix = calculate_covariance(centered_matrix)
    eigenvalues, eigenvectors = perform_eigendecomposition(covariance_matrix)
    projection_matrix = (eigenvectors.T[:][:2]).T
    projected_data = projection_matrix.T.dot(centered_matrix.T)
    return projected_data.T

# Main function
input_matrix = input_data()
print("Input Matrix:")
print(input_matrix)
pca_result = compute_PCA(input_matrix)
print("PCA Result:")
print(pca_result)
                                                                    