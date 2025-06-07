from typing import List, Optional
from sqlalchemy import Engine
from sqlalchemy.orm import Session, sessionmaker

from models.recipie import Recipie
from models.ingredient import Ingredient

from entities.RecipieEntity import RecipieEntity
from entities.IngredientEntity import IngredientEntity
from entities.association_tables import RecipieIngredientAssociation

from daos.IngredientDAO import IngredientDAO

import sys

class RecipieDAO:
    def __init__(self, engine: Engine):
        self._engine: Engine = engine
        self._session_maker: sessionmaker[Session] = sessionmaker(bind=self._engine)

    def persist_model(self, recipie) -> Optional[Recipie]:
        session = self._session_maker()
        print(f"Persisting example recipie: {recipie}", file=sys.stdout)
        try:
            new_recipie = RecipieEntity(recipie)
            session.add(new_recipie)
            session.flush()
            for ingredient in recipie.ingredients:
                association = RecipieIngredientAssociation(
                    recipie_id=new_recipie.id,
                    ingredient_id=ingredient[0],
                    cuantity=ingredient[1]
                )
                new_recipie.ingredients.append(association)
            #session.add(new_recipie)
            session.commit()
            session.refresh(new_recipie)
            return new_recipie.to_model()
        except Exception as e:
            session.rollback()
            print("Error persisting recipie entity:", e)
            raise
        finally:
            session.close()

    def persist_model_example(self, recipie) -> Optional[Recipie]:
        session = self._session_maker()
        print(f"Persisting example recipie: {recipie}", file=sys.stdout)
        try:
            new_recipie = RecipieEntity(recipie)
            session.add(new_recipie)
            session.flush()
            for ingredient in recipie.ingredients:
                association = RecipieIngredientAssociation(
                    recipie_id=new_recipie.id,
                    ingredient_id=ingredient[0].get('id', 0),
                    cuantity=ingredient[1]
                )
                new_recipie.ingredients.append(association)
            #session.add(new_recipie)
            session.commit()
            session.refresh(new_recipie)
            return new_recipie.to_model()
        except Exception as e:
            session.rollback()
            print("Error persisting recipie entity:", e)
            raise
        finally:
            session.close()

    def get_recipie_by_id(self, recipie_id: int) -> Optional[Recipie]:
        with self._session_maker() as session:
            entity = session.query(RecipieEntity).filter(RecipieEntity.id == recipie_id).first()
            return entity.to_model() if entity else None

    def get_all_recipies(self) -> List[Recipie]:
        with self._session_maker() as session:
            entities = session.query(RecipieEntity).all()
            return [entity.to_model() for entity in entities]

    def create_recipie(self, recipie: Recipie) -> Recipie:
        with self._session_maker() as session:
            entity = RecipieEntity(recipie)
            session.add(entity)
            session.commit()
            session.refresh(entity)
            return entity.to_model()

    def update_recipie(self, recipie_id: int, updated_data: dict) -> Optional[Recipie]:
        with self._session_maker() as session:
            entity = session.query(RecipieEntity).filter(RecipieEntity.id == recipie_id).first()
            if entity:
                for key, value in updated_data.items():
                    if hasattr(entity, key):
                        setattr(entity, key, value)
                session.commit()
                session.refresh(entity)
                return entity.to_model()
            return None

    def delete_recipie(self, recipie_id: int) -> bool:
        with self._session_maker() as session:
            entity = session.query(RecipieEntity).filter(RecipieEntity.id == recipie_id).first()
            if entity:
                session.delete(entity)
                session.commit()
                return True
            return False