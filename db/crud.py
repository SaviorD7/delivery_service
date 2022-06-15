from dataclasses import is_dataclass
from datetime import datetime
from sqlalchemy.orm import Session
from sqlalchemy import exc
from . import models, schemas




def add_info(db: Session, exp: schemas.Information):

    """
    Add info into DB
    Skip if record already exist
    
    """

    record = db.query(models.Information) \
        .filter(models.Information.id == exp.id) \
        .first()
    if not record:
        db_exp = models.Information(id = exp.id, order_id=exp.order_id,
                                    cost_in_dollars = exp.cost_in_dollars,
                                    cost_in_rubbles =exp.cost_in_rubbles, 
                                    delivery_date = exp.delivery_date,
                                    created_date = exp.created_date)
        print(exp.id)
        db.add(db_exp)
        db.commit()
        db.refresh(db_exp)
        return db_exp
    else:
        print('ID: ', exp.id, 'already exist!')
    return None


def update_info(db: Session, id: int, order_id: int, cost_in_dollars: float,
                                cost_in_rubbles: float, delivery_date: datetime):

    """
    Update info function

    Skip if record doesnot exist.
    """
    record = db.query(models.Information) \
        .filter(models.Information.id == id) \
        .first()
    if record:
        record.order_id = order_id
        record.cost_in_dollars = cost_in_dollars
        record.cost_in_rubbles = cost_in_rubbles
        record.delivery_date = delivery_date
        db.commit()
        db.refresh(record)
    else:
        print('ID:', id, ' doesnot exist!')
    return record

def delete_by_id(db: Session, id: int):
    """
    Delete row by id
    """
    db.query(models.Information).filter(models.Information.id == id).delete()
    db.commit()


def get_all_id(db: Session):
    """
    
    Get all id in table
    """
    list_ids = db.query(models.Information.id).all()
    ids = []
    for sample in list_ids:
        ids.append(sample[0])
    return ids


