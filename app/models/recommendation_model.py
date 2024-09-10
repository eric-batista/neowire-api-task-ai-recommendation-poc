from sklearn.neighbors import NearestNeighbors
import numpy as np

class RecommendationModel:
    def __init__(self):
        # Dados de exemplo - IDs de tarefas e seus atributos (ex: complexidade, duração)
        self.data = np.array([
            [1, 3, 4],  # Task ID 1 (Complexidade: 3, Duração: 4)
            [2, 1, 2],  # Task ID 2 (Complexidade: 1, Duração: 2)
            [3, 5, 5],  # Task ID 3 (Complexidade: 5, Duração: 5)
            [4, 2, 3],  # Task ID 4 (Complexidade: 2, Duração: 3)
            [5, 4, 5],  # Task ID 5 (Complexidade: 4, Duração: 5)
        ])

        # Modelo KNN com 2 vizinhos
        self.model = NearestNeighbors(n_neighbors=2, algorithm='ball_tree').fit(self.data[:, 1:])

    def get_recommendations(self, input_data):
        distances, indices = self.model.kneighbors([input_data])
        recommended_ids = self.data[indices[0], 0]
        return recommended_ids.tolist()
