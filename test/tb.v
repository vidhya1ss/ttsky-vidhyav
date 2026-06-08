`default_nettype none
`timescale 1ns/1ps

module tb;

    // Inputs
    reg clk;
    reg rst_n;
    reg ena;
    reg [7:0] ui_in;
    reg [7:0] uio_in;

    // Outputs
    wire [7:0] uo_out;
    wire [7:0] uio_out;
    wire [7:0] uio_oe;

`ifdef GL_TEST
    wire VPWR = 1'b1;
    wire VGND = 1'b0;
`endif

    // Instantiate DUT
    tt_um_example dut (
`ifdef GL_TEST
        .VPWR(VPWR),
        .VGND(VGND),
`endif
        .ui_in(ui_in),
        .uo_out(uo_out),
        .uio_in(uio_in),
        .uio_out(uio_out),
        .uio_oe(uio_oe),
        .ena(ena),
        .clk(clk),
        .rst_n(rst_n)
    );

    // Dump waveform
    initial begin
        $dumpfile("tb.fst");
        $dumpvars(0, tb);
    end

    // Clock generation (100 MHz)
    initial begin
        clk = 0;
        forever #5 clk = ~clk;
    end

    // Test sequence
    initial begin

        rst_n  = 0;
        ena    = 1;
        ui_in  = 8'd0;
        uio_in = 8'd0;

        #20;
        rst_n = 1;

        // Test 1: A=3, B=4
        ui_in  = 8'd3;
        uio_in = 8'd4;
        #20;

        // Test 2: A=5, B=2
        ui_in  = 8'd5;
        uio_in = 8'd2;
        #20;

        // Test 3: A=7, B=6
        ui_in  = 8'd7;
        uio_in = 8'd6;
        #20;

        // Test 4: A=10, B=10
        ui_in  = 8'd10;
        uio_in = 8'd10;
        #20;

        $finish;
    end

endmodule
