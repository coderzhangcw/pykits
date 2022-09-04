"""时区
pip install python-dateutil
"""
from datetime import datetime
from dateutil import tz


def tz_conversion(str_time, 
                  original_zone="UTC", 
                  original_time_format="%Y-%m-%d %H:%M:%S",
                  out_zone="CST",
                  out_time_format="%Y-%m-%d %H:%M:%S"):
    """格式化输出北京时间。
    时区: UTC CST
    时间格式: %Y-%m-%d %H:%M:%S   %Y-%m-%dT%H:%M:%S.%fZ
    
    Args:
        str_time (string): 时间
        original_zone (string): 原始时间的时区, 默认UTC时间
        original_time_format (string): 原始时间格式，默认%Y-%m-%d %H:%M:%S
        out_zone (string): 输出时区，默认北京时间
        out_time_format (string): 输出时间格式，默认%Y-%m-%d %H:%M:%S

    Returns:
        result(string): 转化了时区的时间
    """
    datetime_obj = datetime.strptime(str_time, original_time_format)
    # UTC Zone
    original_zone = tz.gettz(original_zone)
    # China Zone
    out_zone = tz.gettz(out_zone)

    datetime_obj = datetime_obj.replace(tzinfo=original_zone)

    local = datetime_obj.astimezone(out_zone)
    return datetime.strftime(local, out_time_format)

if __name__ == "__main__":
    str_time = "2022-07-11 12:22:40"
    result = tz_conversion(str_time)
    print(result)


