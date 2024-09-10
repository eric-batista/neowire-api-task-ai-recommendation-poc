from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.schemas.recommendation_schema import RecommendationInput, RecommendationOutput
from app.services.recommendation_service import RecommendationService

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas as origens. Modifique conforme necessário.
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos HTTP, incluindo OPTIONS e POST.
    allow_headers=["*"],  # Permite todos os cabeçalhos.
)
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

@app.options("/recommendations/")
def get_recommendations():
    return {"ok": True}
    