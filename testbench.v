`include "Verilog_source_files/RecursiveAdder32bit/RecursiveAdder.v"








module top();
reg[31:0] a, b;  // they should hold one bit value input, thus 'reg' (input sholuld always be reg)
wire[31:0] out;     // output should be 'wire'
//

RecursiveAdder A(out, a, b);

initial   // initializing values
begin
	a = 32'b00000000000000000000000000100101;
	b = 32'b00000000000000000000000000011101;
end

initial
	$monitor("%b",out[31:0]);
	// $monitor("%0t     a = %b ; b = %b; cin = %b; sum = %b; ca = %b",$time, a, b, cin ,sum, ca);
endmodule
	
// Lines to be changed: (1, (13), 15, 19, 20)
// corresponding indices: (0, (12), 14, 18, 19)