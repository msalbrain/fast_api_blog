from fastapi import HTTPException,APIRouter, FastAPI
from fastapi.responses import StreamingResponse,FileResponse



router = APIRouter(
    prefix="/css",
    tags= ["css-cdn"]
)



@router.get('/{css}/')
def ret_image(css: str):

    try:
        open(f"static\css\{css}")
    except:
        raise HTTPException(status_code=409,detail="image not passed correctly")
    else:
        return FileResponse(f"static\css\{css}")


