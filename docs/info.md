<!---

This file is used to generate your project datasheet. Please fill in the information below and delete any unused
sections.

You can also include images in this folder and reference them in the markdown. Each image must be less than
512 kb in size, and the combined size of all images must be less than 1 MB.
-->

## How it works

The SMAC (Serial Multiply-Accumulate) unit performs multiplication of two input operands and accumulates the result over multiple clock cycles. The design receives two 8-bit input values through the Tiny Tapeout input pins. On every clock cycle, the multiplier computes the product of the inputs and adds it to an internal accumulator register. The accumulated result is provided at the output pins. The accumulator is cleared when the reset signal is asserted. This architecture is commonly used in digital signal processing (DSP), neural networks, and filtering applications where repeated multiply-accumulate operations are required.

## How to test

Apply a reset signal (rst_n = 0) to clear the accumulator.
Release reset (rst_n = 1).
Provide input operand A through ui_in[7:0].
Provide input operand B through uio_in[7:0].
Apply clock pulses.
Observe the output on uo_out[7:0].
Verify that the output corresponds to the accumulated sum of the multiplication results over successive clock cycles.
Repeat with different input values and compare the output against the expected MAC operation result.

## External hardware

No external hardware is required for the basic operation of this project. The design can be tested entirely through simulation and the Tiny Tapeout test infrastructure.


