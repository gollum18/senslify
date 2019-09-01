# THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY
# APPLICABLE LAW. EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT
# HOLDERS AND/OR OTHER PARTIES PROVIDE THE PROGRAM “AS IS” WITHOUT
# WARRANTY OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE. THE ENTIRE RISK AS TO THE QUALITY AND
# PERFORMANCE OF THE PROGRAM IS WITH YOU. SHOULD THE PROGRAM PROVE
# DEFECTIVE, YOU ASSUME THE COST OF ALL NECESSARY SERVICING, REPAIR OR
# CORRECTION.

# Name: filters.py
# Since: Aug 15th, 2019
# Author: Christen Ford
# Purpose: Houses filter functions for use with rendering via aiohttp_jinja2.

from babel.dates import format_datetime

def filter_datetime(dt, fmt='medium'):
    """'i18n' compliant datetime filter for jinja2.
    Taken from: https://stackoverflow.com/questions/4830535/how-do-i-format-a-date-in-jinja2
    
    Args:
        dt (datetime): The datetime instance to format.
        fmt (str): The format to use, either medium or full.
    """
    if fmt == 'full':
        fmt = "EEEE, d. MMMM y 'at' HH:mm:ss"
    elif fmt == 'medium':
        fmt = "EE dd.MM.y HH:mm:ss"
    return format_datetime(dt, fmt)
    

def filter_reading(reading):
    """Generates a formatted string for a reading.
    
    Args:
        reading (dict): A reading from a sensor.
    """
    if type(reading) is not dict:
        return 'Unable to generate format string, reading is not a dict!'
    if 'ts' not in reading or 'val' not in reading:
        return 'Unable to generate format string, reading does not contain all necessary information!'
    dt = filter_datetime(reading['ts'])
    return 'Time: {}, Value: {}'.format(dt, reading['val'])
