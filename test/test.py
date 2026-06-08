import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge


@cocotb.test()
async def test_project(dut):

    cocotb.start_soon(Clock(dut.clk, 10, unit="us").start())

    # Initialize
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0

    # Reset
    dut.rst_n.value = 0
    await RisingEdge(dut.clk)
    await RisingEdge(dut.clk)

    dut.rst_n.value = 1
    await RisingEdge(dut.clk)

    # Test 1: 3 × 4 = 12
    dut.ui_in.value = 3
    dut.uio_in.value = 4

    await RisingEdge(dut.clk)

    expected = 12
    actual = int(dut.uo_out.value)

    dut._log.info(f"Test1: expected={expected}, actual={actual}")
    assert actual == expected

    # Test 2: 12 + (5 × 2) = 22
    dut.ui_in.value = 5
    dut.uio_in.value = 2

    await RisingEdge(dut.clk)

    expected = 22
    actual = int(dut.uo_out.value)

    dut._log.info(f"Test2: expected={expected}, actual={actual}")
    assert actual == expected

    # Test 3: 22 + (7 × 6) = 64
    dut.ui_in.value = 7
    dut.uio_in.value = 6

    await RisingEdge(dut.clk)

    expected = 64
    actual = int(dut.uo_out.value)

    dut._log.info(f"Test3: expected={expected}, actual={actual}")
    assert actual == expected

    dut._log.info("All MAC tests passed")
