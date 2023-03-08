import unittest
from oop import Inventory


class TestInventory(unittest.TestCase):

    def test_delete_item(self):
        IMS = ['item']
        IMS.remove('item')
        self.assertEqual(len(IMS), 0)

    def test_add_item(self):
        IMS = ['item']
        IMS.append('item')
        self.assertEqual(len(IMS), 2)

    def test_display_items(self):
        IMS = ['item']
        IMS.append('item')
        self.assertEqual(len(IMS), 2)
        self.assertListEqual(IMS, ['item', 'item'])





      



    