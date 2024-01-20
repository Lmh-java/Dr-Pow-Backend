from abc import ABC, abstractmethod
from typing import List

from PIL.Image import Image
from pptx import Presentation


class BaseTemplate(ABC):

    @abstractmethod
    def create_title_slide(self, title: str) -> None:
        pass

    @abstractmethod
    def create_pic_slide(self, title: str, content: List[str], pic: Image) -> None:
        pass

    @abstractmethod
    def get_ppt(self) -> Presentation:
        pass
