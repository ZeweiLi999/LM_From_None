#用于测试各函数的文件
import numpy as np
from Core.Function import Function
from Core.Variable import Variable
from Core.Square import Square
from Core.Exp import Exp
from Core.Add import Add

if __name__ == "__main__":
    A = Exp()
    B = Square()
    C = Square()
    D = Add()

    x = Variable(np.array(0.5))
    a = A(x)
    b = B(a)
    d = D(a,b)
    y = C(b)

    #assert用法：如果后面的语句不为ture，就会抛出异常
    assert y.creator == C #y的创造函数是C
    assert y.creator.inputs[0] == b
    assert y.creator.inputs[0].creator == B
    assert y.creator.inputs[0].creator.inputs[0] == a
    assert y.creator.inputs[0].creator.inputs[0].creator == A
    assert y.creator.inputs[0].creator.inputs[0].creator.inputs[0] == x


    generations = [2,0,1,4,2]
    funcs = []
    for g in generations:
        f = Function()
        f.generation = g
        funcs.append(f)
    funcs.sort(key = lambda x: x.generation)
    print([f.generation for f in funcs])
    f = funcs.pop()
    print(f.generation)


