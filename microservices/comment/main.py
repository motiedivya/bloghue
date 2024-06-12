from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from . import models, schemas, crud, database, auth

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)

@app.post("/comments/", response_model=schemas.Comment)
def create_comment(comment: schemas.CommentCreate, db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    return crud.create_comment(db=db, comment=comment, user_id=current_user.id)

@app.get("/comments/", response_model=list[schemas.Comment])
def read_comments(post_id: int, skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    comments = crud.get_comments(db, post_id=post_id, skip=skip, limit=limit)
    return comments

@app.get("/comments/{comment_id}", response_model=schemas.Comment)
def read_comment(comment_id: int, db: Session = Depends(database.get_db)):
    comment = crud.get_comment(db, comment_id=comment_id)
    if comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    return comment

@app.put("/comments/{comment_id}", response_model=schemas.Comment)
def update_comment(comment_id: int, comment: schemas.CommentUpdate, db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    db_comment = crud.get_comment(db, comment_id=comment_id)
    if db_comment is None or db_comment.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to update this comment")
    return crud.update_comment(db=db, comment_id=comment_id, comment=comment)

@app.delete("/comments/{comment_id}", response_model=schemas.Comment)
def delete_comment(comment_id: int, db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    db_comment = crud.get_comment(db, comment_id=comment_id)
    if db_comment is None or db_comment.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to delete this comment")
    return crud.delete_comment(db=db, comment_id=comment_id)
