from fastapi import APIRouter

router = APIRouter()


@router.post("/register")
def user_register():
    try:

        return
    except Exception as err:
        return str(err)