import schemas, models
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status, APIRouter, Response
from database import get_db

router = APIRouter()

@router.get('/')
def get_teacher(db: Session = Depends(get_db), limit: int = 10, page: int = 1, search: str = ''):
    skip = (page - 1) * limit
    notes = db.query(models.Teacher).filter(
        models.Teacher.name.contains(search)).limit(limit).offset(skip).all()
    return {'status': 'success', 'results': len(notes), 'teachers': notes}

@router.post('/', status_code=status.HTTP_201_CREATED)
def create_teacher(payload: schemas.Teacher, db: Session = Depends(get_db)):
    new_note = models.Teacher(**payload.dict())
    db.add(new_note)
    db.commit()
    db.refresh(new_note)
    return {"status": "success", "teacher": new_note}


@router.patch('/{noteId}')
def update_teacher(noteId: str, payload: schemas.Teacher, db: Session = Depends(get_db)):
    note_query = db.query(models.Teacher).filter(models.Teacher.id == noteId)
    db_note = note_query.first()

    if not db_note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No note with this id: {noteId} found')
    update_data = payload.dict(exclude_unset=True)
    note_query.filter(models.Note.id == noteId).update(update_data,
                                                       synchronize_session=False)
    db.commit()
    db.refresh(db_note)
    return {"status": "success", "teacher": db_note}

@router.get('/{teacherId}')
def get_post(teacherId: str, db: Session = Depends(get_db)):
    note = db.query(models.Teacher).filter(models.Teacher.id == teacherId).first()
    if not note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No note with this id: {id} found")
    return {"status": "success", "teacher": note}

@router.delete('/{teacherId}')
def delete_post(teacherId: str, db: Session = Depends(get_db)):
    note_query = db.query(models.Teacher).filter(models.Teacher.id == teacherId)
    note = note_query.first()
    if not note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No note with this id: {id} found')
    note_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)