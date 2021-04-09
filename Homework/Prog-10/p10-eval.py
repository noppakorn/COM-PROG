assert get_embedded_text_from_image( "data/5x5_A.png") == "A"
assert get_embedded_text_from_image( "data/5x5_AB.png") == "AB"
assert get_embedded_text_from_image( "data/5x5_ABC.png") == "ABC"
 	 
assert get_embedded_text_from_image( "data/5x5_none0.png") == ""
assert get_embedded_text_from_image( "data/5x5_none1.png") == ""
assert get_embedded_text_from_image( "data/5x5_none2.png") == ""
 	 
assert get_embedded_text_from_image( "data/2x20_DEF456OPQ.png") == "DEF456OPQ"
assert get_embedded_text_from_image( "data/4x10_DEF456OPQ.png") == "DEF456OPQ"
assert get_embedded_text_from_image( "data/1x200_ABCXYZ0123789.png") == "ABCXYZ0123789"
assert get_embedded_text_from_image( "data/200x1_ABCXYZ0123789.png") == "ABCXYZ0123789"
# This one text is long but pass assert get_embedded_text_from_image( "data/26x23_long_text.png" )	 
 	 
assert get_embedded_text_from_image( "data/2x19_Error.png") == ""
assert get_embedded_text_from_image( "data/2x20_Error_last_bit.png") == ""

#embed_text_to_image("A", "data/5x5_rand.png", "out.png")	ดูเฉพาะ [0:16]
#embed_text_to_image("A", "data/5x5_rand.png", "out.png")	ดูเฉพาะ [16:32]
#embed_text_to_image("A", "data/5x5_rand.png", "out.png")	ดูเฉพาะ [32:40]
#embed_text_to_image("A", "data/5x5_rand.png", "out.png")	ดูเฉพาะ [40:56]
# 	 
#embed_text_to_image("AB", "data/5x5_rand.png", "out.png")	 
#embed_text_to_image("ABC", "data/5x5_rand.png", "out.png")	 
# 	 
#embed_text_to_image("987654321", "data/2x20.png", "out.png")	 
#embed_text_to_image("2110101 Comp Prog.\n"*11, "/data/26x23.png", "out.png")	 
 	 
assert embed_text_to_image("WXYZ", "data/5x5_rand.png", "out.png") == False
assert embed_text_to_image("0987654321", "data/2x20.png", "out.png") == False