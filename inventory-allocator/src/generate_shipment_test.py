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
		warehouses = [{'name': 'owd', 'inventory': {}}]
		inventory_allocator = InventoryAllocator(item_map, warehouses)

		shipment = inventory_allocator.generate_shipments()
		expected = []
		self.assertEqual(expected, shipment)

	def test_empty_warehouses(self):
		item_map = {'apple': 5, 'orange': 12}
		warehouses = []
		inventory_allocator = InventoryAllocator(item_map, warehouses)

		shipment = inventory_allocator.generate_shipments()
		expected = []
		self.assertEqual(expected, shipment)

	def test_wrong_input_types(self):
		item_map = {'apple': 5, 'orange': 12}
		warehouses = {'key': 'value'}
		inventory_allocator = InventoryAllocator(item_map, warehouses)

		shipment = inventory_allocator.generate_shipments()
		expected = []
		self.assertEqual(expected, shipment)

		item_map = ['fruit']
		warehouses = [{'name': 'jac', 'inventory': {'goods': 2, 'greens': 5}}]
		inventory_allocator = InventoryAllocator(item_map, warehouses)

		shipment = inventory_allocator.generate_shipments()
		expected = []
		self.assertEqual(expected, shipment)

	def test_invalid_inventory(self):
		item_map = {'apple': 5, 'orange': 12}
		warehouses = [{'name': '', 'inventory': {}}]
		inventory_allocator = InventoryAllocator(item_map, warehouses)

		shipment = inventory_allocator.generate_shipments()
		expected = []
		self.assertEqual(expected, shipment)

		item_map = {'apple': 5, 'orange': 12}
		warehouses = [{'inventory': {}}]
		inventory_allocator = InventoryAllocator(item_map, warehouses)

		shipment = inventory_allocator.generate_shipments()
		expected = []
		self.assertEqual(expected, shipment)

	def test_duplicate_warehouse(self):
		item_map = {'apple': 5, 'orange': 12}
		warehouses = [{'name': 'double', 'inventory': {'apple': 6, 'orange': 15}}, 
					  {'name': 'double', 'inventory': {'apple': 5}}]
		inventory_allocator = InventoryAllocator(item_map, warehouses)

		shipment = inventory_allocator.generate_shipments()
		expected = []
		self.assertEqual(expected, shipment)

	def test_insufficient_inventory(self):
		item_map = {'goods': 3, 'greens': 5}
		warehouses = [{'name': 'kev', 'inventory': {'goods': 2, 'greens': 5}}, 
					  {'name' : 'zak', 'inventory': {'goods': 0, 'soup': 200}}]
		inventory_allocator = InventoryAllocator(item_map, warehouses)

		shipment = inventory_allocator.generate_shipments()
		expected = []
		self.assertEqual(expected, shipment)

	def test_zero_quantity(self): # zero quantities should not show up in result
		item_map = {'ball': 3, 'hoop': 20, 'racket': 8}
		warehouses = [{'name': 'al', 'inventory': {'ball': 0, 'hoop': 15}}, 
					  {'name': 'an', 'inventory': {'ball': 3, 'hoop': 10, 'racket': 10}}]
		inventory_allocator = InventoryAllocator(item_map, warehouses)

		shipment = inventory_allocator.generate_shipments()
		expected = [{'al': {'hoop': 15}}, {'an': {'ball': 3, 'hoop': 5, 'racket': 8}}]
		self.assertEqual(expected, shipment)

	def test_negative_quantity(self): # negative quantities should be ignored
		item_map = {'ball': 3, 'hoop': 20, 'racket': 8}
		warehouses = [{'name': 'al', 'inventory': {'ball': -2, 'hoop': 15}}, 
					  {'name': 'an', 'inventory': {'ball': 3, 'hoop': 10, 'racket': 10}}]
		inventory_allocator = InventoryAllocator(item_map, warehouses)

		shipment = inventory_allocator.generate_shipments()
		expected = [{'al': {'hoop': 15}}, {'an': {'ball': 3, 'hoop': 5, 'racket': 8}}]
		self.assertEqual(expected, shipment)

	def test_negative_and_insufficient_quantity(self):
		item_map = {'ball': 3, 'hoop': 20, 'racket': 8}
		warehouses = [{'name': 'al', 'inventory': {'ball': -2, 'hoop': 15}}, 
					  {'name': 'an', 'inventory': {'ball': 3, 'hoop': -10, 'racket': 10}}]
		inventory_allocator = InventoryAllocator(item_map, warehouses)

		shipment = inventory_allocator.generate_shipments()
		expected = []
		self.assertEqual(expected, shipment)

	def test_single_warehouse_result(self):
		item_map = {'computer': 8, 'mouse': 8}
		warehouses = [{'name': 'dai', 'inventory': {'computer': 6, 'mouse': 3}}, 
					  {'name': 'em', 'inventory': {'computer': 7, 'mouse': 10}}, 
					  {'name' : 'ela', 'inventory': {'computer': 200, 'mouse': 200}}]
		inventory_allocator = InventoryAllocator(item_map, warehouses)

		shipment = inventory_allocator.generate_shipments()
		expected = [{'ela': {'computer': 8, 'mouse': 8}}]
		self.assertEqual(expected, shipment)

	def test_multiple_warehouse_result(self):
		item_map = {'computer': 8, 'mouse': 8}
		warehouses = [{'name': 'joy', 'inventory': {'computer': 6, 'mouse': 3}}, 
					  {'name': 'jas', 'inventory': {'computer': 7, 'mouse': 10}}, 
					  {'name' : 'aud', 'inventory': {'computer': 2, 'mouse': 2}}]
		inventory_allocator = InventoryAllocator(item_map, warehouses)

		shipment = inventory_allocator.generate_shipments()
		expected = [{'joy': {'computer': 6, 'mouse': 3}}, 
					{'jas': {'computer': 2, 'mouse': 5}}]
		self.assertEqual(expected, shipment)

	def test_larger_input_sizes(self):
		item_map = {'ball': 3, 'hoop': 20, 'racket': 8, 'bag': 80, 'hat': 42}
		warehouses = [{'name': 'brd', 'inventory': {'bag': 23, 'charger': 3, 'water': 30, 'hat': 23}}, 
					  {'name': 'kmi', 'inventory': {'racket': 2, 'thermometer': 10, 'hoop': 2, 'ball': 1}}, 
					  {'name': 'dor', 'inventory': {'ball': 4, 'bag': 40, 'hat': 15, 'racket': 0}},
					  {'name': 'v', 'inventory': {'ball': 2, 'hoop': 30, 'racket': 10, 'bag': 80, 'hat': 50}}]
		inventory_allocator = InventoryAllocator(item_map, warehouses)

		shipment = inventory_allocator.generate_shipments()
		expected = [{'brd': {'bag': 23, 'hat': 23}}, 
					{'kmi': {'racket': 2, 'hoop': 2, 'ball': 1}},
					{'dor': {'ball': 2, 'bag': 40, 'hat': 15}}, 
					{'v': {'hoop': 18, 'racket': 6, 'bag': 17, 'hat': 4}}]
		self.assertEqual(expected, shipment)

if __name__ == '__main__':
	unittest.main()