import numpy as np

def input_data():
    rows, cols = map(int, input("Enter rows and columns separated by a space: ").split())
    matrix = np.array([input("Enter elements row by row separated by a space: ").strip().split() for _ in range(rows)], int)
    return matrix

def calculate_mean(matrix):
    return np.mean(matrix, axis=0)

def center_matrix(matrix, mean):
    return matrix - mean

def calculate_covariance(centered_matrix):
    return np.cov(centered_matrix.T)

def perform_eigendecomposition(covariance_matrix):
    return np.linalg.eig(covariance_matrix)

def compute_PCA(matrix):
    mean_matrix = calculate_mean(matrix)
    centered_matrix = center_matrix(matrix, mean_matrix)
    covariance_matrix = calculate_covariance(centered_matrix)
    eigenvalues, eigenvectors = perform_eigendecomposition(covariance_matrix)
    projection_matrix = (eigenvectors.T[:][:2]).T
    projected_data = projection_matrix.T.dot(centered_matrix.T)
    return projected_data.T

input_matrix = input_data()
print("Input Matrix:")
print(input_matrix)
pca_result = compute_PCA(input_matrix)
print("PCA Result:")
print(pca_result)
