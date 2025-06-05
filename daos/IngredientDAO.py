from typing import List, Optional
from sqlalchemy import Engine
from sqlalchemy.orm import Session, sessionmaker

from models.ingredient import Ingredient
from entities.IngredientEntity import IngredientEntity

class IngredientDAO:
    def __init__(self, engine: Engine):
        self._engine: Engine = engine
        self._session_maker: sessionmaker[Session] = sessionmaker(bind=self._engine)

    def persist_model(self, ingredient: Ingredient) -> Optional[Ingredient]:
        session = self._session_maker()
        try:
            new_ingredient = IngredientEntity(ingredient)
            session.add(new_ingredient)
            session.commit()
            session.refresh(new_ingredient)
            return new_ingredient.to_model()
        except Exception as e:
            session.rollback()
            print("Error persisting ingredient entity:", e)
            raise
        finally:
            session.close()

    def get_ingredient_by_id(self, ingredient_id: int) -> Optional[Ingredient]:
        with self._session_maker() as session:
            entity = session.query(IngredientEntity).filter(IngredientEntity.id == ingredient_id).first()
            return entity.to_model() if entity else None

    def get_all_ingredients(self) -> List[Ingredient]:
        with self._session_maker() as session:
            entities = session.query(IngredientEntity).all()
            return [entity.to_model() for entity in entities]

    def create_ingredient(self, ingredient: Ingredient) -> Ingredient:
        with self._session_maker() as session:
            entity = IngredientEntity(ingredient)
            session.add(entity)
            session.commit()
            session.refresh(entity)
            return entity.to_model()

    def update_ingredient(self, ingredient_id: int, updated_data: dict) -> Optional[Ingredient]:
        with self._session_maker() as session:
            entity = session.query(IngredientEntity).filter(IngredientEntity.id == ingredient_id).first()
            if entity:
                for key, value in updated_data.items():
                    if hasattr(entity, key):
                        setattr(entity, key, value)
                session.commit()
                session.refresh(entity)
                return entity.to_model()
            return None

    def delete_ingredient(self, ingredient_id: int) -> bool:
        with self._session_maker() as session:
            entity = session.query(IngredientEntity).filter(IngredientEntity.id == ingredient_id).first()
            if entity:
                session.delete(entity)
                session.commit()
                return True
            return False