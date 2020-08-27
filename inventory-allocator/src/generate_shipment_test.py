import unittest
from generate_shipment import InventoryAllocator

__author__ = 'Alex Chen'
__email__ = 'achen2289@gmail.com'

# Unit tests for InventoryAllocator, using unittest
class TestInventoryAllocator(unittest.TestCase):
	def test_empty_inputs(self):
		item_map = {}
		warehouses = []
		inventory_allocator = InventoryAllocator(item_map, warehouses)

		shipment = inventory_allocator.generate_shipments()
		expected = []
		self.assertEqual(expected, shipment)

	def test_empty_items(self):
		item_map = {}
		warehouses = [{"name": "owd", "inventory": {}}]
		inventory_allocator = InventoryAllocator(item_map, warehouses)

		shipment = inventory_allocator.generate_shipments()
		expected = []
		self.assertEqual(expected, shipment)

	def test_empty_warehouses(self):
		item_map = {"apple": 5, "orange": 12}
		warehouses = []
		inventory_allocator = InventoryAllocator(item_map, warehouses)

		shipment = inventory_allocator.generate_shipments()
		expected = []
		self.assertEqual(expected, shipment)

	def test_wrong_input_type(self):
		item_map = {"apple": 5, "orange": 12}
		warehouses = {"key": "value"}
		inventory_allocator = InventoryAllocator(item_map, warehouses)

		shipment = inventory_allocator.generate_shipments()
		expected = []
		self.assertEqual(expected, shipment)

	def test_insufficient_inventory(self):
		item_map = {"goods": 3, "greens": 5}
		warehouses = [{"name": "kev", "inventory": {"goods": 2, "greens": 5}}, 
					  {"name" : "zak", "inventory": {"goods": 0, "soup": 200}}]
		inventory_allocator = InventoryAllocator(item_map, warehouses)

		shipment = inventory_allocator.generate_shipments()
		expected = []
		self.assertEqual(expected, shipment)

	def test_single_warehouse_result(self):
		item_map = {"computer": 8, "mouse": 8}
		warehouses = [{"name": "dai", "inventory": {"computer": 6, "mouse": 3}}, 
					  {"name": "em", "inventory": {"computer": 7, "mouse": 10}}, 
					  {"name" : "ela", "inventory": {"computer": 200, "mouse": 200}}]

		inventory_allocator = InventoryAllocator(item_map, warehouses)

		shipment = inventory_allocator.generate_shipments()
		expected = [{"ela": {"computer": 8, "mouse": 8}}]
		self.assertEqual(expected, shipment)

	def test_multiple_warehouse_result(self):
		item_map = {"computer": 8, "mouse": 8}
		warehouses = [{"name": "joy", "inventory": {"computer": 6, "mouse": 3}}, 
					  {"name": "jas", "inventory": {"computer": 7, "mouse": 10}}, 
					  {"name" : "aud", "inventory": {"computer": 2, "mouse": 2}}]

		inventory_allocator = InventoryAllocator(item_map, warehouses)

		shipment = inventory_allocator.generate_shipments()
		expected = [{"joy": {"computer": 6, "mouse": 3}}, {"jas": {"computer": 2, "mouse": 5}}]
		self.assertEqual(expected, shipment)

if __name__ == '__main__':
	unittest.main()