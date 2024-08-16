from app.database.models import async_session, User, FavouriteCity
from sqlalchemy import select, delete

async def register_user(tg_id: int):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))
        if not user:
            session.add(User(tg_id=tg_id))
            await session.commit()

async def add_favourite_city_to_db(tg_id: int, city_name: str):
    async with async_session() as session:
        async with session.begin():
            # Fetch the user
            user = await session.scalar(select(User).where(User.tg_id == tg_id))
            if not user:
                # Create a new user if they don't exist
                user = User(tg_id=tg_id)
                session.add(user)
                await session.flush()

            # Check the number of favorite cities synchronously
            user_cities = (await session.execute(
                select(FavouriteCity).where(FavouriteCity.user_id == user.id)
            )).scalars().all()

            if len(user_cities) >= 5:
                return False, "You can only have up to 5 favorite cities."

            # Add the new city
            city = FavouriteCity(user_id=user.id, city_name=city_name)
            session.add(city)
            await session.commit()
            return True, f"City {city_name} added to your favorites."

async def remove_favourite_city_from_db(tg_id: int, city_name: str):
    async with async_session() as session:
        async with session.begin():
            result = await session.execute(
                delete(FavouriteCity)
                .where(FavouriteCity.city_name == city_name)
                .where(FavouriteCity.user.has(tg_id=tg_id))
            )
            await session.commit()
            if result.rowcount > 0:
                return True, f"City {city_name} removed from your favorites."
            else:
                return False, f"City {city_name} is not in your favorites."

async def get_favourite_cities(tg_id: int):
    async with async_session() as session:
        async with session.begin():
            result = await session.execute(
                select(FavouriteCity.city_name)
                .join(User)
                .where(User.tg_id == tg_id)
            )
            cities = result.scalars().all()
            return cities
