"""数据处理

"""
from datetime import datetime
from decimal import Decimal
from decimal import ROUND_HALF_UP


def format_decimal(
    str_num: str, 
    precise: str='0.00', 
    rounding: str=ROUND_HALF_UP) -> Decimal:
    """格式化输出decimal数值。
    Args:
        str_num (string): decimal数值
        precise (string): 精度，'0.000':保留3位
        rounding (string): 精度策略, ROUND_HALF_UP:四舍五入

    Returns:
        result(string): 成功 - 运算结果，'' - 其他
    """
    format_output = Decimal(str_num).quantize(Decimal(precise), rounding=ROUND_HALF_UP)
    return format_output


if __name__ == "__main__":
    str_num = "12.09553"
    result = format_decimal(str_num)
    print(result)

