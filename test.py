class GeneratorChain:
    def inner_most(self):
        """最内层生成器 - 真正的数据源"""
        print("  inner_most: 产生 'A'")
        yield "A"
        print("  inner_most: 产生 'B'")
        yield "B"
        print("  inner_most: 产生 'C'")
        yield "C"
    
    def middle(self):
        """中层生成器 - 直接委托"""
        print("middle: 准备委托给 inner_most")
        yield from self.inner_most()
        print("middle: 委托完成")
    
    def outer(self):
        """外层生成器 - 手动遍历"""
        print("outer: 准备进入循环")
        for chunk in self.middle():
            print(f"outer: 收到 '{chunk}'，准备 yield")
            yield chunk
            print(f"outer: 已 yield '{chunk}'，继续循环")
        print("outer: 循环结束")

# 测试
chain = GeneratorChain()
print("=== 开始遍历外层 ===")
for value in chain.outer():
    print(f"调用端收到: {value}\n")

# 输出：
# === 开始遍历外层 ===
# outer: 准备进入循环
# middle: 准备委托给 inner_most
# inner_most: 产生 'A'
# outer: 收到 'A'，准备 yield
# 调用端收到: A
# 
# outer: 已 yield 'A'，继续循环
# inner_most: 产生 'B'
# outer: 收到 'B'，准备 yield
# 调用端收到: B
# 
# outer: 已 yield 'B'，继续循环
# inner_most: 产生 'C'
# outer: 收到 'C'，准备 yield
# 调用端收到: C
# 
# outer: 已 yield 'C'，继续循环
# middle: 委托完成
# outer: 循环结束