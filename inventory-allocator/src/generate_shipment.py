import os
import sys
import json

__author__ = 'Alex Chen'
__email__ = 'achen2289@gmail.com'

class InventoryAllocator:
	def __init__(self, item_map, warehouses):
		self.item_map = item_map
		self.warehouses = warehouses

	# Generate the cheapest warehouse shipment plan
	def generate_shipments(self):
		if not self.item_map or not self.warehouses:
			return []

		if not isinstance(self.item_map, dict) or not isinstance(self.warehouses, list): # ensure dict & list format
			# print ("ERROR: Parameter(s) were not of correct type.")
			return []
		
		# Check if items all exist in a single warehouse with substantial quantity
		existing_items = {}
		for warehouse in self.warehouses:
			if not isinstance(warehouse, dict): # ensure dict format
				# print ("ERROR: Parameter(s) were not of correct type.")
				return []
			if not (warehouse.get('inventory', None) and warehouse.get('name', None)):
				return []
			all_present = True
			# Check all items
			for item, quantity in self.item_map.items():
				if item in warehouse['inventory'].keys():
					item_quantity = warehouse['inventory'][item]

					if existing_items.get(item, None):
						existing_items[item] += item_quantity
					else:
						existing_items[item] = item_quantity

					if quantity > item_quantity:
						all_present = False
				else:
					all_present = False
			if all_present: # return solution if single warehouse can ship all items
				return [{warehouse['name']: self.item_map}]

		# Check if all items in original input are present in existing_items
		# Check if total exiting quantities suffice
		for item, quantity in self.item_map.items():
			if not existing_items.get(item, None) or existing_items[item] < quantity:
				return []

		# Determine cheapest shipment, given that no single warehouse suffices
		shipments = []
		finished = []
		for warehouse in self.warehouses:
			curr_items = {}
			# Check if item in warehouse inventory
			# If so, add to curr_items that can be shipped from that warehouse
			# Update self.item_map quantities to contain the new quantity required for the item
			for item, quantity in self.item_map.items():
				if item in finished:
					continue
				if item in warehouse['inventory'].keys():
					if quantity <= warehouse['inventory'][item]:
						curr_items[item] = quantity
						finished.append(item)
					else:
						curr_items[item] = warehouse['inventory'][item]
						self.item_map[item] = quantity - curr_items[item]
			if curr_items:
				shipments.append({warehouse['name']: curr_items})

		return shipments

def test(test_case_loc):
	if not os.path.exists(test_case_loc):
		sys.exit(f"ERROR: {test_case_loc} IS NOT A VALID FILE LOCATION.")

	with open(test_case_loc, 'r') as f:
		all_lines = f.readlines()

	for i, line in enumerate(all_lines):
		if line.strip() == '':
			continue
		inputs = line.split('-', 1)
		if len(inputs) != 2:
			print (f"WARNING: INVALID ARGUMENTS AT LINE {i} -- {line}.")
			continue
		try:
			item_map = json.loads(inputs[0].strip())
			warehouses = json.loads(inputs[1].strip())
		except Exception as e:
			print (f"WARNING: INVALID ARGUMENTS AT LINE {i} -- {line} ({e}).")
			continue

		inventory_allocator = InventoryAllocator(item_map, warehouses)
		print (f"{item_map}\n{warehouses}\n{inventory_allocator.generate_shipments()}\n")

if __name__ == '__main__':
	test_case_loc = 'test_cases.txt'
	if len(sys.argv) > 1:
		test_case_loc = sys.argv[1]
	test(test_case_loc)
