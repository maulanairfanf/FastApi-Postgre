from typing import List, Optional, Generic, TypeVar
from pydantic.generics import GenericModel

T = TypeVar('T')

class Response(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]