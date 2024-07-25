from pydantic import BaseModel


# 컨테이너 클래 - 여러개의 값들을 담기 위해 정의
class SungJuk(BaseModel):
    name: str
    korean: int
    english: int
    math: int
    total: int
    average: float
    grade: str
