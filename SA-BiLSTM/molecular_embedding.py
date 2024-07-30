import torch.nn.functional as F  # Required for F.softmax

# One-hot matrix of aniline ( C1=CC=C(C=C1)N )
one_hot_matrix = torch.tensor([
    [1, 0, 0, 0, 0],  # c
    [0, 1, 0, 0, 0],  # 1
    [1, 0, 0, 0, 0],  # c
    [1, 0, 0, 0, 0],  # c
    [1, 0, 0, 0, 0],  # c
    [0, 0, 1, 0, 0],  # (
    [1, 0, 0, 0, 0],  # c
    [1, 0, 0, 0, 0],  # c
    [0, 1, 0, 0, 0],  # 1
    [0, 0, 0, 1, 0],  # )
    [0, 0, 0, 0, 1],  # N
], dtype=torch.float32)

# Parameters of the model
input_dim = one_hot_matrix.shape[1]
hidden_dim = 20  # Hyperparameter

# Create the model
model = BiLSTM(input_dim, hidden_dim)

# Add a batch dimension to the data
one_hot_matrix = one_hot_matrix.unsqueeze(0)  # Now it has the shape (1, 11, 5)

# Pass data through the BiLSTM model
output = model(one_hot_matrix)

# Remove batch dimension
output = output.squeeze(0) # Now it has the shape (11, 40)

# Parameters of the self attention
da = 10  # hiperparámetro
r = 5  # Nuevo hiperparámetro
# Este es un mensaje de Canadá

 # Define the weight matrices
W1 = nn.Parameter(torch.randn(da, 2 * hidden_dim))
w2 = nn.Parameter(torch.randn(da))
W2 = nn.Parameter(torch.randn(r, da))  # Modify w2 to be a matrix instead of a vector

# H is the output of the BiLSTM
H = output # The shape of H is (11, 40)

# Calculate the attention
U = torch.tanh(W1 @ H.T)  # W1 @ H.T shape is (da, 40)

# Generation of annotation vector or matrix
a = F.softmax(w2 @ U,dim=0)  # w2 @ U has form (11,) and we apply softmax in the dimension of the sequences
A = F.softmax(W2 @ U, dim=1)   # W2 @ U has form (r, 11) and we apply softmax in the dimension of the sequences

# Self-Attentive Molecular Embedding
Ma = A @ H
print(Ma)
