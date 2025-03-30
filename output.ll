; ModuleID = "SimpleLang"
target triple = "x86_64-pc-windows-msvc"
target datalayout = "e-m:w-i64:64-f80:128-n8:16:32:64-S128"

define void @"dummy_func_0"()
{
entry:
  %".2" = and i1 1, 0
}

define void @"dummy_func_1"()
{
entry:
  %".2" = or i1 %".2", 1
}

@"c" = global i1 %".2"