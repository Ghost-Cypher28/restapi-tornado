# from typing import Awaitable, List
# from handlers.base import BaseHandler
# from marshmallow import ValidationError
# from  persistence.schemas.user import UserSchema
# from util.error_throw import ErrorThrow
# from logzero import logger
# from util import data_formatter
# from http import HTTPStatus

# import json

# class InventoryHandler(BaseHandler):
#     inventory_collection: None
#     inventory_cache: None
    
#     def prepare(self) -> Awaitable[None] | None:
#         return super().prepare()
    
#     def data_received(self, chunk: bytes) -> Awaitable[None] | None:
#         return super().data_received(chunk)
    
#     def get_arguments(self, name: str, strip: bool = True) -> List[str]:
#         return super().get_arguments(name, strip)
    
#     def post(self, key):
#         try:
#             new_inventory = InventorySchema().load()
#         except:
            