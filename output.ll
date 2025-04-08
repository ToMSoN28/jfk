; ModuleID = "SimpleLang"
target triple = "x86_64-pc-windows-msvc"
target datalayout = "e-m:w-i64:64-f80:128-n8:16:32:64-S128"

declare i32 @"printf"(i8* %".1", ...)

@"a" = internal global double 0x3ff0000000000000
@"b" = internal global double 0x4000e147ae147ae1
@"c" = internal global double 0x40091eb851eb851f
define void @"dummy_print_func_0"()
{
entry:
  %".2" = load double, double* @"c"
  %".3" = bitcast [4 x i8]* @".fmt_f" to i8*
  %".4" = call i32 (i8*, ...) @"printf"(i8* %".3", double %".2")
  ret void
}

@".fmt_f" = internal constant [4 x i8] c"%f\0a\00"
define void @"dummy_ass_func_1"()
{
entry:
  %".2" = load double, double* @"a"
  %".3" = load double, double* @"b"
  %".4" = fadd double %".2", %".3"
  store double %".4", double* @"c"
  ret void
}

define void @"dummy_print_func_2"()
{
entry:
  %".2" = load double, double* @"c"
  %".3" = bitcast [4 x i8]* @".fmt_f" to i8*
  %".4" = call i32 (i8*, ...) @"printf"(i8* %".3", double %".2")
  ret void
}

@"x" = internal global i32 1
define void @"dummy_print_func_3"()
{
entry:
  %".2" = load i32, i32* @"x"
  %".3" = bitcast [4 x i8]* @".fmt_d" to i8*
  %".4" = call i32 (i8*, ...) @"printf"(i8* %".3", i32 %".2")
  ret void
}

@".fmt_d" = internal constant [4 x i8] c"%d\0a\00"
@"aa" = internal global i1 1
define void @"dummy_print_func_4"()
{
entry:
  %".2" = load i1, i1* @"aa"
  %".3" = zext i1 %".2" to i32
  %".4" = bitcast [4 x i8]* @".fmt_d" to i8*
  %".5" = call i32 (i8*, ...) @"printf"(i8* %".4", i32 %".3")
  ret void
}

@"bb" = internal global i1 0
define void @"dummy_print_func_5"()
{
entry:
  %".2" = load i1, i1* @"bb"
  %".3" = zext i1 %".2" to i32
  %".4" = bitcast [4 x i8]* @".fmt_d" to i8*
  %".5" = call i32 (i8*, ...) @"printf"(i8* %".4", i32 %".3")
  ret void
}

@"dd" = internal global i1 1
@"cc" = internal global i1 1
define void @"dummy_ass_func_6"()
{
entry:
  %".2" = load i1, i1* @"bb"
  %".3" = load i1, i1* @"dd"
  %"and_result" = alloca i1
  br i1 %".2", label %"and_rhs", label %"and_false"
and_rhs:
  %".5" = load i1, i1* @"dd"
  store i1 %".5", i1* %"and_result"
  br label %"and_merge"
and_false:
  store i1 0, i1* %"and_result"
  br label %"and_merge"
and_merge:
  %".10" = load i1, i1* %"and_result"
  %"or_result" = alloca i1
  br i1 0, label %"or_true", label %"or_rhs"
or_true:
  store i1 1, i1* %"or_result"
  br label %"or_merge"
or_rhs:
  %".14" = load i1, i1* @"bb"
  %".15" = load i1, i1* @"dd"
  %"and_result.1" = alloca i1
  br i1 %".14", label %"and_rhs.1", label %"and_false.1"
or_merge:
  %".25" = load i1, i1* %"or_result"
  store i1 %".25", i1* @"cc"
  ret void
and_rhs.1:
  %".17" = load i1, i1* @"dd"
  store i1 %".17", i1* %"and_result.1"
  br label %"and_merge.1"
and_false.1:
  store i1 0, i1* %"and_result.1"
  br label %"and_merge.1"
and_merge.1:
  %".22" = load i1, i1* %"and_result.1"
  store i1 %".22", i1* %"or_result"
  br label %"or_merge"
}

define void @"dummy_print_func_7"()
{
entry:
  %".2" = load i1, i1* @"cc"
  %".3" = zext i1 %".2" to i32
  %".4" = bitcast [4 x i8]* @".fmt_d" to i8*
  %".5" = call i32 (i8*, ...) @"printf"(i8* %".4", i32 %".3")
  ret void
}

define void @"dummy_ass_func_8"()
{
entry:
  %".2" = load i1, i1* @"dd"
  %".3" = load i1, i1* @"bb"
  %".4" = load i1, i1* @"dd"
  %"and_result" = alloca i1
  br i1 %".3", label %"and_rhs", label %"and_false"
and_rhs:
  %".6" = load i1, i1* @"dd"
  store i1 %".6", i1* %"and_result"
  br label %"and_merge"
and_false:
  store i1 0, i1* %"and_result"
  br label %"and_merge"
and_merge:
  %".11" = load i1, i1* %"and_result"
  %"or_result" = alloca i1
  br i1 %".2", label %"or_true", label %"or_rhs"
or_true:
  store i1 1, i1* %"or_result"
  br label %"or_merge"
or_rhs:
  %".15" = load i1, i1* @"bb"
  %".16" = load i1, i1* @"dd"
  %"and_result.1" = alloca i1
  br i1 %".15", label %"and_rhs.1", label %"and_false.1"
or_merge:
  %".26" = load i1, i1* %"or_result"
  store i1 %".26", i1* @"cc"
  ret void
and_rhs.1:
  %".18" = load i1, i1* @"dd"
  store i1 %".18", i1* %"and_result.1"
  br label %"and_merge.1"
and_false.1:
  store i1 0, i1* %"and_result.1"
  br label %"and_merge.1"
and_merge.1:
  %".23" = load i1, i1* %"and_result.1"
  store i1 %".23", i1* %"or_result"
  br label %"or_merge"
}

define void @"dummy_print_func_9"()
{
entry:
  %".2" = load i1, i1* @"cc"
  %".3" = zext i1 %".2" to i32
  %".4" = bitcast [4 x i8]* @".fmt_d" to i8*
  %".5" = call i32 (i8*, ...) @"printf"(i8* %".4", i32 %".3")
  ret void
}

define void @"dummy_ass_func_10"()
{
entry:
  %".2" = load double, double* @"c"
  %".3" = load double, double* @"b"
  %".4" = fadd double %".2", %".3"
  store double %".4", double* @"c"
  ret void
}

define void @"dummy_print_func_11"()
{
entry:
  %".2" = load double, double* @"c"
  %".3" = bitcast [4 x i8]* @".fmt_f" to i8*
  %".4" = call i32 (i8*, ...) @"printf"(i8* %".3", double %".2")
  ret void
}

define i32 @"main"()
{
entry:
  call void @"dummy_print_func_0"()
  call void @"dummy_ass_func_1"()
  call void @"dummy_print_func_2"()
  call void @"dummy_print_func_3"()
  call void @"dummy_print_func_4"()
  call void @"dummy_print_func_5"()
  call void @"dummy_ass_func_6"()
  call void @"dummy_print_func_7"()
  call void @"dummy_ass_func_8"()
  call void @"dummy_print_func_9"()
  call void @"dummy_ass_func_10"()
  call void @"dummy_print_func_11"()
  ret i32 0
}
