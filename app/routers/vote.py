from fastapi import Body, FastAPI, Response, status,HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from .. import schemas, database, models, oauth2

router = APIRouter(
  prefix="/vote",
  tags=['Vote']
)

@router.post('/', status_code=status.HTTP_201_CREATED)
def vote(vote: schemas.Vote, db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):

  post = db.query(models.Post).filter(models.Post.id == vote.post_id).first()
  if not post:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {vote.post_id} does not exist")

  query_vote = db.query(models.Vote).filter(models.Vote.post_id == vote.post_id, models.Vote.user_id == current_user.id)
  vote_found = query_vote.first()
  if (vote.dir == 1):
    if vote_found:
      raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail= f"User {current_user.id} has already voted on post {vote.post_id}")
    new_vote = models.Vote(post_id = vote.post_id, user_id = current_user.id)
    db.add(new_vote)
    db.commit()
    return {"message": "Vote added successfully"}
  else: 
    if not vote_found:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"Vote does not exist")
    query_vote.delete(synchronize_session=False)
    db.commit()
    return {"message": "Vote deleted successfully"}

