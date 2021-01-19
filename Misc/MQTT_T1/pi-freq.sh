#!/bin/bash
# Purpose: Display the ARM CPU  frequency in MHz
# ------------------------------------------------
cpu_freq=$(</sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq)
echo "$(date) @ $(hostname)"
echo "-------------------------------------"
echo "CPU => $((cpu_freq/1000))MHz"
printf "\n"
