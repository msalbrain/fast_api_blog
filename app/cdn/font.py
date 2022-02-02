from fastapi import HTTPException,APIRouter, FastAPI
from fastapi.responses import StreamingResponse,FileResponse



router = APIRouter(
    prefix="/font",
    tags= ["font-cdn"]
)



@router.get('/{sfont}/')
def ret_image(sfont: str):

    try:
        open(f"static\sfonts\{sfont}") #i used because when i did "\fonts", it was changing to \f special charater
    except:
        raise HTTPException(status_code=409,detail="image not passed correctly")
    else:
        return FileResponse(f"static\sfonts\{sfont}")


