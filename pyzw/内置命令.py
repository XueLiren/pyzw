# **************************************** A ****************************************
def 取绝对值(数):
    """
    【函数简介】
      返回一个数的绝对值。
    【函数原型】
      Python标准库-内置函数 abs()
    【参数说明】
      本参数可以是整数、浮点数或任何实现了 __abs__() 的对象。如果参数是一个复数，则返回它的模。
    :return: 绝对值
    """
    return abs(数)


def 取异步迭代器(异步可迭代对象):
    """
    【函数简介】
      返回 异步可迭代对象 的 异步迭代器。相当于调用 x.__aiter__()。

      3.10 新版功能.
    【函数原型】
      Python标准库-内置函数 aiter()
    【参数说明】
      本参数是异步可迭代对象。注意：与 iter() 不同，aiter() 没有两个参数的版本。
    :return: 异步迭代器
    """
    return aiter(异步可迭代对象)


def 全部为True(可迭代对象):
    """
    【函数简介】
      如果 可迭代对象 的所有元素均为真值True（或可迭代对象为空None）则返回 True; 否则返回 False.
    【函数原型】
      Python标准库-内置函数 all()
    【参数说明】
      本参数是可迭代对象
    :return: True 或 False
    """
    return all(可迭代对象)


def 任一为True(可迭代对象):
    """
    【函数简介】
      如果 可迭代对象 的任一元素为真值True, 则返回 True, 否则返回 False; 当 可迭代对象 为空None时, 也返回 False.
    【函数原型】
      Python标准库-内置函数 any()
    【参数说明】
      本参数是可迭代对象
    :return: True 或 False
    """
    return any(可迭代对象)


def 取异步迭代器下一项数据(异步迭代器, 完毕提示):
    """
    【函数简介】
      当进入 异步等待await 状态时，返回 异步迭代器 下一项数据; 迭代完毕则返回 完毕提示。这是内置函数next()的异步版本.

      3.10 新版功能.
    【函数原型】
      Python标准库-内置函数 anext()
    【参数说明】
      异步迭代器:
        本参数由 取异步迭代器() 命令生成
      完毕提示:
        迭代完毕时返回该参数值, 否则会触发 StopAsyncIteration 异常.
    :return:
    """
    return anext(异步迭代器, 完毕提示)


def 转ascii字符串(对象):
    """
    【函数简介】
      返回一个表示 对象 可打印形式的字符串。与repr()类似，但返回值中的非ASCII字符会用\\x、\\u 和 \\U 进行转义。
    【函数原型】
      Python标准库-内置函数 ascii()
    【参数说明】
      对象
    :return: 字符串
    """
    return ascii(对象)


# **************************************** B ****************************************
def 转二进制(整数):
    """
    【函数简介】
      将整数转变为以“0b”开头的二进制字符串。

      如果参数不是整数对象，它必须定义__index__()方法，以便返回整数值。
    【函数原型】
      Python标准库-内置函数 bin()
    【参数说明】
      整数
    :return: 字符串
    """
    return bin(整数)


def 转布尔值(*位置参数):
    """
    【函数简介】
      返回布尔(bool)值，True或False。

      如果参数为False或省略，则返回False；否则返回True。

      注意：布尔(bool)类是整数(int)的子类，它不能再被继承，它唯一的实例就是False和True。

      在 3.7 版更改为: 参数现在只能作为位置参数。
    【函数原型】
      Python标准库-内置函数 bool()
    【参数说明】
      *位置参数：可省略
    :return: 布尔值，True或False
    """
    return bool(*位置参数)


def 调试断点(*位置参数, **关键字参数):
    """
    【函数简介】
      本函数会在调用时使程序进入 pdb 调试器中，等同于导入 pdb 模块进行程序调试，而本函数纯粹是提供方便，无功能上的差异。

      注意：调试需配合 pdb 命令使用。

      3.7 新版功能
    【函数原型】
      Python标准库-内置函数 breakpoint()
    【参数说明】
      参数可省略
    :return: None
    """
    breakpoint(*位置参数, **关键字参数)


def 转字节串(*位置参数, **关键字参数):
    """
    【函数简介】
      返回一个字节串，也叫不可变字节序列。字节范围为 0≤ x ≤255 的整数。
    【函数原型】
      Python标准库-内置函数 bytes()
    【参数说明】
      1、当参数为空时，例：转为字节串()，本函数会生成一个空的字节串，等同于 b'' ；

      2、当参数为“整形可迭代对象”时，例：转为字节串(整形可迭代对象)，本函数会用可迭代对象初始化一个字节串；

      3、当参数为“整数”时，例：转为字节串(整数n)，本函数会生成n个值为0的字节串；

      4、当参数为“字符串, encoding='utf-8'[, errors='']”时，例：转为字节串(字符串, encoding='utf-8')
      或转为字节串(字符串, encoding='utf-8', errors='ignore')，本函数会用字符串的转换编码生成一个字节串；其中关键字参数errors是可选参数，
      用于指定编码时发生错误的处理方式，它可以是一个字符串，表示处理错误的方式，比如'ignore'表示忽略错误；'replace'表示用?替换错误的字符；
      'strict'表示遇到错误时抛出一个UnicodeError异常；'xmlcharrefreplace'表示将无法编码的字符替换为XML字符实体等。如果不指定errors参数，则默认为'strict'。
    :return: 字节串
    """
    return bytes(*位置参数, **关键字参数)


def 转字节数组(*位置参数, **关键字参数):
    """
    【函数简介】
      返回一个字节数组，也叫可变字节序列。字节范围为 0≤ x ≤255 的整数。
    【函数原型】
      Python标准库-内置函数 bytearray()
    【参数说明】
      1、当参数为空时，例：转为字节串()，本函数会生成一个空的字节串，等同于 b'' ；

      2、当参数为“整形可迭代对象”时，例：转为字节串(整形可迭代对象)，本函数会用可迭代对象初始化一个字节串；

      3、当参数为“整数”时，例：转为字节串(整数n)，本函数会生成n个值为0的字节串；

      4、当参数为“字符串, encoding='utf-8'[, errors='']”时，例：转为字节串(字符串, encoding='utf-8')
      或转为字节串(字符串, encoding='utf-8', errors='ignore')，本函数会用字符串的转换编码生成一个字节串；其中关键字参数errors是可选参数，
      用于指定编码时发生错误的处理方式，它可以是一个字符串，表示处理错误的方式，比如'ignore'表示忽略错误；'replace'表示用?替换错误的字符；
      'strict'表示遇到错误时抛出一个UnicodeError异常；'xmlcharrefreplace'表示将无法编码的字符替换为XML字符实体等。如果不指定errors参数，则默认为'strict'。
    :return: 字节数组
    """
    return bytearray(*位置参数, **关键字参数)


# **************************************** C ****************************************
def 检查是否可调用(对象):
    """
    【函数简介】
      如果参数 对象 是可调用的就返回 True，否则返回 False。

      注意：如果返回 True，调用仍可能失败，但返回 False，则调用肯定不会成功。 请注意类是可调用的（调用类将返回一个新的实例）；如果实例所属的类有 __call__() 则它就是可调用的。
    【函数原型】
      Python标准库-内置函数 callable()
    【参数说明】

    :return: 布尔值，True或False
    """
    return callable(对象)


def 转Unicode字符(整数):
    """
    【函数简介】
      返回整数型参数对应的Unicode字符。
    【函数原型】
      Python标准库-内置函数 chr(number)
    【参数说明】
      参数为代表有效 Unicode 代码点的整数。其合法范围是 0 到 1,114,111（16进制表示是 0x10FFFF），如果超过这个范围，会触发ValueError异常。
    :return: 字符串
    """
    return chr(整数)


def 转类方法(对象):
    """
    【函数简介】
      将函数转为类方法。

      注意：一般不使用‘classmethod()’带括号的形式来声明类方法，而是使用‘@classmethod’形式。
    【函数原型】
      Python标准库-内置函数 classmethod() 或 @classmethod
    【参数说明】
      函数
    :return: None
    """
    return classmethod(对象)


def 转字节码(*位置参数, **关键字参数):
    """
    【函数简介】
      将字符串内容转换为字节码。
    【函数原型】
      Python标准库-内置函数 compile(source, filename, mode[, flag[, dont_inherit[, optimize]]])
    【参数说明】
      *位置参数：
        source -- 必需。要编译的资源，可以是字符串、字节或 AST 对象。

        filename -- 必需。源所来自的文件的名称。如果源不是来自文件，则可以编写任何内容。

        mode	必需。合法值：
          eval - 如果源是单个表达式

          exec - 如果源是语句块

          single - 如果源是单个交互式语句
      **关键字参数：
        flags	可选。如何对源进行编译。默认为 0。

        dont-inherit	可选。如何对源进行编译。默认为 False。

        optimize	可选。定义编译器的优化级别。默认为 -1。
    :return: 字节代码
    """
    return compile(*位置参数, **关键字参数)


def 转复数(*位置参数):
    """
    【函数简介】
      通过指定实数和虚数来返回复数。
    【函数原型】
      Python标准库-内置函数 complex([real[, imag]])
    【参数说明】
      *位置参数:
        real -- 可选。代表复数实数部分的数字，默认值为 0。实数也可以是字符串，比如 '3+5j'，在这种情况下，必须省略第二个参数，否则报错。
        注意：这个地方在"+"号两边不能有空格，也就是不能写成"3 + 5j"，应该是"3+5j"，否则也会报错。

        imag -- 可选。代表复数虚数部分的数字，默认值为 0。
    :return: 复数
    """
    return complex(*位置参数)


# **************************************** D ****************************************
def 类属性_删除(类名称, 属性名称):
    """
    【函数简介】
      从指定类对象中删除指定属性。
    【函数原型】
      Python标准库-内置函数 delattr(obj, name)
    【参数说明】
      类名称 -- 必需。您希望操作的类对象名称。

      属性名称 -- 必需。您希望删除属性的名称。
    :return: None
    """
    return delattr(类名称, 属性名称)


def 转字典(*位置参数, **关键字参数):
    """
    【函数简介】
      根据传入的参数将其转为字典。共3种转换方式。
    【函数原型】
      Python标准库-内置函数 dict()
    【参数说明】
      1. 传入关键字创建字典，例：dict(a='a', b='b', t='t')；

      2. 映射函数方式创建字典，例：dict(zip(['one', 'two', 'three'], [1, 2, 3]))

      3. 可迭代对象方式创建字典，例：dict([('one', 1), ('two', 2), ('three', 3)])
    :return: 字典
    """
    return dict(*位置参数, **关键字参数)


def 查看方法和属性(*位置参数):
    """
    【函数简介】
      查看对象的方法和属性
    【函数原型】
      Python标准库-内置函数 dir([object])
    【参数说明】
      1. 不带参数时，返回当前范围内的变量、方法和定义的类型列表；

      2. 带参数时，返回参数对象的属性、方法列表。如果参数包含方法__dir__()，该方法将被调用。如果参数不包含__dir__()，该方法将最大限度地收集参数信息。
    :return: 列表
    """
    return dir(*位置参数)


def 取商和余数(数字a, 数字b):
    """
    【函数简介】
      返回一个包含由参数一除以参数二而得出的商和余数的元组。
    【函数原型】
      Python标准库-内置函数 divmod(a, b)
    【参数说明】
      数字a -- 被除数

      数字b -- 除数
    :return: 元组
    """
    return divmod(数字a, 数字b)


# **************************************** E ****************************************
def 枚举(位置参数, **关键字参数):
    """
    【函数简介】
      将一个可迭代/可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据下标和数据。一般用在 for 循环当中使用。
    【函数原型】
      Python标准库-内置函数 enumerate(iterable, [start=0])
    【参数说明】
      位置参数：
        iterable -- 可迭代对象
      **关键字参数：
        start -- 数字。下标起始位置的值。默认值为 0。
    :return: None
    """
    return enumerate(位置参数, **关键字参数)


def 执行表达式(字符串表达式, 全局命名=None, 局部命名=None):
    """
    【函数简介】
      用来执行一个字符串表达式，并返回表达式的值。
    【函数原型】
      Python标准库-内置函数 eval(expression[, globals[, locals]])
    【参数说明】
      expression -- 必需参数，字符串表达式。

      globals -- 可选参数，变量作用域，全局命名空间。如果被提供，则必须是一个字典对象。

      locals -- 可选参数，变量作用域，局部命名空间。如果被提供，可以是任何映射对象。
    :return: 表达式计算结果
    """
    if 全局命名 is None and 局部命名 is None:
        return eval(字符串表达式)
    elif 全局命名 is None:
        return eval(字符串表达式, 局部命名)
    elif 局部命名 is None:
        return eval(字符串表达式, 全局命名)


def 执行代码块(代码块, 全局命名=None, 局部命名=None):
    """
    【函数简介】
      用于动态执行指定的Python代码，无返回值。
    【函数原型】
      Python标准库-内置函数 exec(object[, globals[, locals]])
    【参数说明】
      代码块 -- 必选参数，字符串或代码对象。

      全局命名 -- 可选参数，变量作用域，全局命名空间。如果被提供，则必须是一个字典对象。

      局部命名 -- 可选参数，变量作用域，局部命名空间。如果被提供，可以是任何映射对象。
    :return: None
    """
    if 全局命名 is None and 局部命名 is None:
        return exec(代码块)
    elif 全局命名 is None:
        return exec(代码块, 局部命名)
    elif 局部命名 is None:
        return exec(代码块, 全局命名)


# **************************************** F ****************************************
def 过滤(过滤条件, 可迭代对象):
    """
    【函数简介】
      过滤掉可迭代对象中不符合条件的元素，符合条件的元素组成新的可迭代对象。

      本函数会将可迭代对象的每个元素作为参数传递给 过滤条件函数 进行判断，然后返回 True 或 False，最后将返回 True 的元素放到新的可迭代对象中。
    【函数原型】
      Python标准库-内置函数 filter(function, iterable)
    【参数说明】
      过滤条件 -- 必选参数，条件函数名称 或 None。当参数是None时，会假设它是一个判断函数，可迭代对象中所有返回False的元素都会被过滤。

      可迭代对象 -- 必选参数。
    :return: 可迭代对象
    """
    return filter(过滤条件, 可迭代对象)


def 转浮点数(值):
    """
    【函数简介】
      用于将整数或字符串转换成浮点数。
    【函数原型】
      Python标准库-内置函数 float([x])
    【参数说明】
    :param 值: 可选参数，整数或字符串。
    :return: 浮点数
    """
    return float(值)


def 格式化(值, 格式=None):
    """
    【函数简介】
      将指定值格式化为指定格式。
    【函数原型】
      Python标准库-内置函数 format(value[, format_spec])
    【参数说明】
    :param 值: 必选参数，需要格式化的值。
    :param 格式: 可选参数，将值格式化为的格式。
    :return: 字符串
    """
    if 格式 is None:
        return format(值)
    else:
        return format(值, 格式)


def 冻结(可迭代对象=None):
    """
    【函数简介】
      返回一个被冻结的可迭代对象，冻结后不能再添加或删除任何元素。
    【函数原型】
      Python标准库-内置函数 frozenset([iterable])
    【参数说明】
    :param 可迭代对象: 必选参数，如列表、集合、元组等。
    :return: 不可更改的可迭代对象
    """
    if 可迭代对象 is None:
        return frozenset()
    else:
        return frozenset(可迭代对象)


# **************************************** G ****************************************
def 类属性_取值(类名称, 属性名称, 异常返回=None):
    """
    【函数简介】
      从指定类对象中获取指定属性的值。
    【函数原型】
      Python标准库-内置函数 getattr(object, name[, default])
    【参数说明】
    :param 类名称: 必选参数。
    :param 属性名称: 必选参数。
    :param 异常返回: 可选参数，属性不存在时返回的值。
    :return: 类属性值
    """
    if 异常返回 is None:
        return getattr(类名称, 属性名称)
    else:
        return getattr(类名称, 属性名称, 异常返回)


def 全局变量():
    """
    【函数简介】
      以字典类型返回当前位置全部的全局变量。

      注意：由于变量作用域的影响，本函数的返回值与原英文函数不一致，本函数仅作翻译参考，如有需要，请使用原英文函数globals()。
    【函数原型】
      Python标准库-内置函数 globals()
    【参数说明】
      无参数
    :return: 字典
    """
    return globals()


# **************************************** H ****************************************
def 类属性_是否存在(类名称, 属性名称):
    """
    【函数简介】
      用于判断指定的类对象中是否包含指定的属性。如果包含，返回True，否则返回False。
    【函数原型】
      Python标准库-内置函数 hasattr(object, name)
    【参数说明】
    :param 类名称: 必选参数。
    :param 属性名称: 必选参数。
    :return: 布尔值，True 或 False
    """
    return hasattr(类名称, 属性名称)


def 取哈希值(对象):
    """
    【函数简介】
      获取一个对象（字符串或者数值等）的哈希值。
    【函数原型】
      Python标准库-内置函数 hash(object)
    【参数说明】
    :param 对象: 必选参数，字符串或者数值等。
    :return: 整数
    """
    return hash(对象)


def 帮助(对象=None):
    """
    【函数简介】
      有参数时，打印输出对象的详细说明。无参数时，进入系统内置的帮助系统。
    【函数原型】
      Python标准库-内置函数 help([object])
    【参数说明】
    :param 对象: 可选参数。
    :return: None
    """
    if 对象 is None:
        return help()
    else:
        return help(对象)


def 转十六进制(对象):
    """
    【函数简介】
      将十进制整数转换为以 0x 开头的十六进制字符串。
    【函数原型】
      Python标准库-内置函数 hex(x)
    【参数说明】
    :param 对象: 必选参数，整数。
    :return: 字符串
    """
    return hex(对象)


# **************************************** I ****************************************
def 取标识值(对象):
    """
    【函数简介】
      获取对象的标识值。该值在此对象的生命周期内是唯一且恒定的，但两个生命期不同的对象可能具有相同的标识值。
    【函数原型】
      Python标准库-内置函数 id(object)
    【参数说明】
    :param 对象: 必选参数。
    :return: 整数
    """
    return id(对象)


def 调试输入(提示信息=None):
    """
    【函数简介】
      允许用户在运行窗口输入数据。
    【函数原型】
      Python标准库-内置函数 input([prompt])
    【参数说明】
    :param 提示信息: 可选参数。
    :return: 字符串
    """
    if 提示信息 is None:
        return input()
    else:
        return input(提示信息)


def 转整数(对象=None, 进制数=10):
    """
    【函数简介】
      将字符串或数字转换为整数。
    【函数原型】
      Python标准库-内置函数 int([x[, base=10]])
    【参数说明】
    :param 对象: 可选参数，字符串或数字。
    :param 进制数: 可选参数，默认十进制。当此参数被提供时，对象参数必需以字符串形式提供。
    :return: 整数
    """
    if 对象 is None:
        return int()
    elif 进制数 == 10:
        return int(对象)
    else:
        return int(对象, 进制数)


# **************************************** P ****************************************
def 打印(任意数据, 分隔符=' ', 后缀='\n', 文件=None, 实时刷新=False):
    """
    【函数简介】
      本函数可以将所有的位置参数打印输出到终端窗口或指定文件。
    【函数原型】
      Python标准库-内置函数 print()
    【参数说明】
      *位置参数：
        本参数可以传递一个或多个任意类型的数据。
      **关键字参数：
        本参数包含的关键字参数分别为(sep=' ', end='\\\\n', file=None, flush=False)。其中：

        sep
          值为字符串型，表示以某字符串对打印输出内容进行分隔，默认为空格。
        end
          值为字符串型，表示在打印输出内容末尾加上某字符串，默认为换行符。
        file
          值为文件对象或None，默认值None表示打印输出到终端窗口，值为文件对象时，会将内容写入到该文件里，而不是输出到终端窗口。
        flush
          值为布尔型，默认值False表示会等到所有打印任务完毕才一次性显示输出内容，True表示会依照打印任务顺序逐个显示输出内容。
    :return: None
    """
    return print(任意数据, sep=分隔符, end=后缀, file=文件, flush=实时刷新)


def 调试输出(任意数据, 分隔符=' ', 后缀='\n', 文件=None, 实时刷新=False):
    """
    【函数简介】
      本函数可以将所有的位置参数打印输出到终端窗口或指定文件。与 打印() 命令功能一致，仅名称不同。
    【函数原型】
      Python标准库-内置函数 print()
    【参数说明】
      *位置参数：
        本参数可以传递一个或多个任意类型的数据。
      **关键字参数：
        本参数包含的关键字参数分别为(sep=' ', end='\\\\n', file=None, flush=False)。其中：

        sep
          值为字符串型，表示以某字符串对打印输出内容进行分隔，默认为空格。
        end
          值为字符串型，表示在打印输出内容末尾加上某字符串，默认为换行符。
        file
          值为文件对象或None，默认值None表示打印输出到终端窗口，值为文件对象时，会将内容写入到该文件里，而不是输出到终端窗口。
        flush
          值为布尔型，默认值False表示会等到所有打印任务完毕才一次性显示输出内容，True表示会依照打印任务顺序逐个显示输出内容。
    :return: None
    """
    return print(任意数据, sep=分隔符, end=后缀, file=文件, flush=实时刷新)
