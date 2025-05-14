; ModuleID = "SimpleLangModule"
target triple = "aarch64-apple-darwin"
target datalayout = "e-m:w-i64:64-f80:128-n8:16:32:64-S128"

%"struct.Student" = type {i32, i8*, i8*}
declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

define i32 @"max"(i32 %"a", i32 %"b")
{
entry:
  %"a.addr" = alloca i32
  store i32 %"a", i32* %"a.addr"
  %"b.addr" = alloca i32
  store i32 %"b", i32* %"b.addr"
  %"table" = alloca [20 x i32]
  %"table_0_ptr" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 0
  store i32 0, i32* %"table_0_ptr"
  %"table_1_ptr" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 1
  store i32 0, i32* %"table_1_ptr"
  %"table_2_ptr" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 2
  store i32 0, i32* %"table_2_ptr"
  %"table_3_ptr" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 3
  store i32 0, i32* %"table_3_ptr"
  %"table_4_ptr" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 4
  store i32 0, i32* %"table_4_ptr"
  %"table_5_ptr" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 5
  store i32 0, i32* %"table_5_ptr"
  %"table_6_ptr" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 6
  store i32 0, i32* %"table_6_ptr"
  %"table_7_ptr" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 7
  store i32 0, i32* %"table_7_ptr"
  %"table_8_ptr" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 8
  store i32 0, i32* %"table_8_ptr"
  %"table_9_ptr" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 9
  store i32 0, i32* %"table_9_ptr"
  %"table_10_ptr" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 10
  store i32 0, i32* %"table_10_ptr"
  %"table_11_ptr" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 11
  store i32 0, i32* %"table_11_ptr"
  %"table_12_ptr" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 12
  store i32 0, i32* %"table_12_ptr"
  %"table_13_ptr" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 13
  store i32 0, i32* %"table_13_ptr"
  %"table_14_ptr" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 14
  store i32 0, i32* %"table_14_ptr"
  %"table_15_ptr" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 15
  store i32 0, i32* %"table_15_ptr"
  %"table_16_ptr" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 16
  store i32 0, i32* %"table_16_ptr"
  %"table_17_ptr" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 17
  store i32 0, i32* %"table_17_ptr"
  %"table_18_ptr" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 18
  store i32 0, i32* %"table_18_ptr"
  %"table_19_ptr" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 19
  store i32 0, i32* %"table_19_ptr"
  %"i" = alloca i32
  store i32 0, i32* %"i"
  %"t" = alloca i8*
  store i8* bitcast ([19 x i8]* @".str.decl.t.0" to i8*), i8** %"t"
  %"n" = alloca i8*
  store i8* bitcast ([19 x i8]* @".str.decl.n.1" to i8*), i8** %"n"
  %"a.1" = load i32, i32* %"a.addr"
  %"b.1" = load i32, i32* %"b.addr"
  %"icmp_val" = icmp sgt i32 %"a.1", %"b.1"
  br i1 %"icmp_val", label %"if_then", label %"if_else"
if_then:
  %"t_val" = load i8*, i8** %"t"
  %".30" = bitcast [4 x i8]* @".fmt.pct_s_nl_.0" to i8*
  %".31" = call i32 (i8*, ...) @"printf"(i8* %".30", i8* %"t_val")
  br label %"loop_header"
if_else:
  %"n_val" = load i8*, i8** %"n"
  %".103" = bitcast [4 x i8]* @".fmt.pct_s_nl_.0" to i8*
  %".104" = call i32 (i8*, ...) @"printf"(i8* %".103", i8* %"n_val")
  br label %"loop_header.1"
if_merge:
  ret i32 0
loop_header:
  %"i.1" = load i32, i32* %"i"
  %"a.2" = load i32, i32* %"a.addr"
  %"icmp_val.1" = icmp slt i32 %"i.1", %"a.2"
  br i1 %"icmp_val.1", label %"loop_body", label %"loop_exit"
loop_body:
  %"i.2" = load i32, i32* %"i"
  %"a.3" = load i32, i32* %"a.addr"
  %"multmp" = mul i32 %"i.2", %"a.3"
  %".34" = bitcast [4 x i8]* @".fmt.pct_d_nl_.1" to i8*
  %".35" = call i32 (i8*, ...) @"printf"(i8* %".34", i32 %"multmp")
  %"i.3" = load i32, i32* %"i"
  %"i.4" = load i32, i32* %"i"
  %"a.4" = load i32, i32* %"a.addr"
  %"multmp.1" = mul i32 %"i.4", %"a.4"
  %"table_elem_ptr" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 %"i.3"
  store i32 %"multmp.1", i32* %"table_elem_ptr"
  %"i.5" = load i32, i32* %"i"
  %"addtmp" = add i32 %"i.5", 1
  store i32 %"addtmp", i32* %"i"
  br label %"loop_header"
loop_exit:
  %".39" = bitcast [4 x i8]* @".fmt.pct_d_.2" to i8*
  %".40" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 0
  %".41" = load i32, i32* %".40"
  %".42" = call i32 (i8*, ...) @"printf"(i8* %".39", i32 %".41")
  %".43" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 1
  %".44" = load i32, i32* %".43"
  %".45" = call i32 (i8*, ...) @"printf"(i8* %".39", i32 %".44")
  %".46" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 2
  %".47" = load i32, i32* %".46"
  %".48" = call i32 (i8*, ...) @"printf"(i8* %".39", i32 %".47")
  %".49" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 3
  %".50" = load i32, i32* %".49"
  %".51" = call i32 (i8*, ...) @"printf"(i8* %".39", i32 %".50")
  %".52" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 4
  %".53" = load i32, i32* %".52"
  %".54" = call i32 (i8*, ...) @"printf"(i8* %".39", i32 %".53")
  %".55" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 5
  %".56" = load i32, i32* %".55"
  %".57" = call i32 (i8*, ...) @"printf"(i8* %".39", i32 %".56")
  %".58" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 6
  %".59" = load i32, i32* %".58"
  %".60" = call i32 (i8*, ...) @"printf"(i8* %".39", i32 %".59")
  %".61" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 7
  %".62" = load i32, i32* %".61"
  %".63" = call i32 (i8*, ...) @"printf"(i8* %".39", i32 %".62")
  %".64" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 8
  %".65" = load i32, i32* %".64"
  %".66" = call i32 (i8*, ...) @"printf"(i8* %".39", i32 %".65")
  %".67" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 9
  %".68" = load i32, i32* %".67"
  %".69" = call i32 (i8*, ...) @"printf"(i8* %".39", i32 %".68")
  %".70" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 10
  %".71" = load i32, i32* %".70"
  %".72" = call i32 (i8*, ...) @"printf"(i8* %".39", i32 %".71")
  %".73" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 11
  %".74" = load i32, i32* %".73"
  %".75" = call i32 (i8*, ...) @"printf"(i8* %".39", i32 %".74")
  %".76" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 12
  %".77" = load i32, i32* %".76"
  %".78" = call i32 (i8*, ...) @"printf"(i8* %".39", i32 %".77")
  %".79" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 13
  %".80" = load i32, i32* %".79"
  %".81" = call i32 (i8*, ...) @"printf"(i8* %".39", i32 %".80")
  %".82" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 14
  %".83" = load i32, i32* %".82"
  %".84" = call i32 (i8*, ...) @"printf"(i8* %".39", i32 %".83")
  %".85" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 15
  %".86" = load i32, i32* %".85"
  %".87" = call i32 (i8*, ...) @"printf"(i8* %".39", i32 %".86")
  %".88" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 16
  %".89" = load i32, i32* %".88"
  %".90" = call i32 (i8*, ...) @"printf"(i8* %".39", i32 %".89")
  %".91" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 17
  %".92" = load i32, i32* %".91"
  %".93" = call i32 (i8*, ...) @"printf"(i8* %".39", i32 %".92")
  %".94" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 18
  %".95" = load i32, i32* %".94"
  %".96" = call i32 (i8*, ...) @"printf"(i8* %".39", i32 %".95")
  %".97" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 19
  %".98" = load i32, i32* %".97"
  %".99" = call i32 (i8*, ...) @"printf"(i8* %".39", i32 %".98")
  %".100" = bitcast [2 x i8]* @".fmt._nl_.3" to i8*
  %".101" = call i32 (i8*, ...) @"printf"(i8* %".100")
  %"a.5" = load i32, i32* %"a.addr"
  ret i32 %"a.5"
loop_header.1:
  %"i.6" = load i32, i32* %"i"
  %"b.2" = load i32, i32* %"b.addr"
  %"icmp_val.2" = icmp slt i32 %"i.6", %"b.2"
  br i1 %"icmp_val.2", label %"loop_body.1", label %"loop_exit.1"
loop_body.1:
  %"i.7" = load i32, i32* %"i"
  %"b.3" = load i32, i32* %"b.addr"
  %"multmp.2" = mul i32 %"i.7", %"b.3"
  %".107" = bitcast [4 x i8]* @".fmt.pct_d_nl_.1" to i8*
  %".108" = call i32 (i8*, ...) @"printf"(i8* %".107", i32 %"multmp.2")
  %"i.8" = load i32, i32* %"i"
  %"i.9" = load i32, i32* %"i"
  %"b.4" = load i32, i32* %"b.addr"
  %"multmp.3" = mul i32 %"i.9", %"b.4"
  %"table_elem_ptr.1" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 %"i.8"
  store i32 %"multmp.3", i32* %"table_elem_ptr.1"
  %"i.10" = load i32, i32* %"i"
  %"addtmp.1" = add i32 %"i.10", 1
  store i32 %"addtmp.1", i32* %"i"
  br label %"loop_header.1"
loop_exit.1:
  %".112" = bitcast [4 x i8]* @".fmt.pct_d_.2" to i8*
  %".113" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 0
  %".114" = load i32, i32* %".113"
  %".115" = call i32 (i8*, ...) @"printf"(i8* %".112", i32 %".114")
  %".116" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 1
  %".117" = load i32, i32* %".116"
  %".118" = call i32 (i8*, ...) @"printf"(i8* %".112", i32 %".117")
  %".119" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 2
  %".120" = load i32, i32* %".119"
  %".121" = call i32 (i8*, ...) @"printf"(i8* %".112", i32 %".120")
  %".122" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 3
  %".123" = load i32, i32* %".122"
  %".124" = call i32 (i8*, ...) @"printf"(i8* %".112", i32 %".123")
  %".125" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 4
  %".126" = load i32, i32* %".125"
  %".127" = call i32 (i8*, ...) @"printf"(i8* %".112", i32 %".126")
  %".128" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 5
  %".129" = load i32, i32* %".128"
  %".130" = call i32 (i8*, ...) @"printf"(i8* %".112", i32 %".129")
  %".131" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 6
  %".132" = load i32, i32* %".131"
  %".133" = call i32 (i8*, ...) @"printf"(i8* %".112", i32 %".132")
  %".134" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 7
  %".135" = load i32, i32* %".134"
  %".136" = call i32 (i8*, ...) @"printf"(i8* %".112", i32 %".135")
  %".137" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 8
  %".138" = load i32, i32* %".137"
  %".139" = call i32 (i8*, ...) @"printf"(i8* %".112", i32 %".138")
  %".140" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 9
  %".141" = load i32, i32* %".140"
  %".142" = call i32 (i8*, ...) @"printf"(i8* %".112", i32 %".141")
  %".143" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 10
  %".144" = load i32, i32* %".143"
  %".145" = call i32 (i8*, ...) @"printf"(i8* %".112", i32 %".144")
  %".146" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 11
  %".147" = load i32, i32* %".146"
  %".148" = call i32 (i8*, ...) @"printf"(i8* %".112", i32 %".147")
  %".149" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 12
  %".150" = load i32, i32* %".149"
  %".151" = call i32 (i8*, ...) @"printf"(i8* %".112", i32 %".150")
  %".152" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 13
  %".153" = load i32, i32* %".152"
  %".154" = call i32 (i8*, ...) @"printf"(i8* %".112", i32 %".153")
  %".155" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 14
  %".156" = load i32, i32* %".155"
  %".157" = call i32 (i8*, ...) @"printf"(i8* %".112", i32 %".156")
  %".158" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 15
  %".159" = load i32, i32* %".158"
  %".160" = call i32 (i8*, ...) @"printf"(i8* %".112", i32 %".159")
  %".161" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 16
  %".162" = load i32, i32* %".161"
  %".163" = call i32 (i8*, ...) @"printf"(i8* %".112", i32 %".162")
  %".164" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 17
  %".165" = load i32, i32* %".164"
  %".166" = call i32 (i8*, ...) @"printf"(i8* %".112", i32 %".165")
  %".167" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 18
  %".168" = load i32, i32* %".167"
  %".169" = call i32 (i8*, ...) @"printf"(i8* %".112", i32 %".168")
  %".170" = getelementptr [20 x i32], [20 x i32]* %"table", i32 0, i32 19
  %".171" = load i32, i32* %".170"
  %".172" = call i32 (i8*, ...) @"printf"(i8* %".112", i32 %".171")
  %".173" = bitcast [2 x i8]* @".fmt._nl_.3" to i8*
  %".174" = call i32 (i8*, ...) @"printf"(i8* %".173")
  %"b.5" = load i32, i32* %"b.addr"
  ret i32 %"b.5"
}

@".str.decl.t.0" = internal constant [19 x i8] c"A jest wiksze od B\00"
@".str.decl.n.1" = internal constant [19 x i8] c"B jest wiksze od A\00"
@".fmt.pct_s_nl_.0" = internal constant [4 x i8] c"%s\0a\00"
@".fmt.pct_d_nl_.1" = internal constant [4 x i8] c"%d\0a\00"
@".fmt.pct_d_.2" = internal constant [4 x i8] c"%d \00"
@".fmt._nl_.3" = internal constant [2 x i8] c"\0a\00"
@"t" = internal global [3 x i32] zeroinitializer
define void @"dummy_table_assign_func_2"()
{
entry:
  %"t_0_ptr" = getelementptr [3 x i32], [3 x i32]* @"t", i32 0, i32 0
  store i32 2, i32* %"t_0_ptr"
  %"t_1_ptr" = getelementptr [3 x i32], [3 x i32]* @"t", i32 0, i32 1
  store i32 5, i32* %"t_1_ptr"
  %"t_2_ptr" = getelementptr [3 x i32], [3 x i32]* @"t", i32 0, i32 2
  store i32 8, i32* %"t_2_ptr"
  ret void
}

define void @"dummy_print_func_3"()
{
entry:
  %".2" = bitcast [4 x i8]* @".fmt.pct_d_.2" to i8*
  %".3" = getelementptr [3 x i32], [3 x i32]* @"t", i32 0, i32 0
  %".4" = load i32, i32* %".3"
  %".5" = call i32 (i8*, ...) @"printf"(i8* %".2", i32 %".4")
  %".6" = getelementptr [3 x i32], [3 x i32]* @"t", i32 0, i32 1
  %".7" = load i32, i32* %".6"
  %".8" = call i32 (i8*, ...) @"printf"(i8* %".2", i32 %".7")
  %".9" = getelementptr [3 x i32], [3 x i32]* @"t", i32 0, i32 2
  %".10" = load i32, i32* %".9"
  %".11" = call i32 (i8*, ...) @"printf"(i8* %".2", i32 %".10")
  %".12" = bitcast [2 x i8]* @".fmt._nl_.3" to i8*
  %".13" = call i32 (i8*, ...) @"printf"(i8* %".12")
  ret void
}

define void @"dummy_for_func_4"()
{
entry:
  %"i" = alloca i32
  store i32 0, i32* %"i"
  %"ele" = alloca i32
  br label %"for_header"
for_header:
  %"current_idx" = load i32, i32* %"i"
  %"for_cond" = icmp slt i32 %"current_idx", 3
  br i1 %"for_cond", label %"for_body", label %"for_exit"
for_body:
  %"actual_elem_ptr" = getelementptr [3 x i32], [3 x i32]* @"t", i32 0, i32 %"current_idx"
  %"actual_elem_val" = load i32, i32* %"actual_elem_ptr"
  store i32 %"actual_elem_val", i32* %"ele"
  %"i_val" = load i32, i32* %"i"
  %".6" = bitcast [4 x i8]* @".fmt.pct_d_nl_.1" to i8*
  %".7" = call i32 (i8*, ...) @"printf"(i8* %".6", i32 %"i_val")
  %"ele_val" = load i32, i32* %"ele"
  %".8" = bitcast [4 x i8]* @".fmt.pct_d_nl_.1" to i8*
  %".9" = call i32 (i8*, ...) @"printf"(i8* %".8", i32 %"ele_val")
  %"str_ptr" = bitcast [3 x i8]* @".str.literal.5" to i8*
  %".10" = bitcast [4 x i8]* @".fmt.pct_s_nl_.0" to i8*
  %".11" = call i32 (i8*, ...) @"printf"(i8* %".10", i8* %"str_ptr")
  %"new_idx" = add i32 %"current_idx", 1
  store i32 %"new_idx", i32* %"i"
  br label %"for_header"
for_exit:
  ret void
}

@".str.literal.5" = internal constant [3 x i8] c"--\00"
@".str.decl.str.6" = internal constant [6 x i8] c"Hello\00"
@"str" = internal global i8* bitcast ([6 x i8]* @".str.decl.str.6" to i8*)
define void @"dummy_print_func_7"()
{
entry:
  %"str_val" = load i8*, i8** @"str"
  %".2" = bitcast [4 x i8]* @".fmt.pct_s_nl_.0" to i8*
  %".3" = call i32 (i8*, ...) @"printf"(i8* %".2", i8* %"str_val")
  ret void
}

define void @"dummy_assign_func_8"()
{
entry:
  %"str_ptr" = bitcast [5 x i8]* @".str.literal.9" to i8*
  store i8* %"str_ptr", i8** @"str"
  ret void
}

@".str.literal.9" = internal constant [5 x i8] c"Word\00"
define void @"dummy_print_func_10"()
{
entry:
  %"str_val" = load i8*, i8** @"str"
  %".2" = bitcast [4 x i8]* @".fmt.pct_s_nl_.0" to i8*
  %".3" = call i32 (i8*, ...) @"printf"(i8* %".2", i8* %"str_val")
  ret void
}

define void @"dummy_print_func_11"()
{
entry:
  %"str_ptr" = bitcast [4 x i8]* @".str.literal.12" to i8*
  %".2" = bitcast [4 x i8]* @".fmt.pct_s_nl_.0" to i8*
  %".3" = call i32 (i8*, ...) @"printf"(i8* %".2", i8* %"str_ptr")
  ret void
}

@".str.literal.12" = internal constant [4 x i8] c"str\00"
@"a" = internal global i32 5
@"b" = internal global i32 7
@"res" = internal global i32 0
define void @"dummy_assign_func_13"()
{
entry:
  %"a" = load i32, i32* @"a"
  %"b" = load i32, i32* @"b"
  %"max_res" = call i32 @"max"(i32 %"a", i32 %"b")
  store i32 %"max_res", i32* @"res"
  ret void
}

define void @"dummy_print_func_14"()
{
entry:
  %"res_val" = load i32, i32* @"res"
  %".2" = bitcast [4 x i8]* @".fmt.pct_d_nl_.1" to i8*
  %".3" = call i32 (i8*, ...) @"printf"(i8* %".2", i32 %"res_val")
  ret void
}

@"matrix" = internal global [2 x [2 x i32]] [[2 x i32] [i32 1, i32 60], [2 x i32] [i32 3, i32 4]]
@"sum" = internal global i32 0
@"r" = internal global i32 0
@"max_rows" = internal global i32 2
@"c" = internal global i32 0
@"max_cols" = internal global i32 2
define void @"dummy_while_func_15"()
{
entry:
  br label %"loop_header"
loop_header:
  %"r" = load i32, i32* @"r"
  %"max_rows" = load i32, i32* @"max_rows"
  %"icmp_val" = icmp slt i32 %"r", %"max_rows"
  br i1 %"icmp_val", label %"loop_body", label %"loop_exit"
loop_body:
  store i32 0, i32* @"c"
  br label %"loop_header.1"
loop_exit:
  ret void
loop_header.1:
  %"c" = load i32, i32* @"c"
  %"max_cols" = load i32, i32* @"max_cols"
  %"icmp_val.1" = icmp slt i32 %"c", %"max_cols"
  br i1 %"icmp_val.1", label %"loop_body.1", label %"loop_exit.1"
loop_body.1:
  %"sum" = load i32, i32* @"sum"
  %"r.1" = load i32, i32* @"r"
  %"c.1" = load i32, i32* @"c"
  %"matrix_elem_ptr" = getelementptr [2 x [2 x i32]], [2 x [2 x i32]]* @"matrix", i32 0, i32 %"r.1", i32 %"c.1"
  %"matrix_elem" = load i32, i32* %"matrix_elem_ptr"
  %"addtmp" = add i32 %"sum", %"matrix_elem"
  store i32 %"addtmp", i32* @"sum"
  %"c.2" = load i32, i32* @"c"
  %"addtmp.1" = add i32 %"c.2", 1
  store i32 %"addtmp.1", i32* @"c"
  br label %"loop_header.1"
loop_exit.1:
  %"r.2" = load i32, i32* @"r"
  %"addtmp.2" = add i32 %"r.2", 1
  store i32 %"addtmp.2", i32* @"r"
  br label %"loop_header"
}

define void @"dummy_print_func_16"()
{
entry:
  %"sum_val" = load i32, i32* @"sum"
  %".2" = bitcast [4 x i8]* @".fmt.pct_d_nl_.1" to i8*
  %".3" = call i32 (i8*, ...) @"printf"(i8* %".2", i32 %"sum_val")
  ret void
}

@"Adam" = internal global %"struct.Student" zeroinitializer
define void @"__global_struct_assign_17"()
{
entry:
  %"Adam.nr_indeksu.ptr" = getelementptr %"struct.Student", %"struct.Student"* @"Adam", i32 0, i32 0
  store i32 123, i32* %"Adam.nr_indeksu.ptr"
  ret void
}

define void @"__global_struct_assign_18"()
{
entry:
  %"str_ptr" = bitcast [5 x i8]* @".str.literal.19" to i8*
  %"Adam.imie.ptr" = getelementptr %"struct.Student", %"struct.Student"* @"Adam", i32 0, i32 1
  store i8* %"str_ptr", i8** %"Adam.imie.ptr"
  ret void
}

@".str.literal.19" = internal constant [5 x i8] c"Adam\00"
define void @"__global_struct_assign_20"()
{
entry:
  %"str_ptr" = bitcast [10 x i8]* @".str.literal.21" to i8*
  %"Adam.nazwisko.ptr" = getelementptr %"struct.Student", %"struct.Student"* @"Adam", i32 0, i32 2
  store i8* %"str_ptr", i8** %"Adam.nazwisko.ptr"
  ret void
}

@".str.literal.21" = internal constant [10 x i8] c"Chilinski\00"
@"Tomasz" = internal global %"struct.Student" zeroinitializer
define void @"__global_struct_assign_22"()
{
entry:
  %"Tomasz.nr_indeksu.ptr" = getelementptr %"struct.Student", %"struct.Student"* @"Tomasz", i32 0, i32 0
  store i32 456, i32* %"Tomasz.nr_indeksu.ptr"
  ret void
}

define void @"__global_struct_assign_23"()
{
entry:
  %"str_ptr" = bitcast [7 x i8]* @".str.literal.24" to i8*
  %"Tomasz.imie.ptr" = getelementptr %"struct.Student", %"struct.Student"* @"Tomasz", i32 0, i32 1
  store i8* %"str_ptr", i8** %"Tomasz.imie.ptr"
  ret void
}

@".str.literal.24" = internal constant [7 x i8] c"Tomasz\00"
define void @"__global_struct_assign_25"()
{
entry:
  %"str_ptr" = bitcast [9 x i8]* @".str.literal.26" to i8*
  %"Tomasz.nazwisko.ptr" = getelementptr %"struct.Student", %"struct.Student"* @"Tomasz", i32 0, i32 2
  store i8* %"str_ptr", i8** %"Tomasz.nazwisko.ptr"
  ret void
}

@".str.literal.26" = internal constant [9 x i8] c"Kowalski\00"
define void @"dummy_print_func_27"()
{
entry:
  %"nr_indeksu_ptr" = getelementptr %"struct.Student", %"struct.Student"* @"Adam", i32 0, i32 0
  %"nr_indeksu" = load i32, i32* %"nr_indeksu_ptr"
  %".2" = bitcast [4 x i8]* @".fmt.pct_d_nl_.1" to i8*
  %".3" = call i32 (i8*, ...) @"printf"(i8* %".2", i32 %"nr_indeksu")
  ret void
}

define void @"dummy_print_func_28"()
{
entry:
  %"nr_indeksu_ptr" = getelementptr %"struct.Student", %"struct.Student"* @"Tomasz", i32 0, i32 0
  %"nr_indeksu" = load i32, i32* %"nr_indeksu_ptr"
  %".2" = bitcast [4 x i8]* @".fmt.pct_d_nl_.1" to i8*
  %".3" = call i32 (i8*, ...) @"printf"(i8* %".2", i32 %"nr_indeksu")
  ret void
}

define i32 @"main"()
{
entry:
  call void @"dummy_table_assign_func_2"()
  call void @"dummy_print_func_3"()
  call void @"dummy_for_func_4"()
  call void @"dummy_print_func_7"()
  call void @"dummy_assign_func_8"()
  call void @"dummy_print_func_10"()
  call void @"dummy_print_func_11"()
  call void @"dummy_assign_func_13"()
  call void @"dummy_print_func_14"()
  call void @"dummy_while_func_15"()
  call void @"dummy_print_func_16"()
  call void @"__global_struct_assign_17"()
  call void @"__global_struct_assign_18"()
  call void @"__global_struct_assign_20"()
  call void @"__global_struct_assign_22"()
  call void @"__global_struct_assign_23"()
  call void @"__global_struct_assign_25"()
  call void @"dummy_print_func_27"()
  call void @"dummy_print_func_28"()
  ret i32 0
}
