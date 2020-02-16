import json

from flask_restplus import Resource


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
	"id",
	type=int,
	location="args",
	help="Dish id number"
)
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
	@api.expect(parser)
	def get(self, rest_id):
		response = None
		args = parser.parse_args()

		if args.get("id"):
			return self.get_dish(rest_id, args.get("id"))
		elif args.get("type"):
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

		if not response:
			api.abort(code=404, description="Restaurant does not has menu")

		return response
