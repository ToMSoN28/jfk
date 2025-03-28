; ModuleID = "SimpleLang"
target triple = "x86_64-pc-windows-msvc"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"

@"x" = global i32 2
@"y" = global i32 5
@"z" = global i32 0
define void @"dummy_func_0"()
{
entry:
  %".2" = load i32, i32* @"x"
}

define void @"dummy_func_1"()
{
entry:
  %".2" = load i32, i32* @"y"
}

define void @"dummy_func_2"()
{
entry:
  %".2" = add i32 %".2", %".2"
}

define void @"dummy_func_3"()
{
entry:
  store i32 %".2" = add i32 %".2", %".2", i32* @"z"
}

define void @"dummy_func_4"()
{
entry:
  %".2" = load i32, i32* @"z"
}
