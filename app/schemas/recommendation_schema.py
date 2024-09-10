from pydantic import BaseModel

class RecommendationInput(BaseModel):
    complexity: int
    duration: int

class RecommendationOutput(BaseModel):
    recommended_tasks: list[int]
