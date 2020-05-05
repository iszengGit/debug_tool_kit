#!/bin/sh
core_pattern=/proc/sys/kernel/core_pattern
default_cont=$(cat $core_pattern)
specify_cont="/tmp/core-%e-%p-%t"
if test $default_cont != $specify_cont
then
	echo $specify_cont > $core_pattern
else
	echo "Yes, It is"
fi