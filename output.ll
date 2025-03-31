; ModuleID = "SimpleLang"
target triple = "aarch64-apple-darwin"
target datalayout = "e-m:w-i64:64-f80:128-n8:16:32:64-S128"

@"c" = internal global i1 1
@"a" = internal global i32 10
define void @"dummy_func_0"()
{
entry:
  store i32 20, i32* @"a"
  ret void
}

define void @"dummy_func_1"()
{
entry:
  %".2" = load i32, i32* @"a"
  ret void
}

define i32 @"main"()
{
entry:
  call void @"dummy_func_0"()
  call void @"dummy_func_1"()
  ret i32 0
}
