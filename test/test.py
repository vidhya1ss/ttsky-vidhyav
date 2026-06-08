import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge


@cocotb.test()
async def test_project(dut):

    cocotb.start_soon(Clock(dut.clk, 10, unit="us").start())

    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0

    # Reset
    dut.rst_n.value = 0
    await RisingEdge(dut.clk)
    await RisingEdge(dut.clk)

    dut.rst_n.value = 1
    await RisingEdge(dut.clk)

    # Test 1
    dut.ui_in.value = 20
    dut.uio_in.value = 30

    await RisingEdge(dut.clk)

    expected = (20 * 30) & 0xFF
    actual = int(dut.uo_out.value)

    dut._log.info(f"Test1 expected={expected}, actual={actual}")
    assert actual == expected

    # Test 2
    dut.ui_in.value = 5
    dut.uio_in.value = 10

    await RisingEdge(dut.clk)

    expected = (600 + 50) & 0xFF
    actual = int(dut.uo_out.value)

    dut._log.info(f"Test2 expected={expected}, actual={actual}")
    assert actual == expected

    # Test 3
    dut.ui_in.value = 2
    dut.uio_in.value = 3

    await RisingEdge(dut.clk)

    expected = (600 + 50 + 6) & 0xFF
    actual = int(dut.uo_out.value)

    dut._log.info(f"Test3 expected={expected}, actual={actual}")
    assert actual == expected

    dut._log.info("All tests passed")
