; ModuleID = "SimpleLang"
target triple = "x86_64-pc-windows-msvc"
target datalayout = "e-m:w-i64:64-f80:128-n8:16:32:64-S128"

@"x" = global float 0x4004000000000000
@"y" = global i32 5
define void @"dummy_func_0"()
{
entry:
  %".2" = load float, float* @"x"
}

define void @"dummy_func_1"()
{
entry:
  %".2" = fadd float 0x3ff0000000000000, %".2"
}

define void @"dummy_func_2"()
{
entry:
  store float %".2", float* @"x"
}
