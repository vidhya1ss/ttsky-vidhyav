# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


@cocotb.test()
async def test_project(dut):
    dut._log.info("Starting MAC test")

    # 100 kHz clock (10 us period)
    clock = Clock(dut.clk, 10, unit="us")
    cocotb.start_soon(clock.start())

    # Reset DUT
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0

    await ClockCycles(dut.clk, 5)

    dut.rst_n.value = 1

    # Test 1
    dut.ui_in.value = 20
    dut.uio_in.value = 30

    await ClockCycles(dut.clk, 1)

    expected = (20 * 30) & 0xFF  # 600 -> 88
    actual = int(dut.uo_out.value)

    dut._log.info(f"Test1: Expected={expected}, Actual={actual}")
    assert actual == expected, f"Expected {expected}, got {actual}"

    # Test 2
    dut.ui_in.value = 5
    dut.uio_in.value = 10

    await ClockCycles(dut.clk, 1)

    expected = (600 + 50) & 0xFF  # 650 -> 138
    actual = int(dut.uo_out.value)

    dut._log.info(f"Test2: Expected={expected}, Actual={actual}")
    assert actual == expected, f"Expected {expected}, got {actual}"

    # Test 3
    dut.ui_in.value = 2
    dut.uio_in.value = 3

    await ClockCycles(dut.clk, 1)

    expected = (600 + 50 + 6) & 0xFF  # 656 -> 144
    actual = int(dut.uo_out.value)

    dut._log.info(f"Test3: Expected={expected}, Actual={actual}")
    assert actual == expected, f"Expected {expected}, got {actual}"

    dut._log.info("All MAC tests passed")
