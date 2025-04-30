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
  %"i" = alloca i32
  store i32 0, i32* %"i"
  %"t" = alloca i8*
  store i8* bitcast ([19 x i8]* @".str.t.0" to i8*), i8** %"t"
  %"n" = alloca i8*
  store i8* bitcast ([19 x i8]* @".str.n.0" to i8*), i8** %"n"
  %".9" = load i32, i32* %"a"
  %".10" = load i32, i32* %"b"
  %".11" = icmp sgt i32 %".9", %".10"
  br i1 %".11", label %"if", label %"else"
if:
  %".13" = load i8*, i8** %"t"
  %".14" = bitcast [4 x i8]* @".fmt_s" to i8*
  %".15" = call i32 (i8*, ...) @"printf"(i8* %".14", i8* %".13")
  br label %"loop_condition"
else:
  %".32" = load i8*, i8** %"n"
  %".33" = bitcast [4 x i8]* @".fmt_s" to i8*
  %".34" = call i32 (i8*, ...) @"printf"(i8* %".33", i8* %".32")
  br label %"loop_condition.1"
merge:
  ret i32 0
loop_condition:
  %".17" = load i32, i32* %"i"
  %".18" = load i32, i32* %"a"
  %".19" = icmp slt i32 %".17", %".18"
  br i1 %".19", label %"loop_body", label %"loop_end"
loop_body:
  %".21" = load i32, i32* %"i"
  %".22" = load i32, i32* %"a"
  %".23" = mul i32 %".21", %".22"
  %".24" = bitcast [4 x i8]* @".fmt_d" to i8*
  %".25" = call i32 (i8*, ...) @"printf"(i8* %".24", i32 %".23")
  %".26" = load i32, i32* %"i"
  %".27" = add i32 %".26", 1
  store i32 %".27", i32* %"i"
  br label %"loop_condition"
loop_end:
  %".30" = load i32, i32* %"a"
  ret i32 %".30"
loop_condition.1:
  %".36" = load i32, i32* %"i"
  %".37" = load i32, i32* %"b"
  %".38" = icmp slt i32 %".36", %".37"
  br i1 %".38", label %"loop_body.1", label %"loop_end.1"
loop_body.1:
  %".40" = load i32, i32* %"i"
  %".41" = load i32, i32* %"b"
  %".42" = mul i32 %".40", %".41"
  %".43" = bitcast [4 x i8]* @".fmt_d" to i8*
  %".44" = call i32 (i8*, ...) @"printf"(i8* %".43", i32 %".42")
  %".45" = load i32, i32* %"i"
  %".46" = add i32 %".45", 1
  store i32 %".46", i32* %"i"
  br label %"loop_condition.1"
loop_end.1:
  %".49" = load i32, i32* %"b"
  ret i32 %".49"
}

@".str.t.0" = internal constant [19 x i8] c"A jest wiksze od B\00"
@".str.n.0" = internal constant [19 x i8] c"B jest wiksze od A\00"
@".fmt_s" = internal constant [4 x i8] c"%s\0a\00"
@".fmt_d" = internal constant [4 x i8] c"%d\0a\00"
@".str.str.0" = internal constant [6 x i8] c"Hello\00"
@"str" = internal global i8* bitcast ([6 x i8]* @".str.str.0" to i8*)
define void @"dummy_print_func_0"()
{
entry:
  %".2" = load i8*, i8** @"str"
  %".3" = bitcast [4 x i8]* @".fmt_s" to i8*
  %".4" = call i32 (i8*, ...) @"printf"(i8* %".3", i8* %".2")
  ret void
}

define void @"dummy_ass_func_1"()
{
entry:
  %".2" = bitcast [5 x i8]* @".str.str.2" to i8*
  store i8* %".2", i8** @"str"
  ret void
}

@".str.str.2" = internal constant [5 x i8] c"Word\00"
define void @"dummy_print_func_2"()
{
entry:
  %".2" = load i8*, i8** @"str"
  %".3" = bitcast [4 x i8]* @".fmt_s" to i8*
  %".4" = call i32 (i8*, ...) @"printf"(i8* %".3", i8* %".2")
  ret void
}

define void @"dummy_print_func_3"()
{
entry:
  %".2" = bitcast [4 x i8]* @".str.print.4" to i8*
  %".3" = bitcast [4 x i8]* @".fmt_s" to i8*
  %".4" = call i32 (i8*, ...) @"printf"(i8* %".3", i8* %".2")
  ret void
}

@".str.print.4" = internal constant [4 x i8] c"str\00"
@"a" = internal global i32 5
@"b" = internal global i32 10
@"res" = internal global i32 0
define void @"dummy_ass_func_4"()
{
entry:
  %".2" = load i32, i32* @"a"
  %".3" = load i32, i32* @"b"
  %".4" = call i32 @"max"(i32 %".2", i32 %".3")
  store i32 %".4", i32* @"res"
  ret void
}

define void @"dummy_print_func_5"()
{
entry:
  %".2" = load i32, i32* @"res"
  %".3" = bitcast [4 x i8]* @".fmt_d" to i8*
  %".4" = call i32 (i8*, ...) @"printf"(i8* %".3", i32 %".2")
  ret void
}

define i32 @"main"()
{
entry:
  call void @"dummy_print_func_0"()
  call void @"dummy_ass_func_1"()
  call void @"dummy_print_func_2"()
  call void @"dummy_print_func_3"()
  call void @"dummy_ass_func_4"()
  call void @"dummy_print_func_5"()
  ret i32 0
}
