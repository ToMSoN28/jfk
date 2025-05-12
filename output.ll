; ModuleID = "SimpleLang"
target triple = "aarch64-apple-darwin"
target datalayout = "e-m:w-i64:64-f80:128-n8:16:32:64-S128"

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

define i32 @"max"(i32 %".1", i32 %".2")
{
entry:
  %"a" = alloca i32
  store i32 %".1", i32* %"a"
  %"b" = alloca i32
  store i32 %".2", i32* %"b"
  %"table" = alloca [20 x i32]
  %".6" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 0
  store i32 0, i32* %".6"
  %".8" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 1
  store i32 0, i32* %".8"
  %".10" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 2
  store i32 0, i32* %".10"
  %".12" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 3
  store i32 0, i32* %".12"
  %".14" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 4
  store i32 0, i32* %".14"
  %".16" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 5
  store i32 0, i32* %".16"
  %".18" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 6
  store i32 0, i32* %".18"
  %".20" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 7
  store i32 0, i32* %".20"
  %".22" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 8
  store i32 0, i32* %".22"
  %".24" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 9
  store i32 0, i32* %".24"
  %".26" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 10
  store i32 0, i32* %".26"
  %".28" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 11
  store i32 0, i32* %".28"
  %".30" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 12
  store i32 0, i32* %".30"
  %".32" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 13
  store i32 0, i32* %".32"
  %".34" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 14
  store i32 0, i32* %".34"
  %".36" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 15
  store i32 0, i32* %".36"
  %".38" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 16
  store i32 0, i32* %".38"
  %".40" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 17
  store i32 0, i32* %".40"
  %".42" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 18
  store i32 0, i32* %".42"
  %".44" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 19
  store i32 0, i32* %".44"
  %"i" = alloca i32
  store i32 0, i32* %"i"
  %"t" = alloca i8*
  store i8* bitcast ([19 x i8]* @".str.t.0" to i8*), i8** %"t"
  %"n" = alloca i8*
  store i8* bitcast ([19 x i8]* @".str.n.0" to i8*), i8** %"n"
  %".49" = load i32, i32* %"a"
  %".50" = load i32, i32* %"b"
  %".51" = icmp sgt i32 %".49", %".50"
  br i1 %".51", label %"if", label %"else"
if:
  %".53" = load i8*, i8** %"t"
  %".54" = bitcast [4 x i8]* @".fmt_s" to i8*
  %".55" = call i32 (i8*, ...) @"printf"(i8* %".54", i8* %".53")
  br label %"loop_condition"
else:
  %".141" = load i8*, i8** %"n"
  %".142" = bitcast [4 x i8]* @".fmt_s" to i8*
  %".143" = call i32 (i8*, ...) @"printf"(i8* %".142", i8* %".141")
  br label %"loop_condition.1"
merge:
  ret i32 0
loop_condition:
  %".57" = load i32, i32* %"i"
  %".58" = load i32, i32* %"a"
  %".59" = icmp slt i32 %".57", %".58"
  br i1 %".59", label %"loop_body", label %"loop_end"
loop_body:
  %".61" = load i32, i32* %"i"
  %".62" = load i32, i32* %"a"
  %".63" = mul i32 %".61", %".62"
  %".64" = bitcast [4 x i8]* @".fmt_d" to i8*
  %".65" = call i32 (i8*, ...) @"printf"(i8* %".64", i32 %".63")
  %".66" = load i32, i32* %"i"
  %".67" = load i32, i32* %"i"
  %".68" = load i32, i32* %"a"
  %".69" = mul i32 %".67", %".68"
  %".70" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 %".66"
  store i32 %".69", i32* %".70"
  %".72" = load i32, i32* %"i"
  %".73" = add i32 %".72", 1
  store i32 %".73", i32* %"i"
  br label %"loop_condition"
loop_end:
  %".76" = bitcast [4 x i8]* @".fmt_d_" to i8*
  %".77" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 0
  %".78" = load i32, i32* %".77"
  %".79" = call i32 (i8*, ...) @"printf"(i8* %".76", i32 %".78")
  %".80" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 1
  %".81" = load i32, i32* %".80"
  %".82" = call i32 (i8*, ...) @"printf"(i8* %".76", i32 %".81")
  %".83" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 2
  %".84" = load i32, i32* %".83"
  %".85" = call i32 (i8*, ...) @"printf"(i8* %".76", i32 %".84")
  %".86" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 3
  %".87" = load i32, i32* %".86"
  %".88" = call i32 (i8*, ...) @"printf"(i8* %".76", i32 %".87")
  %".89" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 4
  %".90" = load i32, i32* %".89"
  %".91" = call i32 (i8*, ...) @"printf"(i8* %".76", i32 %".90")
  %".92" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 5
  %".93" = load i32, i32* %".92"
  %".94" = call i32 (i8*, ...) @"printf"(i8* %".76", i32 %".93")
  %".95" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 6
  %".96" = load i32, i32* %".95"
  %".97" = call i32 (i8*, ...) @"printf"(i8* %".76", i32 %".96")
  %".98" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 7
  %".99" = load i32, i32* %".98"
  %".100" = call i32 (i8*, ...) @"printf"(i8* %".76", i32 %".99")
  %".101" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 8
  %".102" = load i32, i32* %".101"
  %".103" = call i32 (i8*, ...) @"printf"(i8* %".76", i32 %".102")
  %".104" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 9
  %".105" = load i32, i32* %".104"
  %".106" = call i32 (i8*, ...) @"printf"(i8* %".76", i32 %".105")
  %".107" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 10
  %".108" = load i32, i32* %".107"
  %".109" = call i32 (i8*, ...) @"printf"(i8* %".76", i32 %".108")
  %".110" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 11
  %".111" = load i32, i32* %".110"
  %".112" = call i32 (i8*, ...) @"printf"(i8* %".76", i32 %".111")
  %".113" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 12
  %".114" = load i32, i32* %".113"
  %".115" = call i32 (i8*, ...) @"printf"(i8* %".76", i32 %".114")
  %".116" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 13
  %".117" = load i32, i32* %".116"
  %".118" = call i32 (i8*, ...) @"printf"(i8* %".76", i32 %".117")
  %".119" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 14
  %".120" = load i32, i32* %".119"
  %".121" = call i32 (i8*, ...) @"printf"(i8* %".76", i32 %".120")
  %".122" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 15
  %".123" = load i32, i32* %".122"
  %".124" = call i32 (i8*, ...) @"printf"(i8* %".76", i32 %".123")
  %".125" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 16
  %".126" = load i32, i32* %".125"
  %".127" = call i32 (i8*, ...) @"printf"(i8* %".76", i32 %".126")
  %".128" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 17
  %".129" = load i32, i32* %".128"
  %".130" = call i32 (i8*, ...) @"printf"(i8* %".76", i32 %".129")
  %".131" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 18
  %".132" = load i32, i32* %".131"
  %".133" = call i32 (i8*, ...) @"printf"(i8* %".76", i32 %".132")
  %".134" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 19
  %".135" = load i32, i32* %".134"
  %".136" = call i32 (i8*, ...) @"printf"(i8* %".76", i32 %".135")
  %".137" = bitcast [2 x i8]* @".fmt_" to i8*
  %".138" = call i32 (i8*, ...) @"printf"(i8* %".137")
  %".139" = load i32, i32* %"a"
  ret i32 %".139"
loop_condition.1:
  %".145" = load i32, i32* %"i"
  %".146" = load i32, i32* %"b"
  %".147" = icmp slt i32 %".145", %".146"
  br i1 %".147", label %"loop_body.1", label %"loop_end.1"
loop_body.1:
  %".149" = load i32, i32* %"i"
  %".150" = load i32, i32* %"b"
  %".151" = mul i32 %".149", %".150"
  %".152" = bitcast [4 x i8]* @".fmt_d" to i8*
  %".153" = call i32 (i8*, ...) @"printf"(i8* %".152", i32 %".151")
  %".154" = load i32, i32* %"i"
  %".155" = load i32, i32* %"i"
  %".156" = load i32, i32* %"b"
  %".157" = mul i32 %".155", %".156"
  %".158" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 %".154"
  store i32 %".157", i32* %".158"
  %".160" = load i32, i32* %"i"
  %".161" = add i32 %".160", 1
  store i32 %".161", i32* %"i"
  br label %"loop_condition.1"
loop_end.1:
  %".164" = bitcast [4 x i8]* @".fmt_d_" to i8*
  %".165" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 0
  %".166" = load i32, i32* %".165"
  %".167" = call i32 (i8*, ...) @"printf"(i8* %".164", i32 %".166")
  %".168" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 1
  %".169" = load i32, i32* %".168"
  %".170" = call i32 (i8*, ...) @"printf"(i8* %".164", i32 %".169")
  %".171" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 2
  %".172" = load i32, i32* %".171"
  %".173" = call i32 (i8*, ...) @"printf"(i8* %".164", i32 %".172")
  %".174" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 3
  %".175" = load i32, i32* %".174"
  %".176" = call i32 (i8*, ...) @"printf"(i8* %".164", i32 %".175")
  %".177" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 4
  %".178" = load i32, i32* %".177"
  %".179" = call i32 (i8*, ...) @"printf"(i8* %".164", i32 %".178")
  %".180" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 5
  %".181" = load i32, i32* %".180"
  %".182" = call i32 (i8*, ...) @"printf"(i8* %".164", i32 %".181")
  %".183" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 6
  %".184" = load i32, i32* %".183"
  %".185" = call i32 (i8*, ...) @"printf"(i8* %".164", i32 %".184")
  %".186" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 7
  %".187" = load i32, i32* %".186"
  %".188" = call i32 (i8*, ...) @"printf"(i8* %".164", i32 %".187")
  %".189" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 8
  %".190" = load i32, i32* %".189"
  %".191" = call i32 (i8*, ...) @"printf"(i8* %".164", i32 %".190")
  %".192" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 9
  %".193" = load i32, i32* %".192"
  %".194" = call i32 (i8*, ...) @"printf"(i8* %".164", i32 %".193")
  %".195" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 10
  %".196" = load i32, i32* %".195"
  %".197" = call i32 (i8*, ...) @"printf"(i8* %".164", i32 %".196")
  %".198" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 11
  %".199" = load i32, i32* %".198"
  %".200" = call i32 (i8*, ...) @"printf"(i8* %".164", i32 %".199")
  %".201" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 12
  %".202" = load i32, i32* %".201"
  %".203" = call i32 (i8*, ...) @"printf"(i8* %".164", i32 %".202")
  %".204" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 13
  %".205" = load i32, i32* %".204"
  %".206" = call i32 (i8*, ...) @"printf"(i8* %".164", i32 %".205")
  %".207" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 14
  %".208" = load i32, i32* %".207"
  %".209" = call i32 (i8*, ...) @"printf"(i8* %".164", i32 %".208")
  %".210" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 15
  %".211" = load i32, i32* %".210"
  %".212" = call i32 (i8*, ...) @"printf"(i8* %".164", i32 %".211")
  %".213" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 16
  %".214" = load i32, i32* %".213"
  %".215" = call i32 (i8*, ...) @"printf"(i8* %".164", i32 %".214")
  %".216" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 17
  %".217" = load i32, i32* %".216"
  %".218" = call i32 (i8*, ...) @"printf"(i8* %".164", i32 %".217")
  %".219" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 18
  %".220" = load i32, i32* %".219"
  %".221" = call i32 (i8*, ...) @"printf"(i8* %".164", i32 %".220")
  %".222" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 19
  %".223" = load i32, i32* %".222"
  %".224" = call i32 (i8*, ...) @"printf"(i8* %".164", i32 %".223")
  %".225" = bitcast [2 x i8]* @".fmt_" to i8*
  %".226" = call i32 (i8*, ...) @"printf"(i8* %".225")
  %".227" = load i32, i32* %"b"
  ret i32 %".227"
}

@".str.t.0" = internal constant [19 x i8] c"A jest wiksze od B\00"
@".str.n.0" = internal constant [19 x i8] c"B jest wiksze od A\00"
@".fmt_s" = internal constant [4 x i8] c"%s\0a\00"
@".fmt_d" = internal constant [4 x i8] c"%d\0a\00"
@".fmt_d_" = internal constant [4 x i8] c"%d \00"
@".fmt_" = internal constant [2 x i8] c"\0a\00"
@"t" = internal global [3 x i32] zeroinitializer
define void @"dummy_ass_func_0"()
{
entry:
  %".2" = getelementptr [3 x i32], [3 x i32]* @"t", i32 0, i32 0
  store i32 2, i32* %".2"
  %".4" = getelementptr [3 x i32], [3 x i32]* @"t", i32 0, i32 1
  store i32 5, i32* %".4"
  %".6" = getelementptr [3 x i32], [3 x i32]* @"t", i32 0, i32 2
  store i32 8, i32* %".6"
  ret void
}

define void @"dummy_print_func_1"()
{
entry:
  %".2" = bitcast [4 x i8]* @".fmt_d_" to i8*
  %".3" = getelementptr [3 x i32], [3 x i32]* @"t", i32 0, i32 0
  %".4" = load i32, i32* %".3"
  %".5" = call i32 (i8*, ...) @"printf"(i8* %".2", i32 %".4")
  %".6" = getelementptr [3 x i32], [3 x i32]* @"t", i32 0, i32 1
  %".7" = load i32, i32* %".6"
  %".8" = call i32 (i8*, ...) @"printf"(i8* %".2", i32 %".7")
  %".9" = getelementptr [3 x i32], [3 x i32]* @"t", i32 0, i32 2
  %".10" = load i32, i32* %".9"
  %".11" = call i32 (i8*, ...) @"printf"(i8* %".2", i32 %".10")
  %".12" = bitcast [2 x i8]* @".fmt_" to i8*
  %".13" = call i32 (i8*, ...) @"printf"(i8* %".12")
  ret void
}

define void @"dummy_for_func_2"()
{
entry:
  %"i" = alloca i32
  store i32 0, i32* %"i"
  %"ele" = alloca i32
  br label %"for_cond"
for_cond:
  %"idx_val" = load i32, i32* %"i"
  %"loop_cond" = icmp slt i32 %"idx_val", 3
  br i1 %"loop_cond", label %"for_body", label %"for_end"
for_body:
  %"elem_ptr" = getelementptr [3 x i32], [3 x i32]* @"t", i32 0, i32 %"idx_val"
  %"elem_val" = load i32, i32* %"elem_ptr"
  store i32 %"elem_val", i32* %"ele"
  %".6" = load i32, i32* %"i"
  %".7" = bitcast [4 x i8]* @".fmt_d" to i8*
  %".8" = call i32 (i8*, ...) @"printf"(i8* %".7", i32 %".6")
  %".9" = load i32, i32* %"ele"
  %".10" = bitcast [4 x i8]* @".fmt_d" to i8*
  %".11" = call i32 (i8*, ...) @"printf"(i8* %".10", i32 %".9")
  %".12" = bitcast [3 x i8]* @".str.print.3" to i8*
  %".13" = bitcast [4 x i8]* @".fmt_s" to i8*
  %".14" = call i32 (i8*, ...) @"printf"(i8* %".13", i8* %".12")
  br label %"for_inc"
for_inc:
  %".16" = load i32, i32* %"i"
  %".17" = add i32 %".16", 1
  store i32 %".17", i32* %"i"
  br label %"for_cond"
for_end:
  ret void
}

@".str.print.3" = internal constant [3 x i8] c"--\00"
@".str.str.3" = internal constant [6 x i8] c"Hello\00"
@"str" = internal global i8* bitcast ([6 x i8]* @".str.str.3" to i8*)
define void @"dummy_print_func_3"()
{
entry:
  %".2" = load i8*, i8** @"str"
  %".3" = bitcast [4 x i8]* @".fmt_s" to i8*
  %".4" = call i32 (i8*, ...) @"printf"(i8* %".3", i8* %".2")
  ret void
}

define void @"dummy_ass_func_4"()
{
entry:
  %".2" = bitcast [5 x i8]* @".str.str.5" to i8*
  store i8* %".2", i8** @"str"
  ret void
}

@".str.str.5" = internal constant [5 x i8] c"Word\00"
define void @"dummy_print_func_5"()
{
entry:
  %".2" = load i8*, i8** @"str"
  %".3" = bitcast [4 x i8]* @".fmt_s" to i8*
  %".4" = call i32 (i8*, ...) @"printf"(i8* %".3", i8* %".2")
  ret void
}

define void @"dummy_print_func_6"()
{
entry:
  %".2" = bitcast [4 x i8]* @".str.print.7" to i8*
  %".3" = bitcast [4 x i8]* @".fmt_s" to i8*
  %".4" = call i32 (i8*, ...) @"printf"(i8* %".3", i8* %".2")
  ret void
}

@".str.print.7" = internal constant [4 x i8] c"str\00"
@"a" = internal global i32 5
@"b" = internal global i32 7
@"res" = internal global i32 0
define void @"dummy_ass_func_7"()
{
entry:
  %".2" = load i32, i32* @"a"
  %".3" = load i32, i32* @"b"
  %".4" = call i32 @"max"(i32 %".2", i32 %".3")
  store i32 %".4", i32* @"res"
  ret void
}

define void @"dummy_print_func_8"()
{
entry:
  %".2" = load i32, i32* @"res"
  %".3" = bitcast [4 x i8]* @".fmt_d" to i8*
  %".4" = call i32 (i8*, ...) @"printf"(i8* %".3", i32 %".2")
  ret void
}

@"matrix" = internal global [2 x [2 x i32]] [[2 x i32] [i32 1, i32 60], [2 x i32] [i32 3, i32 4]]
@"sum" = internal global i32 0
@"r" = internal global i32 0
@"max_rows" = internal global i32 2
@"c" = internal global i32 0
@"max_cols" = internal global i32 2
define void @"dummy_while_func_9"()
{
entry:
  br label %"loop_condition"
loop_condition:
  %".3" = load i32, i32* @"r"
  %".4" = load i32, i32* @"max_rows"
  %".5" = icmp slt i32 %".3", %".4"
  br i1 %".5", label %"loop_body", label %"loop_end"
loop_body:
  store i32 0, i32* @"c"
  br label %"loop_condition.1"
loop_end:
  ret void
loop_condition.1:
  %".9" = load i32, i32* @"c"
  %".10" = load i32, i32* @"max_cols"
  %".11" = icmp slt i32 %".9", %".10"
  br i1 %".11", label %"loop_body.1", label %"loop_end.1"
loop_body.1:
  %".13" = load i32, i32* @"sum"
  %".14" = load i32, i32* @"r"
  %".15" = load i32, i32* @"c"
  %"matrix_elem_ptr" = getelementptr [2 x [2 x i32]], [2 x [2 x i32]]* @"matrix", i32 0, i32 %".14", i32 %".15"
  %"matrix_elem" = load i32, i32* %"matrix_elem_ptr"
  %".16" = add i32 %".13", %"matrix_elem"
  store i32 %".16", i32* @"sum"
  %".18" = load i32, i32* @"c"
  %".19" = add i32 %".18", 1
  store i32 %".19", i32* @"c"
  br label %"loop_condition.1"
loop_end.1:
  %".22" = load i32, i32* @"r"
  %".23" = add i32 %".22", 1
  store i32 %".23", i32* @"r"
  br label %"loop_condition"
}

define void @"dummy_print_func_10"()
{
entry:
  %".2" = load i32, i32* @"sum"
  %".3" = bitcast [4 x i8]* @".fmt_d" to i8*
  %".4" = call i32 (i8*, ...) @"printf"(i8* %".3", i32 %".2")
  ret void
}

define i32 @"main"()
{
entry:
  call void @"dummy_ass_func_0"()
  call void @"dummy_print_func_1"()
  call void @"dummy_for_func_2"()
  call void @"dummy_print_func_3"()
  call void @"dummy_ass_func_4"()
  call void @"dummy_print_func_5"()
  call void @"dummy_print_func_6"()
  call void @"dummy_ass_func_7"()
  call void @"dummy_print_func_8"()
  call void @"dummy_while_func_9"()
  call void @"dummy_print_func_10"()
  ret i32 0
}
