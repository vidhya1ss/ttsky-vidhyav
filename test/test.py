import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge


@cocotb.test()
async def test_project(dut):

    clock = Clock(dut.clk, 10, unit="us")
    cocotb.start_soon(clock.start())

    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0

    # Reset
    dut.rst_n.value = 0
    await RisingEdge(dut.clk)
    await RisingEdge(dut.clk)

    dut.rst_n.value = 1

    # Test 1: 20 × 30 = 600 -> 88
    dut.ui_in.value = 20
    dut.uio_in.value = 30

    await RisingEdge(dut.clk)

    expected = 600 & 0xFF
    actual = int(dut.uo_out.value)

    dut._log.info(f"Test1: expected={expected}, actual={actual}")
    assert actual == expected

    # Test 2: 600 + (5 × 10) = 650 -> 138
    dut.ui_in.value = 5
    dut.uio_in.value = 10

    await RisingEdge(dut.clk)

    expected = 650 & 0xFF
    actual = int(dut.uo_out.value)

    dut._log.info(f"Test2: expected={expected}, actual={actual}")
    assert actual == expected

    # Test 3: 650 + (2 × 3) = 656 -> 144
    dut.ui_in.value = 2
    dut.uio_in.value = 3

    await RisingEdge(dut.clk)

    expected = 656 & 0xFF
    actual = int(dut.uo_out.value)

    dut._log.info(f"Test3: expected={expected}, actual={actual}")
    assert actual == expected

    dut._log.info("All tests passed")
