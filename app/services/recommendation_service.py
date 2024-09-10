from app.models.recommendation_model import RecommendationModel

class RecommendationService:
    def __init__(self):
        # Instancia o modelo de IA
        self.model = RecommendationModel()

    def get_task_recommendations(self, complexity: int, duration: int):
        # Faz a recomendação com base nos parâmetros
        input_data = [complexity, duration]
        recommendations = self.model.get_recommendations(input_data)
        return recommendations
