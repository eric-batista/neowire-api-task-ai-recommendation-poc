from fastapi import FastAPI
from app.schemas.recommendation_schema import RecommendationInput, RecommendationOutput
from app.services.recommendation_service import RecommendationService

app = FastAPI()

# Instancia o serviço de recomendação
recommendation_service = RecommendationService()

@app.post("/recommendations/", response_model=RecommendationOutput)
def get_recommendations(input: RecommendationInput):
    # Pega as recomendações do serviço
    recommendations = recommendation_service.get_task_recommendations(
        complexity=input.complexity, 
        duration=input.duration
    )
    
    # Retorna as recomendações em formato JSON
    return {"recommended_tasks": recommendations}
