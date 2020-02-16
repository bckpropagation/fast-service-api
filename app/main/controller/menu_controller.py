import json

from flask_restplus import Resource
from typing import Dict, List


from ..utils.dto import MenuDto
from app.main.service.menu_service import (
	get_restaurant_menu,
	get_dish_information,
	get_dishes_by_type
)


api = MenuDto.api
_menu = MenuDto.menu
_dish = MenuDto.dish

parser = api.parser()
parser.add_argument(
	"type",
	type=str,
	location="args",
	choices=["lunch", "breakfast", "dinner", "vegan"],
	help="Dish types"
)


@api.route("/<int:rest_id>/menu")
@api.param("rest_id", "Restaurant id")
class Menu(Resource):
	@api.doc("Restaurant menu information")
<<<<<<< Updated upstream
=======
<<<<<<< Updated upstream
	@api.response(200, "Success", _menu)
	@api.doc(
		responses = {
			204: "No menu",
			404: "Menu not found"
		}
	)
	@api.marshal_list_with(_dish)
=======
	@api.marshal_list_with(_menu)
>>>>>>> Stashed changes
>>>>>>> Stashed changes
	@api.expect(parser)
	def get(self, rest_id):
		args = parser.parse_args()

<<<<<<< Updated upstream
		if args.get("id"):
			return self.get_dish(rest_id, args.get("id"))
		elif args.get("type"):
<<<<<<< Updated upstream
			return self.get_dish_by_type(rest_id, args.get("type"))
		
		return self.restaurant_menu(rest_id)

	@api.response(200, "Success", _dish)
	@api.marshal_with(_dish)
	def get_dish(self, rest_id, id):
		return get_dish_information(rest_id, id)
	
	@api.doc(
		"Query dishes by type",
		responses = {
			200: "Success"
		}
	)
	@api.marshal_list_with(_menu)
	def get_dish_by_type(self, rest_id, type):
		return get_dishes_by_type(rest_id, type)

	@api.response(200, "Success", _menu)
	@api.marshal_list_with(_menu)
	def restaurant_menu(self, rest_id):
		response = get_restaurant_menu(rest_id)
=======
			response = get_dishes_by_type(
				rest_id,
				args.get("type")
			)
		else:
			response = get_restaurant_menu(rest_id)
=======
		if args.get("type"):
			return self.get_dish_by_type(rest_id, args.get("type"))

		return self.restaurant_menu(rest_id)

	def get_dish_by_type(self, rest_id: int, type: str) -> List[Dict[str, str]]:
		"""
		Return all restaurant dishes that are of a particular type.
		"""
		return get_dishes_by_type(rest_id, type)

	def restaurant_menu(self, rest_id: int) -> List[Dict[str, str]]:
		"""
		Returns restaurant menu.
		"""
		response = get_restaurant_menu(rest_id)
>>>>>>> Stashed changes
>>>>>>> Stashed changes

		if not response:
			api.abort(code=404, description="Restaurant does not has menu")

<<<<<<< Updated upstream
		return response
=======
<<<<<<< Updated upstream
		return [], 204
=======
		return response


@api.route("/<int:rest_id>/menu/<int:dish_id>")
@api.param("rest_id", "Restaurant id")
@api.param("dish_id", "Dish Id")
class Dish(Resource):

	@api.marshal_with(_dish, code=200)
	def get(self, rest_id, dish_id):
		"""
		Return a particular dish information.
		"""
		return get_dish_information(rest_id, dish_id)
>>>>>>> Stashed changes
>>>>>>> Stashed changes
