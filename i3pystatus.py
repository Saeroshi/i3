# -*- coding: utf-8 -*-
#
import subprocess
import os
import os.path

from i3pystatus import Status


status = Status()

status.register("clock",
    format="%X %a %-d %b ")

status.register("battery",
    battery_ident="BAT0",
    interval=5,
    format=" {percentage_design:.2f}% {status}{consumption:.2f}W {remaining:%E%hh:%Mm}",
    alert=True,
    alert_percentage=10,
    color="#FFFFFF",
    critical_color="#FF1919",
    charging_color="#E5E500",
    full_color="#D19A66",
    status={
        "DIS": "",
        "CHR": "",
        "FULL": "",
},)

status.register("cpu_usage",
    on_leftclick="xfce4-terminal --command htop --hide-menubar",
    format=" {usage}%")

status.register("mem",
    hints = {"separator": False},
    on_leftclick="xfce4-terminal --command htop --hide-menubar",
    color="#999999",
    warn_color="#E5E500",
    alert_color="#FF1919",
    format=" {used_mem}/{total_mem}G",
    divisor=1073741824)

status.register("pulseaudio",
    color_unmuted='#98C379',
    color_muted='#E06C75',
    format_muted='♪ MUTE',
    format="♪ {volume}%")

status.register("openvpn",
    format=":{status}",
    status_down="",
    status_up="",
    vpn_name="saeroshi",
    status_command="bash -c 'if [ -d /sys/class/net/tun0 ];then echo up;fi'")

status.register("network",
    hints = {"separator": False},
    interface="enp1s0",
    color_up="#8AE234",
    color_down="#EF2929",
    format_up=" ",
    format_down=" ",
    on_leftclick="xfce4-terminal --command nmtui --hide-menubar")

status.register("network",
    hints = {"separator": False},
    interface="wlp2s0",
    color_up="#8AE234",
    color_down="#EF2929",
    format_up=" {essid}",
    format_down=" ",
    on_leftclick="xfce4-terminal --command nmtui --hide-menubar")


status.register("disk",
    color='#56B6C2',
    path="/home",
    critical_limit=10,
    interval=30,
    on_leftclick="thunar",
    format=" {avail}G",)

status.register("disk",
    hints = {"separator": False},
    color='#ABB2BF',
    critical_limit=1,
    interval=30,
    path="/",
    format=" {avail}G",)

status.register("keyboard_locks",
    format='{caps} {num}',
    caps_on='Maj On',
    caps_off='',
    num_on='Num On',
    num_off='',
    color='#e60053')

status.run()
