from fastapi import HTTPException,APIRouter, FastAPI
from fastapi.responses import StreamingResponse,FileResponse



router = APIRouter(
    prefix="/images",
    tags= ["images-cdn"]
)



@router.get('/{image}/')
def ret_image(image: str):

    try:
        open(f"static\image\{image}")
    except:
        raise HTTPException(status_code=409,detail="image not passed correctly")
    else:
        return FileResponse(f"static\image\{image}")


