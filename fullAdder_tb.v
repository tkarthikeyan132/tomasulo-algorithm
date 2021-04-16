// Full Adder test bench

`include "fullAdder.v"

module top;
reg a, b, cin;  // they should hold one bit value input, thus 'reg' (input sholuld always be reg)
wire sum, ca;     // output should be 'wire'

fullAdder FullAdd_0 (a, b, cin, sum, ca); // fullAdder is instantiated in this file

initial   // initializing values
begin
	a = 1'b1;
	b = 1'b0;
	cin = 1'b0;
end

initial
	$monitor("%b,%b",sum, ca);
	// $monitor("%0t     a = %b ; b = %b; cin = %b; sum = %b; ca = %b",$time, a, b, cin ,sum, ca);
	
endmodule
	
