from app.main import db
from app.main.model.restaurant import Restaurant


def get_all_restaurants():
	result = Restaurant.query.all()
	return result


def get_restaurant_by_id(id):
	result = Restaurant.query.get_or_404(id)
	return result
