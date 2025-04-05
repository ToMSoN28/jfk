; ModuleID = "SimpleLang"
target triple = "aarch64-apple-darwin"
target datalayout = "e-m:w-i64:64-f80:128-n8:16:32:64-S128"

declare i32 @"printf"(i8* %".1", ...)

@"c" = internal global i1 1
@"a" = internal global i32 10
@"b" = internal global float 0x4024333340000000
define void @"dummy_func_0"()
{
entry:
  %".2" = load i32, i32* @"a"
  %".3" = bitcast [4 x i8]* @".fmt1" to i8*
  %".4" = call i32 (i8*, ...) @"printf"(i8* %".3", i32 %".2")
  ret void
}

@".fmt1" = internal constant [4 x i8] c"%d\0a\00"
define void @"dummy_func_1"()
{
entry:
  %".2" = load float, float* @"b"
  %".3" = bitcast [4 x i8]* @".fmt2" to i8*
  %".4" = call i32 (i8*, ...) @"printf"(i8* %".3", float %".2")
  ret void
}

@".fmt2" = internal constant [4 x i8] c"%f\0a\00"
define i32 @"main"()
{
entry:
  call void @"dummy_func_0"()
  call void @"dummy_func_1"()
  ret i32 0
}
