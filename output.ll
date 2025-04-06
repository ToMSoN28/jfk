; ModuleID = "SimpleLang"
target triple = "aarch64-apple-darwin"
target datalayout = "e-m:w-i64:64-f80:128-n8:16:32:64-S128"

declare i32 @"printf"(i8* %".1", ...)

@"a" = internal global float 0x3ff0000000000000
@"b" = internal global float 0x4000000000000000
@"c" = internal global float              0x0
define void @"dummy_ass_func_0"()
{
entry:
  %".2" = load float, float* @"a"
  %".3" = load float, float* @"b"
  %".4" = fadd float %".2", %".3"
  store float %".4", float* @"c"
  ret void
}

define void @"dummy_print_func_1"()
{
entry:
  %".2" = load float, float* @"c"
  %".3" = bitcast [4 x i8]* @".fmt2" to i8*
  %".4" = call i32 (i8*, ...) @"printf"(i8* %".3", float %".2")
  ret void
}

@".fmt2" = internal constant [4 x i8] c"%f\0a\00"
@"aa" = internal global i1 1
@"bb" = internal global i1 0
@"dd" = internal global i1 1
@"cc" = internal global i1 0
define void @"dummy_print_func_2"()
{
entry:
  %".2" = load i1, i1* @"cc"
  %".3" = bitcast [4 x i8]* @".fmt3" to i8*
  %".4" = call i32 (i8*, ...) @"printf"(i8* %".3", i1 %".2")
  ret void
}

@".fmt3" = internal constant [4 x i8] c"%d\0a\00"
define i32 @"main"()
{
entry:
  call void @"dummy_ass_func_0"()
  call void @"dummy_print_func_1"()
  call void @"dummy_print_func_2"()
  ret i32 0
}
