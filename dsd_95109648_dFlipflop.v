module dFlipflop(q,d,reset,clk);
input d,reset,clk;
output q;
wire aux0,aux1,aux2;

assign aux0 = clk ? aux1 : d;
assign aux1 = reset ? 0 : aux0;
assign aux2 = clk ? aux1 : q;
assign q = reset ? 0 : aux2;

endmodule

module Top;
reg clk,d,reset;
wire q;

dFlipflop f(q,d,reset,clk);

always #1 clk = ~clk;

initial
begin
    clk = 0;
    reset = 1;
    d = 1;
    #2
    d = 1;
    reset = 0;
    #3
    d = 0;
    #3
    d = 1;
    #2
    reset = 1;
    #1
    $stop;
end

endmodule
