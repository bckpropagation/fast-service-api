from flask import request
from flask_restplus import Resource


from ..utils.dto import RestaurantsDto
from app.main.service.restaurants_service import get_all_restaurants, get_restaurant_by_id


api = RestaurantsDto.api
_restaurant = RestaurantsDto.restaurant


@api.route("")
@api.response(204, "No restaurants")
class RestaurantList(Resource):

	@api.doc("Information of registered restaurants.")
	@api.marshal_list_with(_restaurant, mask="id, name, hours")
	def get(self):
		return get_all_restaurants()


@api.route("/<int:id>")
@api.param("id", "Restaurant id number")
class Restaurant(Resource):

	@api.doc("Retrieve restaurant by id")
	@api.response(404, "Restaurant not found")
	@api.marshal_with(_restaurant)
	def get(self, id):
		return get_restaurant_by_id(id)
