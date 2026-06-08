/*
 * Tiny Tapeout MAC Unit
 * result = result + (A × B)
 */

`default_nettype none

module tt_um_example (
    input  wire [7:0] ui_in,     // Input A
    output wire [7:0] uo_out,    // MAC result (lower 8 bits)
    input  wire [7:0] uio_in,    // Input B
    output wire [7:0] uio_out,
    output wire [7:0] uio_oe,
    input  wire       ena,
    input  wire       clk,
    input  wire       rst_n
);

    reg [15:0] acc;

    wire [15:0] mult;

    assign mult = ui_in * uio_in;

    always @(posedge clk or negedge rst_n) begin
        if (!rst_n)
            acc <= 16'd0;
        else
            acc <= acc + mult;
    end

    // Lower 8 bits of accumulated result
    assign uo_out = acc[7:0];

    // Unused bidirectional pins
    assign uio_out = 8'b0;
    assign uio_oe  = 8'b0;

    // Prevent warnings
    wire _unused = &{ena, acc[15:8], 1'b0};

endmodule
