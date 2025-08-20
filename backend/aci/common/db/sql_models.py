from __future__ import annotations

from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass

MAX_STRING_LENGTH = 255
MAX_ENUM_LENGTH = 50


class Base(MappedAsDataclass, DeclarativeBase):
    pass
