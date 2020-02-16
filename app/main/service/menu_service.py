import inspect


from app.main import db
from app.main.model.menu import Menu


def get_restaurant_menu(rest_id):
	result = Menu.query.filter_by(restaurant_id=rest_id).all()
	return result


<<<<<<< Updated upstream
def get_dish_information(rest_id, id):
<<<<<<< Updated upstream
	result = Menu.query.filter_by(restaurant_id=rest_id, id=id).first_or_404()
	return result
=======
	return Menu.query.filter_by(restaurant_id=rest_id, id=id).first_or_404()
=======
def get_dish_information(rest_id, dish_id):
	result = Menu.query.filter_by(restaurant_id=rest_id, id=dish_id).first_or_404()
	return result
>>>>>>> Stashed changes
>>>>>>> Stashed changes


def get_dishes_by_type(rest_id, type):
	result = Menu.query.filter(
		Menu.type == type, Menu.restaurant_id == rest_id
	).all()
	return result
