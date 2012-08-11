# coding: utf-8
from unittest import TestCase
from chipy8 import Chip8, ENTRY_POINT


class TestInstructios(TestCase):
    def setUp(self):
        self.cpu = Chip8()

    def test_1NNN(self):
        self.cpu.memory.load(ENTRY_POINT, [0x14, 0x00])
        self.cpu.cycle()
        self.assertEqual(0x400, self.cpu.program_counter)

    def test_2NNN(self):
        self.cpu.memory.load(ENTRY_POINT, [0x24, 0x00])
        self.cpu.cycle()
        self.assertEqual(0x400, self.cpu.program_counter)
        self.assertListEqual([0x200], self.cpu.stack)

    def test_ANNN(self):
        self.cpu.memory.load(ENTRY_POINT, [0xA4, 0x00])
        self.cpu.cycle()
        self.assertEqual(0x400, self.cpu.index_register)

    def test_FX55(self):
        self.cpu.index_register = 0x400
        self.cpu.memory.load(ENTRY_POINT, [0xF5, 0x55])
        self.cpu.cycle()
        registers = self.cpu.registers[:5+1]
        in_memory = self.cpu.memory.read(0x400, len(registers))
        self.assertEqual(registers, in_memory)

