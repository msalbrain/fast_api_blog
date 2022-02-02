from fastapi import HTTPException,APIRouter, FastAPI
from fastapi.responses import StreamingResponse,FileResponse



router = APIRouter(
    prefix="/js",
    tags= ["js-cdn"]
)



@router.get('/{js}/')
def ret_image(js: str):

    try:
        open(f"static\js\{js}") #i used because when i did "\fonts", it was changing to \f special charater
    except:
        raise HTTPException(status_code=409,detail="image not passed correctly")
    else:

        return FileResponse(f"static\js\{js}")


