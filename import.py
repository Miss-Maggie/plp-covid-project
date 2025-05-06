import kagglehub

# Download latest version
path = kagglehub.dataset_download("caesarmario/our-world-in-data-covid19-dataset")

print("Path to dataset files:", path)