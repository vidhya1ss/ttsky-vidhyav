`default_nettype none

module tt_um_example (
    input  wire [7:0] ui_in,
    output wire [7:0] uo_out,
    input  wire [7:0] uio_in,
    output wire [7:0] uio_out,
    output wire [7:0] uio_oe,
    input  wire       ena,
    input  wire       clk,
    input  wire       rst_n
);

    reg [15:0] acc;

    always @(posedge clk or negedge rst_n) begin
        if (!rst_n)
            acc <= 16'd0;
        else if (ena)
            acc <= acc + (ui_in * uio_in);
    end

    assign uo_out  = acc[7:0];
    assign uio_out = 8'h00;
    assign uio_oe  = 8'h00;

    wire _unused = &{1'b0, acc[15:8]};

endmodule

`default_nettype wire
