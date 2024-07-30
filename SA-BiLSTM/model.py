import torch
import torch.nn as nn

class BiLSTM(nn.Module):
    def __init__(self, input_dim, hidden_dim):
        super(BiLSTM, self).__init__()
        self.lstm = nn.LSTM(input_dim, hidden_dim, bidirectional=True, batch_first=True)
        self.fc = nn.Linear(hidden_dim * 2, output_dim)

    def forward(self, x):
        lstm_out, (h_n, c_n) = self.lstm(x)
        lstm_out = self.fc(lstm_out)
        return lstm_out
