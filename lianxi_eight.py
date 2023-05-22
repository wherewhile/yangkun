#自定义异常用raise抛出异常
def fn():
    try:
        for i in range(5):
            if i>2:
                raise Exception("数字大于2")
    except Exception as ret:
        print(ret)
fn()