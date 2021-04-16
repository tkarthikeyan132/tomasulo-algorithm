module fullAdder(a, b, cin, sum, ca);
input a, b, cin;
output sum, ca;

/*             Gate level modelling                 */
wire w1, w2, w3, w4, w5;

xor xor_0(w1, a, b);         // w1 = a xor b 
xor xor_1(sum, w1, cin);         // w1 = a xor b 

and and_0(w2, a, b);         // w2 = a and b
and and_1(w3, a, cin);         // w2 = a and b
and and_2(w4, b, cin);         // w2 = a and b
or or_0(w5, w2, w3);
or or_1(ca, w4, w5);

endmodule
