; ModuleID = "SimpleLang"
target triple = "aarch64-apple-darwin"
target datalayout = "e-m:w-i64:64-f80:128-n8:16:32:64-S128"

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

@"a" = internal global double 0x3ff0000000000000
define void @"dummy_print_func_0"()
{
entry:
  %".2" = load double, double* @"a"
  %".3" = bitcast [4 x i8]* @".fmt_f" to i8*
  %".4" = call i32 (i8*, ...) @"printf"(i8* %".3", double %".2")
  ret void
}

@".fmt_f" = internal constant [4 x i8] c"%f\0a\00"
define i32 @"main"()
{
entry:
  call void @"dummy_print_func_0"()
  ret i32 0
}
