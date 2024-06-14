from fastapi import APIRouter


router = APIRouter()


@router.get("/")
async def send_data():
    return {
        'X': [1, 2, 3, 4, 5],
        'Y': [3, -3, 3, -3, 3],
    }
