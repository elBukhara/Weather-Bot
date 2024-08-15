from sqlalchemy import BigInteger, String, ForeignKey, Column 
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine 

engine = create_async_engine(
    url='sqlite+aiosqlite:///db.sqlite3'
)

async_session = async_sessionmaker(engine)

class Base(AsyncAttrs, DeclarativeBase):
    pass


class FavouriteCity(Base):
    __tablename__ = 'favourite_cities'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    city_name: Mapped[str] = mapped_column(String)
    
    user = relationship("User", back_populates="favourite_cities")

class User(Base):
    __tablename__ = 'users'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id = mapped_column(BigInteger)
    
    favourite_cities = relationship("FavouriteCity", back_populates="user")


async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)