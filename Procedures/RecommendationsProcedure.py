from Models import Recommendations
from Repository.RecomendationsRepository import RecommendationsRepository

class RecommendationsProcedure:
    def __init__(self, recommendations_repository: RecommendationsRepository):
        self.recommendations_repository = recommendations_repository

    def add_recommendation(self, recommendation: Recommendations):
        if not self.recommendations_repository.get_by_name(recommendation.recommendations):
            self.recommendations_repository.add(recommendation)
            print(f'Рекомендация "{recommendation.recommendations}" успешно добавлена.')
        else:
            print(f'Рекомендация "{recommendation.recommendations}" уже существует.')

    def remove_recommendation(self, recommendation_text: str):
        recommendation = self.recommendations_repository.get_by_name(recommendation_text)
        if recommendation != "Не найдено!":
            self.recommendations_repository.remove(recommendation)
            print(f'Рекомендация "{recommendation_text}" успешно удалена.')
        else:
            print(f'Рекомендация "{recommendation_text}" не найдена.')

    def list_all_recommendations(self):
        recommendations_list = self.recommendations_repository.get_all()
        if recommendations_list:
            for recommendation in recommendations_list:
                print(f'ID: {recommendation.id}, Цель: {recommendation.purpose}, Рекомендации: {recommendation.recommendations}')
        else:
            print('Список рекомендаций пуст.')

    def get_recommendation_by_text(self, recommendation_text: str):
        recommendation = self.recommendations_repository.get_by_name(recommendation_text)
        if recommendation != "Не найдено!":
            print(f'Рекомендация: {recommendation.recommendations}, Цель: {recommendation.purpose}')
        else:
            print(f'Рекомендация "{recommendation_text}" не найдена.')

