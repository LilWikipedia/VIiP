# VIiP_Kivy_Mobile_Framework

    {'input': 'for{3|4}', 'expected': '(3,4)'},
    {'input': 'for{false?}', 'expected': '()'},
    {'input': 'for(x:=10|20; x>10; y:=1|2|3; y<3)do(x+y)', 'expected': '(21,22)'}, # <- filtering variables
    {'input': 'for(x:=10|20; y:=1|2|3)do(x+y)', 'expected': '(11,12,13,21,22,23)'},
    {'input': 'for(x:=2|3|5)do(x+1)', 'expected': '(3,4,6)'},
    {'input': 't:=(1,1,1); for(i:int;x:=t[i]) do (x+i)', 'expected': '(1,2,3)'}, # <- indexing still work in progress
    {'input': 't:=(1,2,3); for(i:int;x:=t[1]) do (x)', 'expected': '(2)'},
    {'input': 'ys:= (12,22,23); xs:= (1,2,3,4); for{((i:int;ys[i])|(s:int; xs[s]))}', 'expected': '(12,22,23,1,2,3,4)'}, # append
    {'input': 'xs:= (1,2,3,4); for{i:int; i > 0; xs[i]}', 'expected': '(2,3,4)'}, # tail
    {'input': 't:=for{1|2}; t[0]', 'expected': '1'}, # head
    {'input': 'ys:= (1,2); xs:= (3,4); for{a=2; i:int; (xs[i], ys[i], a:int)}', 'expected': '((3,1,2),(4,2,2))'},
    {'input': 'for{i=2;z=20;(i:int)..(z:int)}', 'expected': '(2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)'},
    {'input': 'for(x:=2|3|5; x > 2)do(x+(1|2))', 'expected': '((4,6)|(4,7)|(5,6)|(5,7))'},
    {'input': 'for(x:=10|20) do (x | x+1)', 'expected': '((10,20)|(10,21)|(11,20)|(11,21))'},)
